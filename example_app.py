import streamlit as st
import numpy as np
import pandas as pd

# Title of the app
st.title('Simple Streamlit App')

# Text input from the user
user_input = st.text_input('Enter a name:', 'John Doe')

# Display the user's input
st.write(f'Hello, {user_input}! Welcome to this Streamlit app.')

# Slider input for selecting a number
num = st.slider('Select a number', 0, 100, 25)

# Generate some data based on the number
x = np.linspace(0, 10, 100)
y = np.sin(x) * num

# Display a line chart
st.line_chart(pd.DataFrame({'x': x, 'y': y}))

# Display a dataframe of the data
st.write(pd.DataFrame({'x': x, 'y': y}))
