import streamlit as st
import matplotlib.pyplot as plt

def render_ats_chart(score):
    st.subheader('📈 ATS Compatibility Chart')
    labels = ['Optimized', 'Remaining']
    values = [score, 100 - score]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)
