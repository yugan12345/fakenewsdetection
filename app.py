import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model and tokenizer from local saved directory
@st.cache_resource
def load_model():
    tokenizer = BertTokenizer.from_pretrained("saved_model")  # Path to your folder
    model = BertForSequenceClassification.from_pretrained("saved_model")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

st.title("📰 Fake News Detector (BERT)")

user_input = st.text_area("Enter a news article to classify:")

if st.button("Predict"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        # Tokenize and convert to tensor
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=1).item()

        label = "✅ Real News" if prediction == 1 else "❌ Fake News"
        st.subheader(f"Prediction: {label}")
