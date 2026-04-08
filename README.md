# Evaluating Robustness of Large Language Models on Code-Mixed Indian Language Inputs
# 🧠 Evaluating Robustness of LLMs on Code-Mixed Indian Languages

## 📖 Overview
This project evaluates how well Large Language Models (LLMs) like ChatGPT, Gemini, and Perplexity AI handle **code-mixed Indian language inputs** (e.g., Hinglish, Tamil-English, Punjabi-English).

In real-world communication, especially in India, people often mix multiple languages in a single sentence. This research analyzes how such linguistic variations affect model performance.

---

## 🎯 Objective
- Evaluate LLM performance on **code-mixed data**
- Compare results with **monolingual (English) data**
- Measure **accuracy, consistency, and robustness**
- Identify challenges in multilingual NLP systems

---

## 📊 Dataset

### 🔹 Source
- TweetEval Sentiment Dataset (Social Media Data)

### 🔹 Dataset Variants
We created multiple datasets to simulate real-world multilingual usage:

| Dataset Type        | Description |
|--------------------|------------|
| Monolingual        | Pure English text |
| Light Code-Mix     | Low level mixing |
| Medium Code-Mix    | Moderate mixing |
| Heavy Code-Mix     | High mixing |
| Multilingual Mix   | Random multi-language mixing |

### 🔹 Languages Used
- English  
- Hindi  
- Tamil  
- Punjabi  

---

## ⚙️ Methodology

1. **Data Collection**
   - Extracted labeled sentiment data (Positive, Negative, Neutral)

2. **Code-Mixing Generation**
   - Replaced selected English words with Indian language words
   - Used romanized script (real-world typing style)

3. **Model Evaluation**
   - Tested on:
     - ChatGPT
     - Gemini
     - Perplexity AI

4. **Evaluation Metrics**
   - Accuracy
   - Prediction Consistency Rate (PCR)
   - Robustness Degradation Score (RDS)

---

## 📏 Accuracy Calculation
