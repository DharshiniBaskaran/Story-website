import os
from flask import Blueprint, render_template, request, send_file
import google.generativeai as genai
from google.cloud import texttospeech

main = Blueprint('main', __name__)

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("AIzaSyAio6jQiSMMEcZwAmAvRInuI0OBNNusWmQ"))

# Configure Google Cloud Text-to-Speech
tts_client = texttospeech.TextToSpeechClient()

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Generate story using Generative AI API
        story = generate_story(user_input)
        
        # Convert the story to audio
        audio_file = generate_audio(story)
        
        return render_template('index.html', story=story, audio_file=audio_file)
    
    return render_template('index.html')

def generate_story(prompt):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="Generate an engaging and coherent story based on the given prompt.",
    )
    
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
    response = chat_session.send_message(prompt)
    
    return response.text

def generate_audio(text):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    # Save the audio file
    audio_file_path = "static/story_audio.mp3"
    with open(audio_file_path, "wb") as out:
        out.write(response.audio_content)
    
    return audio_file_path
