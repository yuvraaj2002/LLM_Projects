import os
import streamlit as st
import pdfplumber
import pandas as pd

def show_pdf_file(uploaded_file):
    file_container = st.expander("Press to see your PDF file 📄")
    with pdfplumber.open(uploaded_file) as pdf:
        pdf_text = ""
        for page in pdf.pages:
            pdf_text += page.extract_text() + "\n\n"
    file_container.write(pdf_text)


def show_txt_file(uploaded_file):
    file_container = st.expander("Press to see your TXT file 📄")
    uploaded_file.seek(0)
    content = uploaded_file.read().decode("utf-8")
    file_container.write(content)

def show_csv_file(uploaded_file):
    file_container = st.expander("Press to see your CSV file 📄")
    uploaded_file.seek(0)
    shows = pd.read_csv(uploaded_file)
    file_container.write(shows)


def get_file_extension(uploaded_file):
    """
    This method will take the file object as input and will return the extension of
    the file uploaded by the user.
    """
    return os.path.splitext(uploaded_file)[1].lower()


class Handle_Files:

    @staticmethod
    def file_upload(file_types):
        """
        This method display uploaded_file and return the uploaded file object
        :param file_types: List of accepted file types, e.g., ["csv", "pdf", "txt"]
        """

        # Let's take the file as input from the user
        uploaded_file = st.sidebar.file_uploader("upload", type=file_types, label_visibility="collapsed")
        if uploaded_file is not None:

            # Let's make function call for get_file_extension
            uploaded_file_extension = get_file_extension(uploaded_file.name)

            # Show the contents of the file based on its extension
            if uploaded_file_extension == ".csv":
                show_csv_file(uploaded_file)
            elif uploaded_file_extension == ".pdf":
                show_pdf_file(uploaded_file)
            elif uploaded_file_extension == ".txt":
                show_txt_file(uploaded_file)

        else:
            st.session_state["chat_history_cleared"] = True

        return uploaded_file
