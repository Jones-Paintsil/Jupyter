

# Importing necessary libraries
import streamlit as st
import numpy as np
import pandas as pd

def app_page_1():

    import streamlit as st
    # Function to apply color to text using Markdown
def color_text(text, color):
    return f'<span style="color:{color};">{text}</span>'

# Define colors
title_color = "#008080"  # Dark cyan
subtitle_color = "#800080"  # Purple
text_color = "#000000"  # Black

# Title and Authors
st.markdown(f'<h1 style="color:{title_color};">THE DATA SCIENCE PROCESS USING PYTHON AND STREAMLIT</h1>', unsafe_allow_html=True)
authors = "Authors: Chiehhsiung Chang, Kerneka Waldron, Naiya Jackson, Sally Amankwah, Jones A. Paintsil"
st.markdown(f"<p style='color:{text_color};'>{authors}</p>", unsafe_allow_html=True)

# Introduction
st.markdown(f"<h2 style='color:{subtitle_color};'>Introduction</h2>", unsafe_allow_html=True)
intro_text = """
Data science is a multidisciplinary field that uses scientific methods, mathematical models, algorithms, and systems to explore patterns in data, both structured and unstructured, to provide helpful information for policymakers, business corporations, medicine, and almost all aspects of life. Data science processes start with data collection. There are seven data science processes. They are data collection, data cleaning, data exploration, data preparation, model training, model evaluation, and model deployment. In this exercise, we employed the 2018 HBCU dataset to show the various procedures involved in executing the data science processes.
"""
st.markdown(f"<p style='color:{text_color};'>{intro_text}</p>", unsafe_allow_html=True)

# Executive Summary
st.markdown(f"<h2 style='color:{subtitle_color};'>EXECUTIVE SUMMARY</h2>", unsafe_allow_html=True)
summary_text = """
**Title:** Determinants of Enrollment in Historically Black Colleges and Universities (HBCUs).

**Objective:** Examines the relationship between acceptance rate and Enrollment. Investigate whether the type of HBCUs impacts the acceptance rate and enrollment. Also, explore if significant relationships are prominent.

**Data Source:** A sub-sample of 2018 HBCUs dataframe with 100 observations.
"""
st.markdown(f"<p style='color:{text_color};'>{summary_text}</p>", unsafe_allow_html=True)

# Main Findings
st.markdown(f"<h3 style='color:{subtitle_color};'>Main Findings</h3>", unsafe_allow_html=True)
findings_text = """
First, the model with Enrollment and acceptance rate (discrete variable) has an R square of about 6%, which is significant but negatively associated with Enrollment. The second model with Enrollment and acceptance rate (dummy variable) had an increase in R square (14%) and a positive association between Enrollment and acceptance. This shows an improvement in acceptance rate positively explaining enrollment in HBCUs. Then, we took the natural logarithm of the Enrollment to cater to extreme values and found that the linear regression of acceptance rate (discrete variable) and Enrollment changed from 6% to 11%, and that of acceptance rate (dummy variable, a feature engineered) on Enrollment is about 19%. After adding the type of HBCU into the model, we noted that the R square increased from 19% to about 50%. That acceptance rate and type of HBCU explain about 50% of variations in enrollment. We find that all else equal, if the HBCUs have an acceptance rate less than 90% (a feature engineered), enrollment increases about 80% when compared with HBCUs with an acceptance rate of 90 percent or greater, and the result is significant at a 1% alpha level. If the type of HBCU is public, Enrollment increases about 100% when compared with the private HBCUs. Although this analysis is interesting, we cannot assume causality as many factors that might affect enrollment HBCUs are not just acceptance rate and the Type.
"""
st.markdown(f"<p style='color:{text_color};'>{findings_text}</p>", unsafe_allow_html=True)

# Conclusion
st.markdown(f"<h3 style='color:{subtitle_color};'>Conclusion</h3>", unsafe_allow_html=True)
conclusion_text = """
We can conclude that acceptance and Type of HBCU have a strong association with Enrollment in HBCUs in the US.
"""
st.markdown(f"<p style='color:{text_color};'>{conclusion_text}</p>", unsafe_allow_html=True)



# Function to apply color to text
def color_text(text, color):
    return f'<span style="color:{color}">{text}</span>'

# Define colors
title_color = "#008080"  # Dark cyan
step_color = "#800080"   # Purple

# Data Science Process Steps
st.markdown(color_text('**The Data Science Process**', title_color), unsafe_allow_html=True)

steps = [
    color_text("Step one:", step_color) + " Data Collection—This involves gathering data from various sources, such as databases, APIs, web scraping, or surveys.",
    color_text("Step two:", step_color) + " Data Cleaning—This involves preprocessing the data to ensure that it's accurate, complete, and consistent. This includes tasks such as removing duplicates, filling in missing values, and standardizing the format.",
    color_text("Step three:", step_color) + " Data Exploration—This involves exploring the data to gain a better understanding of its characteristics, such as its distribution, correlation, and outliers.",
    color_text("Step four:", step_color) + " Data Preparation—This involves selecting and transforming the features that will be used in the analysis. This includes tasks such as feature engineering, normalization, and dimensionality reduction.",
    color_text("Step five:", step_color) + " Model Training—This involves selecting the appropriate machine learning model and training it on the data.",
    color_text("Step six:", step_color) + " Model Evaluation—This involves evaluating the performance of the model using various metrics and comparing it to other models.",
    color_text("Step seven:", step_color) + " Model Deployment—This involves deploying the model into a production environment, such as a web application or a database."
]

# Display steps
for step in steps:
    st.markdown(step, unsafe_allow_html=True)

