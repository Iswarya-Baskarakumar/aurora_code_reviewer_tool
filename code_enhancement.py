import pandas as pd
import google.generative as genai

GEMINI_API_KEY = 'AIzaSyByLOZAmBso2PXKwA-rt9t0bs3YOBJyxY4'
genai.configure(api_key=GEMINI_API_KEY)

def analyse_code(code):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = f"Review the following python code for best practices, optimices, and potential bugs:\n\n'''python\n{code}\n'''"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
st.title("Automated code review tool")
st.write("This tool uses AI to review your python code for best practices, optimizations, and potential bugs.")

uploaded_file = st.file_uploader("Upload a python file", type=["py"])
code_imput = st.text_area("Or paste your python code here")

if st.button("analyse code"):
    if uploaded_file is not None:
        code = uploaded_file.getvalue().decode("utf-8")
    elif code_input.strip():
        code = code_input
    else:
        st.error("Please upload a file or enter some code")
        st.stop()
        
    st.write("### review results:")
    review_results = analyse_code(code)
    st.write(review_results)            
        
    
        