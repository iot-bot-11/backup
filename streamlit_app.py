
import streamlit as st
import os
from PIL import Image
# Make sure you import the correct library/module for Google Generative AI
import google.generativeai as genai

# Set your Google API key here
API_KEY = "AIzaSyCzDrfg3Zm0Lbczv-YhdhkTy_JcENq5d1I"

# Configure Google API
os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=API_KEY)

# Function to load OpenAI model and get responses
def get_gemini_response(input_text, image, input_prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    if input_text != "":
        response = model.generate_content([input_text, image, input_prompt])
    else:
        response = model.generate_content([image, input_prompt])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="IT'S-MED.Ai")
# Load the image
image = Image.open('scancerlogo.png')
image_resized = image.resize((100, 100))
col1, col2 = st.columns([1, 3])
with col1:
    st.image(image_resized)

    with col2:
        st.title('SCANCER')


# Input prompt
input_text = st.text_input("Specific Doubts: ", key="input")

# File upload
uploaded_file = st.file_uploader("insert scan image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to generate response
submit_button = st.button("Tell me about my condition")
input_prompt1 = """
 Please evaluate the provided image. If it pertains to the medical field, kindly share your professional assessment.
      Otherwise, respond with 'This is not within my expertise.' Thank you!
"""

# If button is clicked
if submit_button:
    if image is not None:
        response = get_gemini_response(input_text, image, input_prompt1)
        st.subheader("Your condition is")
        st.write(response)
        print(response)
    else:
        st.warning("Please upload an image before generating response.")

# Define a function to handle feedback submission
def submit_feedback(feedback):
    # Here, you can implement the logic to store or process the feedback
    st.success("Thank you for your feedback!")



# Feedback button
feedback_button = st.button("Feedback")

# If feedback button is clicked
if feedback_button:
    st.write("Please provide your feedback:")
    feedback_text = st.text_area("Feedback:", height=100)

    st.write("Upload an image (if applicable):")
    feedback_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    submit_feedback_button = st.button("Submit Feedback")
    if submit_feedback_button:
        submit_feedback(feedback_text, feedback_image)
