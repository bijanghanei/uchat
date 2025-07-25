# 🧠 AI Telegram Bot (Fully Dockerized, Offline, Open Source)

This project is a **AI chatbot** that runs:

* A Telegram bot interface
* An open-source LLM (like **llama3** or **LLaMA**)
* Everything inside Docker — **no host installation required**

---

## 🚀 Features

* ✅ **No OpenAI API** – runs local LLMs (GGUF format)
* ✅ **No installation on your machine**
* ✅ **Free & open-source**
* ✅ **Offline, private**
* ✅ Powered by [`Ollama`] + Telegram

---

## 🧱 Project Structure

```
├── bot/
│   └── main.py             # Telegram bot logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # For the bot
└── docker-compose.yml      # Runs both bot and model
```

---

## 🔧 Setup Instructions

### 1. Clone this repo

```bash
git https://github.com/bijanghanei/uchat.git
cd uchat
```

### 2. Get a `llama3` model

```bash
curl -X POST http://localhost:11434/pull \
  -H "Content-Type: application/json" \
  -d '{"name": "llama3"}'
```

---

### 3. Add your Telegram bot token

Edit the `docker-compose.yml` and replace this line:

```yaml
TELEGRAM_BOT_TOKEN: your_telegram_token_here
```

You can get a token from [@BotFather](https://t.me/BotFather) on Telegram.

---

### 4. Run everything with Docker 🐳

```bash
docker compose up --d
```

* LLM model server starts on port 11434
* Telegram bot connects and replies using the model
* Messages are sent through the Telegram Bot API

---

### 5. Talk to your bot

Find your bot in Telegram (via @BotFather) and say:

```
/start
hi
who are you?
explain quantum physics in simple terms
```

---

## 🔍 Testing the LLM API (Optional)

```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3","prompt": "Hi","stream": false}'
```

---

## 📆 Tech Stack

| Component     | Tool                                                                                |
| ------------- | ----------------------------------------------------------------------------------- |
| LLM Inference | Ollama (via Docker)                                                                 |
| Bot Framework | [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) |
| Container     | Docker, docker-compose                                                              |

---

## 🧠 Tips

* You can swap in other models like `llama2`, `mistral`, `gemma`, etc.
* To change model file name: update `docker-compose.yml` and `command:` section

---

## 📜 License

MIT — use freely, modify proudly.
