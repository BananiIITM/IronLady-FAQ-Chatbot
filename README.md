# Iron Lady FAQ Chatbot 🤖  

A chatbot designed to answer frequently asked questions about the **Iron Lady** initiative.  
Built with **Python** and conversational AI techniques, this project helps users interact seamlessly and get instant answers.  

---

## 🚀 Features
- AI-powered FAQ answering system  
- Easy-to-use conversational interface  
- Modular design for adding new questions & answers  
- Built using Python and NLP libraries  

---

## 🛠️ Tech Stack
- **Python 3.x**  
- **Streamlit** (for web interface)
- **OpenAI API** (for AI-powered responses)
- **difflib** (for FAQ matching)
- **python-dotenv** (for environment variables)

---

## 📂 Project Structure
```
├── app.py              # Main application file
├── faqs.json          # JSON file containing FAQ data
├── requirements.txt   # Project dependencies
├── LICENSE           # License information
└── README.md         # Project documentation
```

---

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/BananiIITM/IronLady-FAQ-Chatbot.git
cd IronLady-FAQ-Chatbot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

1. Set up your OpenAI API key (optional, for AI fallback responses):
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

2. Start the Streamlit app:
```bash
streamlit run app.py
```

3. Your default web browser will open automatically with the chatbot interface.

4. Type your questions in the text input field and click "Send" to get answers:
   - The chatbot will first try to match your question with the FAQ database
   - If no good match is found and OpenAI API key is configured, it will use AI to generate a response
   - Otherwise, it will indicate that it doesn't know the answer

## 📝 Example Questions

The chatbot can answer questions like:
- What programs does Iron Lady offer?
- How long do the programs last?
- Are the sessions online or in-person?
- Do I get a certificate?
- Who are the program mentors?

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📋 Requirements

- Python 3.7 or higher
- OpenAI API key (optional, for AI-powered responses)
- Internet connection (for OpenAI API calls when using AI fallback)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2025 Banani Mallick
