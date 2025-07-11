# 🌐 Translation Microservice

A lightweight, modular RESTful translation microservice built using **FastAPI** and **Googletrans**. It accepts text input, translates it to a target language using ISO codes, and returns the translated output via a clean API.

---

## 📦 Features

- 🔤 Translate text using `googletrans`
- 🌍 Supports ISO 639-1 language codes (e.g., `hi`, `ta`, `fr`, `es`)
- 🧪 Input validation (max 1000 characters)
- 🧾 Bulk translation support
- 🗃️ Logs all translation requests in SQLite
- ❤️ `/health` endpoint for health checks
- 🧩 Modular folder structure (routes, services, utils)

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AmrutaJayanti/Translation-Microservice.git
cd Translation-Microservice
```

### 2. Create a virtual environment

```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

