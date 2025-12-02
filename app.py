# Recreate the corrected version of `app.py` after the environment reset

app_code = """
import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/ICE_Chicago_REAL_dataset.csv")

df = load_data()

# Sidebar filters
emotion_filter = st.sidebar.multiselect("Filter by Emotion", sorted(df["Emotion"].dropna().unique()))
theme_filter = st.sidebar.multiselect("Filter by Theme", sorted(df["Theme"].dropna().unique()))
source_filter = st.sidebar.multiselect("Filter by Source", sorted(df["Source"].dropna().unique()))

filtered_df = df.copy()
if emotion_filter:
    filtered_df = filtered_df[filtered_df["Emotion"].isin(emotion_filter)]
if theme_filter:
    filtered_df = filtered_df[filtered_df["Theme"].isin(theme_filter)]
if source_filter:
    filtered_df = filtered_df[filtered_df["Source"].isin(source_filter)]

# Main dashboard
st.title("Witness Archive: ICE Raids in Chicago")
st.markdown("Explore public testimonies and news narratives tagged by emotion and theme.")

for _, row in filtered_df.iterrows():
    title = row.get("Title", "No Title")
    source = row.get("Source", "Unknown Source")
    date = row.get("Publication Date", "Unknown Date")
    excerpt = row.get("Text Excerpt", "")
    url = row.get("URL", "#")

    st.markdown(f"**{title}** ({source}, {date})  \n[Read More]({url})")
    st.write(excerpt)
    st.markdown("---")
"""

# Save the corrected code to app.py
app_path = "/mnt/data/app.py"
with open(app_path, "w") as f:
    f.write(app_code)

app_path
