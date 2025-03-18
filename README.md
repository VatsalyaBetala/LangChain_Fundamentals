# **🚀 LangChain Playground**  
*A personal exploration of LangChain, prompt engineering, and AI-driven workflows*  

## **🧐 Why This Repo Exists**  
This is my **sandbox** for understanding LangChain—not just as a tool, but as a **way of thinking** about how LLMs can be structured, optimized, and deployed effectively.  

LangChain is **more than a framework**—it’s a design philosophy that enables modular and reusable AI workflows. Through this repo, I want to experiment, and rebuild **maybe better**.  

## **🔬 What This Repo Covers**  
This repository isn’t just about one project—it’s going to be a growing collection of **projects, experiments, and learnings** around LangChain:  

- **LLM-powered applications** (e.g., research summarization)  
- **Prompt engineering** (leveraging structured templates for reproducible results)  
- **Embedding models** (using Hugging Face APIs to generate vector representations)  
- **Multi-modal interactions** (text, embeddings, and retrieval-augmented generation)  

Think of this as my living notebook for LangChain. 

## **🛠️ Current Project(s)**  
### 1️⃣ **Research Paper Summarization App**  
- Uses **LangChain + OpenAI** to generate research summaries  
- Supports **multiple explanation styles** (Beginner, Technical, Code-Oriented, Mathematical)  

### 2️⃣ **Hugging Face API for Embeddings**  
- Integrates `sentence-transformers/all-MiniLM-L6-v2` for embeddings  
- Can be extended for **semantic search and knowledge retrieval**  (future scope)

## **📌 The Bigger Picture**  
This repo is more than just code—it’s about **understanding the intersection of LLMs, retrieval, and automation.**  

I'm particularly interested in:  
- How **LLMs and embeddings** work together for **better reasoning**  
- How **memory and context** can be handled efficiently  
- How we can create **LLM-powered agents** that are actually useful  

## **🔮 What’s Next?**  
- 🏗 **More integrations** (custom knowledge retrieval, multi-step reasoning)  
- ⚡ **Efficient caching & vector databases** (e.g., ChromaDB, Pinecone)  

### **⚡ Setup & Running the Project**  
```bash
git clone https://github.com/VatsalyaBetala/langchain-playground.git
cd langchain-playground
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Ensure you have your API keys in `.env`:  
```
OPENAI_API_KEY=your_openai_api_key  
HUGGINGFACEHUB_ACCESS_TOKEN=your_huggingface_api_key  
```

Run the app:  
```bash
streamlit run app.py
```
