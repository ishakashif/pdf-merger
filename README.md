# PDF Merger

A simple Python program to merge multiple PDF files into a single document.

## Features

- Merge any number of PDF files into one
- Easy to use and customize
- Works on macOS, Windows, and Linux

## Requirements

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-merger.git
   cd pdf-merger
   ```

2. **Install dependencies:**
   ```bash
   pip install PyPDF2
   ```

## Usage

1. Place the PDF files you want to merge inside the `pdf files/` directory.

2. Run the merger script:
   ```bash
   python pdfMerger.py
   ```

3. The merged PDF will be saved in the project directory (or as specified in the script).

## Customization

- You can modify the script to change the output filename or the directory where merged files are saved.
- To merge PDFs in a specific order, rename them or adjust the file list in the script.

## Example

Suppose you have:
- `pdf files/Document1.pdf`
- `pdf files/Document2.pdf`

After running the script, you’ll get a single merged PDF containing both documents.

## License

This project is open source
