# 📄 PDF Intelligence System (RAG)

A lightweight Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content using an LLM through OpenRouter.

## ✨ Features

 PDF upload and processing
 Automatic text extraction using PyMuPDF
 Document chunking for efficient retrieval
 Context-aware question answering
 Modern dark-themed user interface
 Drag & drop PDF support
 Real-time chat experience
 OpenRouter API integration

## 🖼️ Demo

The application consists of

 Frontend `rag_demo.html`
 Backend `rag_server.py`

Users can

1. Upload a PDF document
2. Process the document into chunks
3. Ask questions about the document
4. Receive answers generated from the most relevant sections

---

## 🏗️ Architecture

```text
PDF Upload
     │
     ▼
Text Extraction (PyMuPDF)
     │
     ▼
Chunking
     │
     ▼
Keyword-Based Retrieval
     │
     ▼
Context Construction
     │
     ▼
OpenRouter LLM
     │
     ▼
Answer Generation
```

---

## 🛠️ Technologies Used

### Backend

 Python
 Flask
 Flask-CORS
 PyMuPDF (fitz)
 OpenAI SDK
 OpenRouter API

### Frontend

 HTML5
 CSS3
 Vanilla JavaScript

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone httpsgithub.comyourusernamepdf-intelligence-system.git
cd pdf-intelligence-system
```

### 2. Install dependencies

```bash
pip install flask flask-cors pymupdf openai
```

### 3. Configure API Key

Replace the OpenRouter API key in

```python
client = OpenAI(
    base_url=httpsopenrouter.aiapiv1,
    api_key=YOUR_API_KEY
)
```

For security, it is recommended to use environment variables instead of hardcoding API keys.

Example

```python
import os

client = OpenAI(
    base_url=httpsopenrouter.aiapiv1,
    api_key=os.getenv(OPENROUTER_API_KEY)
)
```

---

## 🚀 Running the Application

Start the server

```bash
python rag_server.py
```

Open your browser

```text
httplocalhost5000
```

Upload a PDF and start asking questions.

---

## 📁 Project Structure

```text
project
│
├── rag_server.py      # Flask backend
├── rag_demo.html      # Frontend UI
├── README.md
```

---

## ⚙️ How Retrieval Works

The system

1. Extracts text from uploaded PDFs.
2. Splits text into chunks of 500 words.
3. Finds the most relevant chunks using keyword overlap.
4. Builds a context from the top matching chunks.
5. Sends the context and user question to the LLM.
6. Returns the generated answer.

---

## 🔒 Limitations

Current retrieval is based on simple keyword matching.

Potential improvements

 Sentence embeddings
 Vector databases (FAISS, ChromaDB, Pinecone)
 Semantic search
 Hybrid retrieval
 Streaming responses
 Multi-document support

---

## 📈 Future Improvements

 FAISS vector search
 LangChain integration
 Conversation memory
 OCR for scanned PDFs
 Multi-file knowledge base
 User authentication
 Source citations
 Docker deployment

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub.
