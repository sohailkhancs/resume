import os

def create_ui_structure():
    base_dir = os.path.join(os.getcwd(), "ui")
    components_dir = os.path.join(base_dir, "components")

    dirs = [base_dir, components_dir]

    for d in dirs:
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "__init__.py"), "a").close()

    print("[+] UI directory structure created successfully.")

    files = {
        os.path.join(base_dir, "dashboard.py"): """import streamlit as st
from ui.components.sidebar import render_sidebar
from ui.components.progress_bar import render_progress_bar
from ui.components.charts import render_ats_chart

def main():
    st.set_page_config(page_title='AI Resume Enhancer', layout='wide')
    st.title('🚀 AI Resume Enhancer Dashboard')

    uploaded_file = render_sidebar()
    if uploaded_file:
        st.success('File uploaded successfully!')
        render_progress_bar(80)
        render_ats_chart(80)
        st.write('Next: Integrate ATS Analyzer and AI Optimizer modules.')
    else:
        st.info('Please upload your resume to begin.')

    st.markdown('---')
    st.caption('Phase 3 – Prototype Interface')

if __name__ == '__main__':
    main()
""",

        os.path.join(components_dir, "sidebar.py"): """import streamlit as st

def render_sidebar():
    st.sidebar.header('📁 Upload Your Resume')
    return st.sidebar.file_uploader('Choose a PDF file', type=['pdf'])
""",

        os.path.join(components_dir, "progress_bar.py"): """import streamlit as st
import time

def render_progress_bar(score):
    st.subheader('📊 ATS Optimization Progress')
    progress = st.progress(0)
    for i in range(score + 1):
        progress.progress(i)
        time.sleep(0.01)
    st.success(f'Optimization Score: {score}%')
""",

        os.path.join(components_dir, "charts.py"): """import streamlit as st
import matplotlib.pyplot as plt

def render_ats_chart(score):
    st.subheader('📈 ATS Compatibility Chart')
    labels = ['Optimized', 'Remaining']
    values = [score, 100 - score]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)
"""
    }

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    print("[+] All UI files created successfully.")

if __name__ == "__main__":
    create_ui_structure()
