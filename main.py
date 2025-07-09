
import streamlit as st

# 🌙 Custom Page Settings
st.set_page_config(
    page_title="SafeTube - Clean Video Search",
    page_icon="🕋",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🎨 Custom Styling
st.markdown(
    """
    <style>
        .reportview-container {
            background-color: #0f0f0f;
            color: #f5f5f5;
        }
        .stTextInput>div>div>input {
            background-color: #1f1f1f;
            color: #f5f5f5;
        }
        .stButton>button {
            background-color: #198754;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌟 Title & Islamic Message
st.title("📺 SafeTube – Ethical Video Search Engine") 
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Bismillah.svg/1280px-Bismillah.svg.png", width=400)
st.markdown("**Guard your eyes and heart.** Allah says in the Quran:")
st.success("**“Indeed, hearing, sight and the heart – all those will be questioned.”** (Surah Al-Isra 17:36)")

# 🔍 Search Box
search_query = st.text_input("🔍 Search YouTube videos:", placeholder="Enter something clean to search...")

# 🧠 Fake Videos Example (will upgrade later)
if search_query:
    st.write("🔎 Searching for videos...")

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
            st.error(f"🚫 Blocked: '{video}' (Unethical Content)")
        else:
            st.success(f"✅ Allowed: '{video}'")

# 🧕 Footer
st.markdown("---")
st.markdown("<center><small>🌸 Built with purpose by **Zarish Johar** | Powered by Python & Faith 🌙</small></center>", unsafe_allow_html=True)

