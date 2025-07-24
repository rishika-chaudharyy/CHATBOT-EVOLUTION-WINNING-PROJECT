# 🧠 Cognizance – Seek, Ask, Understand

Cognizance is a powerful AI-powered image-based query assistant built using **Flask** and **Gemini 1.5 Flash**. It allows users to upload an image and ask questions about it, providing responses tailored to different personas like a doctor, student, or customer service provider. It also includes multilingual support, voice input/output, reminders, and feedback tools.

---

## 🚀 Features

- 🖼️ **Image + Query Based AI Analysis**
- 💬 **Persona-Based Explanation Modes**
  - Doctor, Patient, Student, Teacher, Customer, Customer Support
- 🌐 **Multilingual Support**
  - English, Hindi, Spanish, French
- 🎤 **Speech-to-Text Input**
- 🔊 **Text-to-Speech Output with Voice Selection**
- ⏰ **Medicine Reminder Functionality**
- 📥 **Downloadable AI Responses**
- 📝 **Response Summarization**
- 👍👎 **Feedback Rating System**
- 🧠 **Quiz Generation (Coming Soon)**

---

## 📂 Project Structure

📁 your-project/
├── app.py # Flask backend
├── .env # Store your Gemini API key
├── templates/
│ └── index.html # Frontend HTML page
├── static/ # (Optional) For CSS/JS/images if separated
└── README.md # This file



---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cognizance-app.git
cd cognizance-app
2. Create a .env file

GEMINI_API_KEY=your_google_generative_ai_key
🔑 Get your Gemini API key from Google AI Studio

3. Install dependencies
Make sure you have Python 3.7+ and pip installed.


pip install -r requirements.txt
If requirements.txt is not provided, install manually:


pip install Flask google-generativeai python-dotenv Pillow
4. Run the application

python app.py
Visit http://127.0.0.1:5000/ in your browser

📸 Usage
Upload an image (e.g., X-ray, document, chart)

Choose an explanation mode (optional)

Enter or speak your query

Get contextual AI-generated responses

Download or listen to the response, or set reminders

📦 Dependencies
Flask

Google Generative AI Python SDK

Pillow

dotenv

📌 To-Do
 Add quiz generation using Gemini

 Save chat history with local/session storage

 Add image comparison tool

 Deploy on Render/Heroku

🤝 Contributing
Pull requests and feature suggestions are welcome! Please fork this repo and submit a PR.

📜 License
This project is open-source under the MIT License.

🌟 Acknowledgements
Powered by Google Gemini

Designed with ❤️ using HTML, JS, and Flask

