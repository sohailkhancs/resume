import streamlit as st
from ui import dashboard

if __name__ == '__main__':
    st.set_page_config(page_title='ATS Resume Enhancer Pro', layout='wide')
    dashboard.app()
