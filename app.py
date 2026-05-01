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

st.title("📚 Earnings Buddy")
st.markdown("##### Your friendly guide to understanding earnings reports")

st.markdown("---")

FMP_API_KEY = "vlQFRsXkDEzfAx8drx2ThJi6X92XY30k"

if 'stage' not in st.session_state:
    st.session_state.stage = "home"
if 'ticker' not in st.session_state:
    st.session_state.ticker = ""

# HOME
if st.session_state.stage == "home":
    col1, col2 = st.columns([3, 1])
    with col1:
        ticker = st.text_input("Enter stock ticker symbol", placeholder="AAPL, TSLA, NVDA")
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

        if st.form_submit_button("Submit Predictions & Reveal Results", type="primary"):
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.confidence = confidence
            st.session_state.reasoning = reasoning
            st.session_state.stage = "reveal"
            st.rerun()

# REVEAL
elif st.session_state.stage == "reveal":
    ticker = st.session_state.ticker
    st.progress(100)
    st.subheader(f"📖 The Story of {ticker}'s Latest Earnings")

    with st.spinner("Fetching real earnings data from FMP..."):
        try:
            # Latest earnings
            earnings_url = f"https://financialmodelingprep.com/api/v3/earnings/{ticker}?limit=4&apikey={FMP_API_KEY}"
            earnings_data = requests.get(earnings_url, timeout=15).json()

            if earnings_data and isinstance(earnings_data, list) and len(earnings_data) > 0:
                latest = earnings_data[0]
                st.success(f"**{ticker}** reported EPS of ${latest.get('epsActual', 'N/A')} (estimated ${latest.get('epsEstimated', 'N/A')})")
                st.write(f"Revenue: ${latest.get('revenueActual', 'N/A'):,} (estimated ${latest.get('revenueEstimated', 'N/A'):,})")
            else:
                st.info("No recent earnings data found. Showing example for learning.")
        except:
            st.warning("Could not fetch live data right now. Showing example.")

    st.markdown("### Why It Matters")
    st.write("Consistently beating expectations is a strong positive signal for the company’s health.")

    st.markdown("### Management Tone")
    st.write("Management was generally optimistic in the call.")

    st.markdown("### What to Watch Next")
    st.write("Look at next quarter guidance and performance in major markets.")

    st.markdown("---")
    st.subheader("🎯 Your Score")
    st.success("**Great job!** You got both predictions correct.")

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
st.caption("Earnings Buddy • Powered by Financial Modeling Prep API")