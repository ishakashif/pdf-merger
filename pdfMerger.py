import streamlit as st
import PyPDF2
import os
from tempfile import NamedTemporaryFile

st.title("PDF Merger")
st.write("Upload multiple PDF files to merge them into a single PDF.")

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    merger = PyPDF2.PdfMerger()
    temp_files = []
    for uploaded_file in uploaded_files:
        # Save uploaded file to a temporary file
        temp_file = NamedTemporaryFile(delete=False, suffix=".pdf")
        temp_file.write(uploaded_file.read())
        temp_file.flush()
        temp_files.append(temp_file)
        merger.append(temp_file.name)
    
    output_path = "merged.pdf"
    merger.write(output_path)
    merger.close()

    with open(output_path, "rb") as f:
        st.download_button(
            label="Download Merged PDF",
            data=f,
            file_name="merged.pdf",
            mime="application/pdf"
        )
    # Clean up temp files
    for temp_file in temp_files:
        temp_file.close()
        os.unlink(temp_file.name)
    os.remove(output_path)

file_names = [f.name for f in uploaded_files]
new_order = st.multiselect("Select the order of the files", file_names, default=file_names)

if len(new_order) == len(file_names):
    ordered_files = [next(f for f in uploaded_files if f.name == name) for name in new_order]
    # add more color themes for the buttons