import PyPDF2
import sys
import os


merger = PyPDF2.PdfFileMerger()
pdf_folder = 'pdf-files'


for file in sorted(os.listdir(pdf_folder)):
    if file.endswith('.pdf'):
        filepath = os.path.join(pdf_folder, file)
        print(f"Merging: {filepath}")
        merger.append(filepath)
    
        
merger.write('merged.pdf')
merger.close()