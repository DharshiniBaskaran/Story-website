import streamlit as st
from backend.text_generation import generate_text_story
from backend.image_processing import generate_image_story
from backend.video_processing import generate_video_story

st.title("Looney Tunes")

st.write("Upload a text prompt, image, or video to generate a story.")

# Text-based story generation
st.header("Text Story")
prompt = st.text_area("Enter a story prompt:")
if st.button("Generate Text Story"):
    if prompt:
        story = generate_text_story(prompt)
        st.write("### Generated Story")
        st.write(story)
    else:
        st.write("Please enter a prompt.")

# Image-based story generation
st.header("Image Story")
uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
if st.button("Generate Image Story"):
    if uploaded_image:
        story = generate_image_story(uploaded_image)
        st.write("### Generated Story")
        st.write(story)
    else:
        st.write("Please upload an image.")

# Video-based story generation
st.header("Video Story")
uploaded_video = st.file_uploader("Upload a video:", type=["mp4", "mov", "avi"])
if st.button("Generate Video Story"):
    if uploaded_video:
        story = generate_video_story(uploaded_video)
        st.write("### Generated Story")
        st.write(story)
    else:
        st.write("Please upload a video.")
