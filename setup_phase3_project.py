#!/usr/bin/env python3
"""
setup_phase3_project.py
Creates the Phase-3-ready directory structure and writes boilerplate files.
Run: python setup_phase3_project.py
"""

import os
import textwrap

BASE = "resume_enhancer"

# ========== Boilerplate file contents ==========
files = {
    # Top-level
    f"{BASE}/README.md": textwrap.dedent("""\
        # ATS-Smart Resume Enhancer (Phase 3)
        Professional-grade resume analyzer + LLM optimization + JD matching.
        Run:
            pip install -r resume_enhancer/requirements.txt
            streamlit run resume_enhancer/app.py
        """),

    f"{BASE}/requirements.txt": textwrap.dedent("""\
        streamlit
        PyMuPDF
        reportlab
        fpdf
        sentence-transformers
        scikit-learn
        faiss-cpu
        openai
        altair
        pandas
        language_tool_python
        matplotlib
        wordcloud
        """),

    f"{BASE}/app.py": textwrap.dedent("""\
        import streamlit as st
        from ui import dashboard

        if __name__ == '__main__':
            st.set_page_config(page_title='ATS Resume Enhancer Pro', layout='wide')
            dashboard.app()
        """),
}

# ========== helper to write files ==========
def ensure_dir_for_file(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def write_all(files_map):
    for path, content in files_map.items():
        ensure_dir_for_file(path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created: {path}")

if __name__ == "__main__":
    print("🚀 Creating Phase 3 project structure...")
    write_all(files)
    print("\n✅ Done! Project scaffold created under ./resume_enhancer")
    print("Next steps:")
    print("  1) cd resume_enhancer")
    print("  2) pip install -r requirements.txt")
    print("  3) streamlit run app.py")
