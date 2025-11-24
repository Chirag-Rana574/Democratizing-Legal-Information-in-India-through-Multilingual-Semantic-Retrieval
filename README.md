🎯 Democratizing Legal Information in India through Multilingual Semantic Retrieval

A cross-lingual, transformer-powered legal search engine for 22 Indian languages.










📑 Table of Contents

Overview

Motivation

Core Idea

System Architecture

Dataset

Results

Technologies Used

Future Scope

Citation

Contact

🚀 Overview

India is home to 1.4B people speaking hundreds of languages, yet English dominates court judgments.
This project enables:

Queries in 22 Indian languages

Semantic (not keyword) retrieval

Translated, readable case summaries

Accurate embeddings + vector search

A step toward justice accessibility and linguistic equality.

🌍 Motivation

Only 6–10% of Indians speak English, yet legal information is almost entirely in it.
This creates:

Linguistic inequality

Barriers for rural users

Lack of access to case laws

Our system returns legal case information in the user’s native language.

🧠 Core Idea

All queries and documents are aligned in a shared English semantic embedding space.

Workflow:

Query in any language

Translate to English (IndicTrans2)

Generate embedding

HNSW vector search

Retrieve top cases

Translate results back

🏗️ System Architecture
User Query (Any Indic Language)
        |
        v
IndicTrans2 (Indic → English)
        |
        v
Transformer Encoder (Semantic Embedding)
        |
        v
HNSW Vector Search
        |
        v
Top Retrieved Cases
        |
        v
IndicTrans2 (English → Indic)
        |
        v
Final Output to User

📚 Dataset
📘 LeSICiN (Primary Corpus)

42,835 Indian legal cases

JSONL structured format

Includes facts, reasoning, citations

📝 Evaluation Dataset

100 multilingual queries

22 languages

Each annotated with top-3 relevant cases

📊 Results
Metric	K=1	K=3	K=5
Precision@K	0.9833	0.5222	0.3133
Recall@K	0.0983	0.2567	0.4567
NDCG@K	0.9833	0.6203	0.4483

Highlights

98.33% Precision@1

Outperforms BM25

Strong cross-lingual performance

🛠️ Technologies Used

IndicTrans2

Transformer Encoder (ONNX Runtime)

HNSWlib

Python

JSONL

🔮 Future Scope

Multilingual RAG-based legal QA

Expand to Supreme Court + all High Courts

Voice-based query support

Expert-led relevance assessment

Public legal aid platform

📄 Citation
Bangwal, A., Gusain, A., Rana, C., Sharma, N., & Kumar, R. 
“Democratizing Legal Information in India through Multilingual Semantic Retrieval,” 2025.

📬 Contact

Ashish Bangwal — ashish.04014811622@aiml.mait.ac.in

Anubhav Gusain — anubhav.20314811622@aiml.mait.ac.in

Chirag Rana — chirag.35514811622@aiml.mait.ac.in

Neelam Sharma — neelamsharma@mait.ac.in

Rajat Kumar — rajat.05214811622@aiml.mait.ac.in
