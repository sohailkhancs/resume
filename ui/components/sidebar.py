import streamlit as st

def render_sidebar():
    st.sidebar.header('📁 Upload Your Resume')
    return st.sidebar.file_uploader('Choose a PDF file', type=['pdf'])
