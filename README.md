# DYNAMIC_BOT (Gemini Chatbot)

A modern web-based chatbot powered by Google's Gemini API, built with Flask and vanilla JavaScript.  
**Live Demo:** [https://chat-bot-hx28.onrender.com](https://chat-bot-hx28.onrender.com)

## Features

- Conversational AI using Gemini (Google Generative AI)
- Multi-chat support with chat history and deletion
- Light/Dark theme toggle
- Voice input (speech-to-text)
- Responsive and modern UI

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Set up your Google API Key

- Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- Set it as an environment variable:

```sh
export GOOGLE_API_KEY=your_api_key_here
```

Or, create a `.env` file and use [python-dotenv](https://pypi.org/project/python-dotenv/) (optional).

### 4. Run the app

```sh
python bot.py
```

- Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Deployment

This app is ready to deploy on [Render](https://render.com/):

- The `render.yaml` is pre-configured.
- Set the `GOOGLE_API_KEY` environment variable in your Render dashboard.
- The app will be available at: [https://chat-bot-hx28.onrender.com](https://chat-bot-hx28.onrender.com)

## File Structure

```
bot.py
requirements.txt
render.yaml
key.txt (not used in production)
static/
    index.html
    bot-icon.png
    user-icon.png
```

## Notes

- Do **not** commit your API key to version control.
- For production, set the `GOOGLE_API_KEY` as an environment variable (see `render.yaml`).

## License

MIT License

---

**Live Demo:** [https://chat-bot-hx28.onrender.com](https://chat-bot-hx28.onrender.com)
