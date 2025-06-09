import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pubchempy as pcp
import requests
from io import BytesIO

def search():
    query = entry.get().strip()
    search_type = search_option.get()

    if not query:
        messagebox.showwarning("Input Required", "Please enter a query.")
        return

    try:
        compounds = pcp.get_compounds(query, search_type)
        if not compounds:
            raise IndexError

        compound = compounds[0]
        synonyms = ', '.join(compound.synonyms[:3]) if compound.synonyms else 'N/A'

        result = f"""
IUPAC Name:       {compound.iupac_name}
Common Name(s):   {synonyms}
Molecular Weight: {compound.molecular_weight}
Formula:          {compound.molecular_formula}
CID:              {compound.cid}
        """.strip()

        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state='disabled')

        img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{compound.cid}/PNG"
        response = requests.get(img_url)

        if response.ok and response.headers['Content-Type'] == 'image/png' and len(response.content) > 1000:
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img_data)

            image_label.config(image=img_tk, text='')
            image_label.image = img_tk
        else:
            image_label.config(image='', text='[No structure available]')
            image_label.image = None

    except IndexError:
        messagebox.showerror("Not Found", f"No data found for '{query}' using {search_type}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Chemical Info Finder")

tk.Label(root, text="Enter Search Term:").pack()
entry = tk.Entry(root, width=40)
entry.pack()
search_option = tk.StringVar(value='name')
options = ['name', 'formula', 'cid', 'smiles']
tk.OptionMenu(root, search_option, *options).pack(pady=5)
tk.Button(root, text="Search", command=search).pack(pady=5)
frame = tk.Frame(root)
frame.pack()

output_text = tk.Text(frame, width=60, height=10, state='disabled', wrap='word')
output_text.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame, command=output_text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

output_text.config(yscrollcommand=scroll.set)

image_label = tk.Label(root, text='[No structure shown]', font=('Arial', 12), pady=10)
image_label.pack()

entry.bind("<Return>", lambda event: search())
root.mainloop()
