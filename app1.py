import streamlit as st
import pandas as pd
import numpy as np

st.title('My First Streamlit App')

st.write('Hello, welcome to my first Streamlit app!')

# Create a simple dataframe
data = pd.DataFrame({
    'Column 1': np.random.randn(50),
    'Column 2': np.random.randn(50)
})

# Display the dataframe
st.write('Here is a sample dataframe:')
st.dataframe(data)

# Plot a chart
st.line_chart(data)

st.write('Thank you for visiting!')

