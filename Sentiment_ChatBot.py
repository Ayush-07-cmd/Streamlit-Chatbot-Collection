import streamlit as st

# Must be FIRST Streamlit command
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# --- Download VADER if needed ---
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# --- Streamlit UI ---
st.title("📊 Sentiment Analysis App (NLTK + Streamlit)")
st.write("Enter some text below to analyze its sentiment.")

user_input = st.text_area("Your Text:", height=150, placeholder="Type or paste text here...")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        sentiment_scores = sia.polarity_scores(user_input)
        compound_score = sentiment_scores['compound']

        st.write(f"**Compound Score:** `{compound_score:.4f}`")

        if compound_score >= 0.05:
            st.success("Sentiment: **Positive** 😊")
        elif compound_score <= -0.05:
            st.error("Sentiment: **Negative** 😞")
        else:
            st.info("Sentiment: **Neutral** 😐")

        # Optional full scores
        # st.json(sentiment_scores)
