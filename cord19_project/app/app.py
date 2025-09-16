import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers metadata")

@st.cache_data
def load_data():
    return pd.read_csv('../data/metadata.csv')

try:
    df = load_data()
    st.write("Dataset loaded successfully!", df.head())
    
    # Year filter
    df['year'] = pd.to_datetime(df['publish_time'], errors='coerce').dt.year
    year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
    filtered = df[df['year'].between(year_range[0], year_range[1])]
    
    st.subheader("Publications per Year")
    year_counts = filtered['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    year_counts.plot(kind='bar', ax=ax)
    st.pyplot(fig)
    
    st.subheader("Top Journals")
    top_journals = filtered['journal'].value_counts().head(10)
    st.bar_chart(top_journals)
    
    st.subheader("Word Cloud of Titles")
    text = " ".join(filtered['title'].dropna().astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400).generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
    
except Exception as e:
    st.error(f"Error loading data: {e}")
