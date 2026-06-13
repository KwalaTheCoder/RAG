# 📄 Multilingual PDF Intelligence System

A lightweight Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions in multiple languages.

The system automatically detects the language of the user's question and responds in the same language while using the uploaded document as its knowledge source.

---

## ✨ Features

* 📄 PDF Upload & Processing
* 🔍 Retrieval-Augmented Generation (RAG)
* 🌍 Automatic Language Detection
* 🇮🇷 Persian Question Answering
* 🇬🇧 English Question Answering
* 🤖 OpenRouter LLM Integration
* 💬 Modern Chat Interface
* 📁 Drag & Drop PDF Upload
* ⚡ Fast Keyword-Based Retrieval

---

## 🚀 How It Works

1. Upload a PDF document.
2. The system extracts text using PyMuPDF.
3. The document is split into manageable chunks.
4. Relevant chunks are retrieved based on the user's question.
5. The selected context is sent to an LLM through OpenRouter.
6. The model generates an answer using only the document content.
7. The response language automatically matches the user's question language.

---

## 🌐 Multilingual Support

### Persian Example

**Question:**

```text
این سند درباره چیست؟
```

**Response:**

```text
این سند درباره ...
```

### English Example

**Question:**

```text
What is the main topic of this document?
```

**Response:**

```text
The document discusses ...
```

The system automatically detects the language and responds accordingly.

---

## 🏗️ Architecture

```text
PDF
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
Keyword Retrieval
 │
 ▼
Context Building
 │
 ▼
OpenRouter LLM
 │
 ▼
Answer Generation
```

---

## 🛠 Technologies

### Backend

* Python
* Flask
* Flask-CORS
* PyMuPDF
* OpenAI SDK
* OpenRouter API

### Frontend

* HTML
* CSS
* JavaScript

---

## 📦 Installation

```bash
pip install flask flask-cors pymupdf openai
```

---

## 🔑 Environment Variable

Never store your API key directly in the source code.

```bash
OPENROUTER_API_KEY=your_key_here
```

Example:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
```

---

## ▶️ Run

```bash
python rag_server.py
```

Open:

```text
http://localhost:5000
```

---

## ⚠️ Current Limitations

Current retrieval uses keyword matching.

Possible future improvements:

* FAISS Vector Database
* Sentence Transformers Embeddings
* Semantic Search
* Hybrid Search
* OCR Support
* Multi-document Knowledge Base
* Conversation Memory

---

## ⭐ Future Roadmap

* Semantic RAG
* Vector Search
* Source Citations
* Docker Deployment
* Authentication System
* Multi-user Support

---

## License

MIT License
