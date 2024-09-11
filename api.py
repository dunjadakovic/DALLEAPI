from flask import Flask, request, jsonify
import openai
import os
app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.json['prompt']
    response = openai.Image.create(prompt=prompt, n=1, size="256x256")
    image_url = response['data'][0]['url']
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
