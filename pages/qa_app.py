import openai
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Advanced Q&A App", page_icon="💬", layout="wide")

# Title and Description
st.title("GPT Q&A App")
st.markdown("""
    Ask anything, and I will try to give you an insightful answer using AI.
    Enter your question in the input box below and press "Ask".
""")

# Set your OpenAI API key (or load it from an environment variable for production)
openai.api_key = 'something'  # Replace with your actual API key

# Initialize session state to keep track of past questions and answers
if 'questions' not in st.session_state:
    st.session_state.questions = []

# Function to get an answer from GPT-3 based on the user's question
def get_answer_from_gpt3(question):
    try:
        response = openai.completions.create(
            model='gpt-4o-mini',  # You can use "gpt-4" or other models as well
            prompt=question,
            max_tokens=150,  # Adjust the response length
            temperature=0.7,  # Control the randomness of the response
            top_p=1,          # Top-p sampling for creativity
            frequency_penalty=0,  # Control repetitiveness
            presence_penalty=0.6  # Control response diversity
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Input text box for the user to ask a question
question = st.text_input("Ask a question:")

# When the user submits a question
if st.button("Ask"):
    if question:
        # Get an answer from GPT-3 based on the user's question
        answer = get_answer_from_gpt3(question)
        
        # Store the question and its answer in the session state
        st.session_state.questions.append({"question": question, "answer": answer})
        
        # Show the question and the answer on the screen
        st.write(f"**Question:** {question}")
        st.write(f"**Answer:** {answer}")
    else:
        st.warning("Please enter a question before submitting.")

# Show all past questions and answers
if st.session_state.questions:
    st.subheader("Past Questions and Answers:")
    for qa in st.session_state.questions:
        st.write(f"**Q:** {qa['question']}")
        st.write(f"**A:** {qa['answer']}")

# Optionally, allow the user to clear past interactions
if st.button("Clear History"):
    st.session_state.questions = []
    st.rerun()  # Re-run the app to clear the session state
