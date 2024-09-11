from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
app = Flask(__name__)

# Set up your OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate_image', methods=['GET'])
def generate_image():
    prompt = request.args.get('prompt')

    client = OpenAI()
    
    response = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    )

    image_url = response['data'][0]['url']
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
