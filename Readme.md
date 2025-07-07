# 📰 Fake News Detection — BERT-based Classification with Streamlit

👉 **[🔗 Live Demo](https://your-project-link-here.com](https://fakenewsdetection-9ix5r3mbvwd9vakvdh6j3f.streamlit.app/)**  
*(Click to try the app online — replace with your actual link)*

---

This project focuses on building a robust **fake news detection system** using the **BERT (Bidirectional Encoder Representations from Transformers)** model. We initially explored traditional machine learning approaches, then moved to BERT to incorporate **contextual understanding** of language — significantly improving performance.

🔗 Dataset used: [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## 🧠 Why BERT?

Traditional ML methods rely on frequency-based features and often ignore context. BERT, however, understands the meaning of words based on their surrounding context, making it a powerful tool for detecting misinformation or misleading headlines.

We fine-tuned the **`bert-base-uncased`** model using Hugging Face Transformers, achieving:

> ✅ **F1 Score: 99.98% on validation data**

This result demonstrates the strong capability of BERT in handling subtle linguistic cues in real vs fake news articles.

---

## 🚀 Streamlit Interface

To make the model interactive, we built a lightweight Streamlit web application.

### Features:
- Paste a news article or headline
- Click **Predict**
- Instantly get a result:
  - ✅ **Real News**
  - ❌ **Fake News**

---

## 📁 Project Structure

