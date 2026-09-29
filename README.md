# 🎓 AI Study Assistant

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF study materials and ask questions based on their own documents.

Instead of relying on general knowledge, the application retrieves the most relevant information from the uploaded documents using **semantic search** and generates context-aware answers with a **Large Language Model (LLM)**.

---

## ✨ Features

* 📄 Upload PDF study materials
* 📚 Store multiple document collections
* 🗑️ Delete uploaded collections
* 📋 View available collections
* 💬 Chat with your uploaded documents
* 🔍 Semantic Search using ChromaDB
* 🤖 AI-generated answers using Groq LLM
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ Interactive Streamlit interface

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / Machine Learning

* LangChain
* HuggingFace Embeddings
* Sentence Transformers
* Groq API

### Vector Database

* ChromaDB

### PDF Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

---

## ⚙️ How It Works

```text
               Upload PDF
                    │
                    ▼
            PyPDFLoader
                    │
                    ▼
      RecursiveCharacterTextSplitter
                    │
                    ▼
      HuggingFace Embeddings
                    │
                    ▼
               ChromaDB
                    │
                    ▼
        Semantic Retrieval (Top-K)
                    │
                    ▼
            LangChain Prompt
                    │
                    ▼
              Groq LLM
                    │
                    ▼
             AI Generated Answer
```

---

## 📁 Project Structure

```text
student-assistance-system/
│
├── src/
│   ├── app/
│   │   ├── main.py
│   │   ├── home.py
│   │   ├── doc.py
│   │   ├── chat.py
│   │   
│   │
│   ├── QA.py
│   ├── langchain_manager.py
│   ├── DATA/
│   └── .env
│
├── requirements.txt
└── README.md
```

---

## 🚀 Workflow

### 1. Upload PDF

Users upload one or more PDF study materials.

---

### 2. Text Processing

The uploaded PDF is loaded using **PyPDFLoader** and split into smaller chunks using **RecursiveCharacterTextSplitter**.

---

### 3. Embedding Generation

Each chunk is converted into vector embeddings using:

* sentence-transformers/all-MiniLM-L6-v2

---

### 4. Vector Storage

The embeddings are stored inside **ChromaDB** as a collection.

---

### 5. User Query

The user selects a document collection and asks a question.

---

### 6. Semantic Search

ChromaDB retrieves the **Top-K** most relevant chunks based on semantic similarity.

---

### 7. Response Generation

The retrieved context is passed to the **Groq LLM** through LangChain.

The model generates an answer **grounded only in the uploaded document**.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Study-Assistant.git
```

Go to the project folder

```bash
cd AI-Study-Assistant
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the **src** directory.

add your groq api

---

## ▶️ Run the Application

```bash
streamlit run src/app/main.py
```

## 🔮 Upcoming Features

* 🔐 User Authentication
* 📄 DOCX Support
* 📊 PPTX Support
* 🖼️ OCR for Images
* 📝 Notes Summarizer
* 🧠 Flashcard Generator
* ❓ Quiz Generator
* 🗂️ Conversation History
* 🎤 Voice Input
* 📥 Export Chat

---

## 📚 Concepts Used

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embeddings
* Chunking
* Prompt Engineering
* Large Language Models (LLMs)

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📧 Contact

**GitHub**

[https://github.com/Panwithaging]

**LinkedIn**

[https://www.linkedin.com/in/pangingtushar54/]

**Email**

[pangingtushar54@gmail.com]

---

