🎯 Democratizing Legal Information in India through Multilingual Semantic Retrieval

A cross-lingual, transformer-powered legal search engine for 22 Indian languages.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/NLP-Transformers-purple?style=for-the-badge" /> <img src="https://img.shields.io/badge/Model-IndicTrans2-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/Vector%20Search-HNSW-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" /> </p>
📑 Table of Contents

🚀 Overview

🌍 Motivation

🧠 Core Idea

🏗️ System Architecture

📚 Dataset

📊 Results

🛠️ Technologies Used

🔮 Future Scope

📄 Citation

📬 Contact

🚀 Overview

India is home to 1.4 billion people speaking hundreds of languages, yet English dominates the Supreme Court & High Court judgments — making legal information inaccessible to over 90% of citizens.

This project presents a Multilingual Semantic Legal Retrieval System that:

✔️ Accepts queries in 22 Indian languages
✔️ Performs semantic (not keyword-based) case retrieval
✔️ Returns case titles & summaries translated back into the user's language
✔️ Uses transformer-based embeddings + vector search for accuracy

A step toward justice accessibility and linguistic inclusivity.

🌍 Motivation

Only 6–10% of Indians speak English, but legal proceedings rely heavily on complex English terminology. This creates:

❌ Linguistic inequality
❌ Lack of accessibility to legal knowledge
❌ Barriers for rural communities
❌ Limited awareness of rights & precedents

Our system breaks this barrier by enabling citizens to access legal case information in their native language, without English proficiency.

🧠 Core Idea

We align all languages into a shared English embedding space so that queries in any language find semantically relevant legal cases.

🔄 Multilingual Retrieval Pipeline

User enters query (Hindi/Bengali/Tamil/etc.)

IndicTrans2 translates query → English

Transformer encoder generates embeddings

HNSW vector search finds similar legal cases

Retrieved results translated back → user language

User receives readable, understandable output

🏗️ System Architecture
flowchart TD
    A[User Query in Any Indian Language] --> B[IndicTrans2<br>Indic → English]
    B --> C[Semantic Embedding<br>Transformer Encoder (ONNX)]
    C --> D[Vector Search Engine<br>HNSWlib]
    D --> E[Top-k Case Retrieval]
    E --> F[IndicTrans2<br>English → Indic]
    F --> G[Output Case Titles, Summaries & Scores in User Language]

📚 Dataset
📘 Primary Dataset: LeSICiN

42,835 legal case documents

JSONL format

Includes facts, reasoning, citations, etc.

Used for embedding generation

📝 Evaluation Dataset

100 multilingual queries

22 Indian languages

Each query annotated with 3 relevant cases

Designed to test cross-lingual semantic retrieval

📊 Results
Metric	K=1	K=3	K=5
Precision@K	⭐ 0.9833	0.5222	0.3133
Recall@K	0.0983	0.2567	0.4567
NDCG@K	⭐ 0.9833	0.6203	0.4483
🌟 Key Insights

98.33% Precision@1 → First result is almost always correct

Outperforms BM25 by 15–20%

Maintains high semantic accuracy across languages

Captures legal meaning beyond keywords

🛠️ Technologies Used

IndicTrans2 – multilingual translation

Sentence-Transformers (ONNX Runtime) – embedding generation

HNSWlib – high-speed vector similarity search

Python – pipelines, preprocessing, evaluation

JSONL – dataset format
