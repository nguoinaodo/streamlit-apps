import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Streamlit App Store", page_icon=":guardsman:", layout='centered')

# Sidebar for navigation (optional)
# st.sidebar.title("Streamlit App Store")
# st.sidebar.markdown("""
#     Select an app from the grid below to explore.
# """)

# Main Page: App Store Overview
st.title("Welcome to the Local Streamlit App Store!")
st.markdown("""
Explore a collection of local Streamlit apps running on your machine. 
Click on an app in the grid to explore more details and access the app.
""")

# Grid Layout for Apps
col1, col2, col3 = st.columns(3)

# # App 1: Data Visualizer
# with col1:
#     st.image("https://via.placeholder.com/150")  # Replace with your app's image
#     st.subheader("Data Visualizer")
#     st.write("Visualize data in interactive formats.")
#     st.page_link("Go to Data Visualizer", page="data_visualizer")  # Link to the Data Visualizer app

# # App 2: Sentiment Analyzer
# with col2:
#     st.image("https://via.placeholder.com/150")  # Replace with your app's image
#     st.subheader("Sentiment Analyzer")
#     st.write("Analyze sentiment from text input using NLP models.")
#     st.page_link("Go to Sentiment Analyzer", page="sentiment_analyzer")  # Link to the Sentiment Analyzer app

# # App 3: Machine Learning Model
# with col3:
#     st.image("https://via.placeholder.com/150")  # Replace with your app's image
#     st.subheader("ML Model")
#     st.write("Demo of an interactive machine learning model.")
#     st.page_link("Go to ML Model", page="ml_model")  # Link to the ML Model app

# App 1: Sudoku Solver
with col1:
    st.image("https://via.placeholder.com/150")  # Replace with your app's image
    st.subheader("Sudoku solver")
    st.page_link(page="pages/sudoku_app.py", label="Go to app", icon="🚨")

# App 2: Example app
with col2:
    st.image("https://via.placeholder.com/150")  # Replace with your app's image
    st.subheader("Example app")
    st.page_link(page="pages/example_app.py", label="Go to app", icon="🚨")

# App 3: Q&A app
with col3:
    st.image("https://via.placeholder.com/150")  # Replace with your app's image
    st.subheader("Q&A app")
    st.page_link(page="pages/qa_app.py", label="Go to app", icon="🚨")


# Footer
st.markdown("""
---
Created with ❤️ by [Bui Hoang Luu](https://your-portfolio.com)
""")
