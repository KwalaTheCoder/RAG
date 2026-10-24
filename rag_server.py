from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
import fitz  # PyMuPDF
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# ذخیره موقت متن PDF
pdf_chunks = []
pdf_name = ""

def extract_and_chunk(pdf_path, chunk_size=500):
    """استخراج متن PDF و تقسیم به chunk"""
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page in doc:
        full_text += page.get_text() + "\n"
    
    doc.close()
    
    # تقسیم به chunk های کوچک
    words = full_text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    
    return chunks, len(full_text.split())

def find_relevant_chunks(question, chunks, top_k=3):
    """پیدا کردن مرتبط‌ترین chunk ها با کلمات کلیدی"""
    question_words = set(question.lower().split())
    scored = []
    
    for i, chunk in enumerate(chunks):
        chunk_words = set(chunk.lower().split())
        score = len(question_words & chunk_words)
        scored.append((score, i, chunk))
    
    scored.sort(reverse=True)
    return [chunk for _, _, chunk in scored[:top_k]]

@app.route('/')
def index():
    return send_from_directory('.', 'rag_demo.html')

@app.route('/upload', methods=['POST'])
def upload():
    global pdf_chunks, pdf_name
    
    if 'file' not in request.files:
        return jsonify({"error": "فایل انتخاب نشده"}), 400
    
    file = request.files['file']
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "فقط PDF قبول میشه"}), 400
    
    # ذخیره موقت
    temp_path = "temp_upload.pdf"
    file.save(temp_path)
    
    try:
        pdf_chunks, word_count = extract_and_chunk(temp_path)
        pdf_name = file.filename
        os.remove(temp_path)
        
        return jsonify({
            "success": True,
            "filename": pdf_name,
            "chunks": len(pdf_chunks),
            "words": word_count
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ask', methods=['POST'])
def ask():
    global pdf_chunks, pdf_name
    
    if not pdf_chunks:
        return jsonify({"error": "اول PDF آپلود کن"}), 400
    
    question = request.json.get('question', '')
    if not question:
        return jsonify({"error": "سوال خالیه"}), 400
    
    # پیدا کردن مرتبط‌ترین بخش‌ها
    relevant = find_relevant_chunks(question, pdf_chunks)
    context = "\n\n---\n\n".join(relevant)
    
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are an expert assistant. Answer questions based ONLY on the provided document context.
If the answer is not in the context, say "This information is not available in the document."
Be concise and accurate.

Document: {pdf_name}

Context:
{context}"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        
        answer = response.choices[0].message.content
        return jsonify({
            "answer": answer,
            "chunks_used": len(relevant)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "pdf_loaded": len(pdf_chunks) > 0,
        "pdf_name": pdf_name,
        "chunks": len(pdf_chunks)
    })

if __name__ == '__main__':
    print("✅ RAG Server started: http://localhost:5000")
    app.run(port=5000, debug=False)
