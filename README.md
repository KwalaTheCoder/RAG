# Multilingual PDF RAG

A lightweight Flask application for asking Persian or English questions about an uploaded PDF. It extracts document text, retrieves relevant chunks, and uses an OpenRouter-hosted language model to compose an answer.

## Features

- Drag-and-drop PDF upload
- PyMuPDF text extraction
- Lightweight keyword retrieval
- Persian and English question answering
- Responsive HTML/CSS/JavaScript chat interface

## Run locally

```bash
python -m venv .venv
pip install flask flask-cors pymupdf openai
```

Configure your API key outside the repository:

```bash
# PowerShell
$env:OPENROUTER_API_KEY="your-key"

# macOS/Linux
export OPENROUTER_API_KEY="your-key"
```

Start the server and open `http://127.0.0.1:5000`:

```bash
python rag_server.py
```

## Architecture

`PDF → text extraction → chunking → keyword retrieval → context → LLM answer`

## Limitations

Retrieval is lexical rather than semantic, uploaded content is held for the current process, and generated answers can be inaccurate. Do not upload sensitive documents to an untrusted deployment.
