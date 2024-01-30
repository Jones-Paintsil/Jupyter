# Importing necessary libraries

def app_page_2():

    import streamlit as st
    import numpy as np
    import pandas as pd

    # Create a title for the app
    st.title("My Second Streamlit App")

    # Write some text to the app
    st.write("This is my Second Streamlit app.")

    # Display a DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9], "D": [10,11,12]})
    st.dataframe(df)

    # Create a slider widget
    num_rows = st.slider("Number of rows to display", 1, 5)

    # Display the DataFrame with the selected number of rows
    df = pd.DataFrame(np.random.randint(0, 20, size=(num_rows, 4)), columns=["A", "B", "C", "D"])
    st.dataframe(df)

    # Create a button widget
    if st.button("Are you done?"):
        st.write("You clicked me, so that must mean you are done!")