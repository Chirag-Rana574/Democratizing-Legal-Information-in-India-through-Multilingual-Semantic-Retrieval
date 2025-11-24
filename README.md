# Multilingual-Legal-Information-Retrieval
Democratizing Legal Information in India through Multilingual Semantic Retrieval

A multilingual legal information retrieval system designed to break India’s language barrier in accessing judicial knowledge. The system enables users to query legal case information in 22 Indian languages, retrieves semantically relevant case laws, and returns results translated back into the user’s preferred language.

This project leverages Neural Machine Translation (IndicTrans2), transformer-based semantic embeddings, and vector similarity search (HNSW) to make legal information more accessible to non-English speakers — a crucial step toward democratizing justice in a multilingual nation.

🚀 Motivation

Only 6–10% of Indians speak English, yet English remains the dominant language of the Supreme Court and most High Courts. Legal judgments are dense, long, and filled with complex terminology that even seasoned lawyers find difficult.

This creates a linguistic exclusion for millions of citizens.

Our project aims to eliminate this barrier by allowing users to:

ask legal queries in their native language

retrieve semantically similar legal cases

understand case summaries and titles translated back to their own language

This is not keyword search — it is semantic, cross-lingual retrieval.

🧠 Core Idea

We align legal case documents and multilingual user queries into a single English semantic embedding space, enabling cross-lingual matching.

Pipeline Overview:

User enters a query in any of 22 Indian languages

Query is translated to English using IndicTrans2

Query is encoded into a semantic vector using a Transformer encoder (ONNX Runtime)

Vector similarity search (HNSW) identifies the top legal cases

The titles and summaries are translated back into the user’s language

Results displayed with relevance scores
