# 🔍 Fake News Classifier (Political Text)  
**[Live Demo → Click here](https://your-username-your-repo-name.streamlit.app/)**

This project aims to **classify political news articles as real or fake** based on their textual content.

---

## 🧠 Project Overview

We explored the problem of fake news detection using both traditional and modern Natural Language Processing (NLP) techniques.

---

## 📌 Phase 1: Classical Machine Learning Approach

Initially, we used classical machine learning models by performing the following preprocessing and feature engineering steps:

- **Tokenization**
- **Lemmatization**
- **Stemming**
- **TF-IDF Vectorization**

We trained multiple classifiers on this preprocessed text:

- 🔹 Support Vector Machines (SVM)  
- 🔹 Logistic Regression  
- 🔹 Naive Bayes  
- 🔹 Random Forest

Despite some initial success, these models **struggled with context understanding**, especially for nuanced or long-form political paragraphs.

---

## 🔁 Why Classical ML Didn't Work Well

Classical methods treat each word as independent and lack **contextual embeddings**. They fail to capture the **semantic meaning** of phrases like "fake news" vs. "allegedly fake news" in different political contexts.

---

## 🚀 Phase 2: BERT-Based Classification

To overcome these limitations, we used **BERT (Bidirectional Encoder Representations from Transformers)** — a transformer-based model that understands contextual relationships between words.

- 📦 **Dataset**: 100 MB of labeled text (~40,000+ long political paragraphs)
- 📊 **Model**: `BertForSequenceClassification`
- 🎯 **Accuracy**: Achieved **99.98%** on validation

---

## 🌐 Deployment

We deployed the trained BERT model using **Streamlit**, a lightweight web framework for ML applications.

Try it yourself here:  
👉 **[Live Streamlit App](https://your-username-your-repo-name.streamlit.app/)**

---

## 📁 Repo Structure

