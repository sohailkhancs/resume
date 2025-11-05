import streamlit as st
import time

def render_progress_bar(score):
    st.subheader('📊 ATS Optimization Progress')
    progress = st.progress(0)
    for i in range(score + 1):
        progress.progress(i)
        time.sleep(0.01)
    st.success(f'Optimization Score: {score}%')
