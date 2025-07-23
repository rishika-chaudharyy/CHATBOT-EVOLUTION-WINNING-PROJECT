from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import tempfile
import google.generativeai as genai


app = Flask(__name__)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/upload', methods=['POST'])
def upload_image_and_query():
    image_file = request.files.get('image')
    query = request.form.get('query')

    print("[INFO] Received image and query")

    if not image_file or not query:
        print("[ERROR] Missing image or query")
        return jsonify({'error': 'Both image and query are required.'}), 400

    try:
        
        import io
        from PIL import Image
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        jpeg_bytes = buffer.getvalue()

        print("[INFO] Sending to Gemini...")

        response = model.generate_content([
            query,
            {
                "mime_type": "image/jpeg",
                "data": jpeg_bytes
            }
        ])

        print("[SUCCESS] Gemini response:", response.text)
        return jsonify({"response": response.text})

    except Exception as e:
        import traceback
        print("[ERROR] Exception occurred:")
        traceback.print_exc()  
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
