# Loading the packages
import re
import pandas as pd
import streamlit as st

def data_cc():
    st.title("Data Collection and Cleaning")
    
    # Data Collection
    # Importing the data
    hbcus_1 = pd.read_csv('hbcus_2018.csv')
    
    # Display first 5 rows of the dataset
    st.subheader("First 5 rows of the dataset:")
    st.write(hbcus_1.head())
    
    # Data cleaning
    
    # Determine the total number of columns in the data
    names = hbcus_1.columns
    st.subheader("Column names:")
    st.write(names)
    
    # Get the total number of observations
    total_obs = hbcus_1.shape[0]
    st.subheader("Total number of observations:")
    st.write(f"The total number of observations in the dataset is {total_obs}")
    
    # Check for missing values
    st.subheader("Missing values:")
    st.write(hbcus_1.isnull().sum())
    
    # Drop missing values
    hbcus_2 = hbcus_1.dropna()
    null_check = hbcus_2.isnull().sum()
    total_obs_check = hbcus_2.shape[0]
    
    st.subheader("After dropping missing values:")
    st.write(null_check)
    st.write(f"Checking the total number of observations after dropping missing values: {total_obs_check}")

# Call the function to run the Streamlit app
if __name__ == "__main__":
    data_cc()

