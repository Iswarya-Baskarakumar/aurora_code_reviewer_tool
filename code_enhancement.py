import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
GEMINI_API_KEY = "AIzaSyByLOZAmBso2PXKwA-rt9t0bs3YOBJyxY4"
genai.configure(api_key=GEMINI_API_KEY)

# Function to analyze code using Gemini API
def analyze_code(code):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = f"Review the following code for best practices, optimizations, and potential bugs:\n\n```\n{code}\n```"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AURORA Code Review Tool")
st.write("Analyze your code for best practices and optimization.")

# Upload or paste code
uploaded_file = st.file_uploader("Upload a file (any format)", type=None)
code_input = st.text_area("Or paste your code here:")

if st.button("Analyze Code"):
    if uploaded_file is not None:
        try:
            code = uploaded_file.read().decode("utf-8")
        except UnicodeDecodeError:
            st.error("Unable to read file. Please upload a text-based file.")
            st.stop()
    elif code_input.strip():
        code = code_input
    else:
        st.error("Please upload a file or enter code.")
        st.stop()

    # Run analysis
    st.write("### Review Results:")
    review_results = analyze_code(code)
    st.write(review_results)
