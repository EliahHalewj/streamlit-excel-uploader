
import streamlit as st
import pandas as pd

st.title("Excel File Uploader")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        # Use appropriate engine based on file extension
        file_extension = uploaded_file.name.split('.')[-1]
        engine = 'openpyxl' if file_extension == 'xlsx' else 'xlrd'

        df = pd.read_excel(uploaded_file, engine=engine)
        st.success("File uploaded and read successfully!")
        st.write(df.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")
