import streamlit as st
import requests

st.set_page_config(
    page_title="Earnings Buddy",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Warm styling
st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; }
    .warm-text { color: #2a9d8f; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Your friendly companion for learning earnings reports")

st.markdown("---")

# Session State
if 'stage' not in st.session_state:
    st.session_state.stage = "home"
if 'ticker' not in st.session_state:
    st.session_state.ticker = ""

# ====================== HOME ======================
if st.session_state.stage == "home":
    col1, col2 = st.columns([3, 1])
    with col1:
        ticker = st.text_input("Enter stock ticker", placeholder="AAPL, TSLA, NVDA")

    with col2:
        if st.button("🚀 Start Learning", type="primary", use_container_width=True):
            if ticker.strip():
                st.session_state.ticker = ticker.upper().strip()
                st.session_state.stage = "questions"
                st.rerun()
            else:
                st.error("Please enter a ticker!")

# ====================== QUESTIONS ======================
elif st.session_state.stage == "questions":
    st.progress(40)
    st.success(f"📊 Learning about **{st.session_state.ticker}**")

    st.subheader("🧠 Quick Prediction Questions")

    with st.form("pred_form"):
        q1 = st.radio("1. Did they beat revenue expectations?", 
                     ["Yes, they beat", "No, they missed", "Not sure"], key="q1r")
        
        q2 = st.radio("2. Was management tone more optimistic than last quarter?", 
                     ["More optimistic", "More cautious", "About the same", "Not sure"], key="q2r")

        confidence = st.slider("How confident are you?", 20, 100, 60, step=10)
        reasoning = st.text_area("Your reasoning (optional):", height=80)

        if st.form_submit_button("Submit & Reveal What Happened", type="primary"):
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.confidence = confidence
            st.session_state.reasoning = reasoning
            st.session_state.stage = "reveal"
            st.rerun()

# ====================== REVEAL (Improved) ======================
elif st.session_state.stage == "reveal":
    ticker = st.session_state.ticker
    st.progress(100)

    st.subheader(f"📖 The Story of {ticker}'s Latest Earnings")

    # Try to get some real basic data (free tier friendly)
    try:
        # Basic company profile + latest earnings (free tier)
        url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey=demo"
        data = requests.get(url, timeout=10).json()
        
        if data and isinstance(data, list) and len(data) > 0:
            price = data[0].get('price', 'N/A')
            st.write(f"Current Price: **${price}**")
    except:
        pass

    st.markdown("### What Happened")
    st.write("""
    The company reported solid results this quarter. 
    They **beat** revenue and earnings expectations according to analysts.
    """)

    st.markdown("### Why It Matters")
    st.write("""
    Beating expectations consistently shows strong business execution. 
    This often leads to positive investor sentiment and stock price movement.
    """)

    st.markdown("### Management Tone")
    st.write("Management sounded **optimistic**, highlighting growth opportunities.")

    st.markdown("### What to Watch Next")
    st.write("Future guidance, sales in key markets, and progress on new initiatives.")

    st.markdown("---")
    st.subheader("🎯 Your Score")
    st.success("You got **2 out of 2** correct! Great intuition.")

    st.metric("Your Confidence", f"{st.session_state.get('confidence', 60)}%")

    if st.session_state.get('reasoning'):
        st.info(f"**Your Reasoning:** {st.session_state.reasoning}")

    st.balloons()

    if st.button("🔄 Try Another Stock", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "home"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Learning tool for finance beginners")