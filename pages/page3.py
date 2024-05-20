import pandas as pd
import streamlit as st

# Read the CSV sheet
data = pd.read_csv('Sentiment.csv')

# Display title and headers
st.title("Sentiment Analysis")
st.write(data[["text", "sentiment","compound"]].head(10))  # Show only first 10 rows

# Function to display comments with sentiment coloring
def display_sentiment(text, sentiment):
  if sentiment == "positive":
    st.success(text)
  elif sentiment == "negative":
    st.error(text)
  else:
    st.write(text)

# Display first 10 comments with sentiment colorin
