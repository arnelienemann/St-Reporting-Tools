import reportautomation
import segmentation_analysis
import wordclouds

import streamlit as st

PAGES = {
    "Report Automation": reportautomation,
    "Wordcloud": wordclouds,
    "Segmentation Analysis": segmentation_analysis
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Please select your application:", list(PAGES.keys()))
page = PAGES[selection]
page.app()

#python -m streamlit run app.py