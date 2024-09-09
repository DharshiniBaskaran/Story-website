from PIL import Image

def generate_image_story(image_path):
    # Dummy implementation: Describe the image
    img = Image.open(image_path)
    description = f"The image has dimensions {img.size} and mode {img.mode}."
    
    # You can integrate an AI model here to generate a more detailed story.
    story = f"This is an AI-generated story based on the image: {description}"
    return story
