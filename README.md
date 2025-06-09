
---

# 🧪 Chemical Info Finder

A simple Python GUI app to search for chemical compound data using the [PubChem](https://pubchem.ncbi.nlm.nih.gov/) API. This tool allows users to retrieve information such as IUPAC name, molecular weight, chemical formula, and more—complete with structure images.

## ✨ Features

* Search by:

  * Name (default)
  * Formula
  * CID
  * SMILES
* Retrieves and displays:

  * IUPAC Name
  * Common Synonyms
  * Molecular Formula
  * Molecular Weight
  * Compound CID
* Downloads and shows compound structure image from PubChem
* Built with `Tkinter` for a clean and simple GUI

## 🖼️ Screenshot

![Image Alt](https://github.com/tajulislamsaidul/-Chemical-Info/blob/24bb44e808222b91097868f0d5f3ba53d2356da4/DEMO.png)

## 🛠️ Requirements

* Python 3.x
* [pubchempy](https://pypi.org/project/PubChemPy/)
* [Pillow](https://pypi.org/project/Pillow/)
* requests

### Install dependencies

```bash
pip install pubchempy Pillow requests
```

## 🚀 How to Run

```bash
python "Chemical Info Finder.py"
```

## 💡 Usage

1. Enter a search term (e.g., "glucose").
2. Select the search type from the dropdown.
3. Click **Search** or press **Enter**.
4. View the retrieved information and structure image (if available).

## ❗ Notes

* Make sure you are connected to the internet—the app fetches data and images live from PubChem.
* If no image is available, a `[No structure available]` message will be shown.

  
---
