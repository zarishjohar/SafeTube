import streamlit as st

st.title("📺 SafeTube – Ethical Video Search Engine")

search_query = st.text_input("🔍 Search YouTube videos:")

if search_query:
    st.write("Searching for videos...")

    videos = [
        "Funny clean motivation video",
        "Hot gossip about celebrities 😳",
        "Peaceful Quran recitation",
        "Insult battle gone wrong!",
        "Islamic reminder on patience"
    ]

    bad_words = ["gossip", "hot", "sexy", "insult", "fight"]

    for video in videos:
        if any(bad_word in video.lower() for bad_word in bad_words):
            st.warning(f"🚫 Blocked: '{video}' (Unethical Content)")
        else:
            st.success(f"✅ Allowed: '{video}'")
