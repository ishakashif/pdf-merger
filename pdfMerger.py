import gradio as gr
import PyPDF2
import os

def merge_pdfs(pdf_paths):  # pdf_paths is a list of string file paths
    merger = PyPDF2.PdfMerger()
    output_path = "merged.pdf"

    for path in pdf_paths:
        merger.append(path)

    merger.write(output_path)
    merger.close()
    return output_path

iface = gr.Interface(
    fn=merge_pdfs,
    inputs=gr.File(label="Upload PDF files", file_count="multiple", type="filepath"),
    outputs=gr.File(label="Merged PDF"),
    title="PDF Merger",
    description="Upload multiple PDF files to merge them into a single PDF."
)

if __name__ == "__main__":
    iface.launch()
