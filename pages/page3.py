import pandas as pd
import streamlit as st

# Read the CSV sheet
data = pd.read_csv('Sentiment.csv')

# Display title and headers with clear column renaming
st.title("Sentiment Analysis")
data.rename(columns={"compound": "Sentiment Score"}, inplace=True)
data.rename(columns={"text": "Tweets"}, inplace=True)
data.rename(columns={"sentiment": "Sentiment"}, inplace=True)# Rename in-place
st.write(data[["Tweets", "Sentiment", "Sentiment Score"]].head(10))  # Show first 10 rows

# Function to display comments with sentiment coloring
def display_sentiment(text, sentiment):
    if sentiment == "positive":
        st.success(text)
    elif sentiment == "negative":
        st.error(text)
    else:
        st.write(text)

