import streamlit as st
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
