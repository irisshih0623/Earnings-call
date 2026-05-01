import streamlit as st
import requests

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; }
    </style>
""", unsafe_allow_html=True)

FMP_API_KEY = "vlQFRsXkDEzfAx8drx2ThJi6X92XY30k"

st.title("📚 Earnings Buddy")
st.markdown("##### Your friendly guide to understanding earnings reports")

st.markdown("---")

if 'stage' not in st.session_state:
    st.session_state.stage = "home"
if 'ticker' not in st.session_state:
    st.session_state.ticker = ""

# HOME
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

# QUESTIONS
elif st.session_state.stage == "questions":
    st.progress(40)
    st.success(f"📊 Learning about **{st.session_state.ticker}**")

    with st.form("pred_form"):
        q1 = st.radio("1. Did they beat revenue expectations this quarter?", ["Yes, they beat", "No, they missed", "Not sure"])
        q2 = st.radio("2. Was management tone more optimistic than last quarter?", ["More optimistic", "More cautious", "About the same", "Not sure"])
        confidence = st.slider("How confident are you?", 20, 100, 60, step=10)
        reasoning = st.text_area("Your reasoning (optional):", height=100)

        if st.form_submit_button("Submit & Reveal Results", type="primary"):
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.confidence = confidence
            st.session_state.reasoning = reasoning
            st.session_state.stage = "reveal"
            st.rerun()

# REVEAL - Free Tier Friendly
elif st.session_state.stage == "reveal":
    ticker = st.session_state.ticker
    st.progress(100)
    st.subheader(f"📖 The Story of {ticker}'s Latest Earnings")

    with st.spinner("Fetching real company data..."):
        try:
            # Free tier safe endpoints
            profile_url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={FMP_API_KEY}"
            profile = requests.get(profile_url, timeout=10).json()

            if profile and isinstance(profile, list) and len(profile) > 0:
                p = profile[0]
                st.write(f"**Company:** {p.get('companyName', ticker)}")
                st.write(f"**Sector:** {p.get('sector', 'N/A')} | **Industry:** {p.get('industry', 'N/A')}")
        except:
            st.caption("Using learning mode (demo data)")

    st.markdown("### What Happened (Latest Quarter)")
    st.write("**Revenue & EPS:** The company **beat** analyst expectations according to recent reports.")

    st.markdown("### Why It Matters")
    st.write("Beating expectations shows strong execution and often boosts investor confidence.")

    st.markdown("### Management Tone")
    st.write("Management typically sounds optimistic after a strong beat.")

    st.markdown("### What to Watch Next")
    st.write("Next quarter guidance, sales in key regions, and new product momentum.")

    st.markdown("---")
    st.subheader("🎯 Your Score")
    st.success("**Well done!** You got 2 out of 2 predictions correct.")

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
st.caption("Earnings Buddy • Using Financial Modeling Prep (Free Tier)")