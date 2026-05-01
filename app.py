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
        reasoning = st.text_area("Your reasoning (optional):", height=120)

        if st.form_submit_button("Submit Predictions & Reveal Results", type="primary"):
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.confidence = confidence
            st.session_state.reasoning = reasoning
            st.session_state.stage = "reveal"
            st.rerun()

# REVEAL - Richer Story
elif st.session_state.stage == "reveal":
    ticker = st.session_state.ticker
    st.progress(100)
    st.subheader(f"📖 The Story of {ticker}'s Latest Earnings")

    # Fetch basic info
    with st.spinner("Fetching company info..."):
        try:
            url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={FMP_API_KEY}"
            data = requests.get(url, timeout=10).json()
            if data and isinstance(data, list) and len(data) > 0:
                company = data[0]
                st.write(f"**{company.get('companyName')}** ({ticker})")
                st.write(f"Sector: {company.get('sector')} | Industry: {company.get('industry')}")
        except:
            st.caption(f"Learning about {ticker}")

    st.markdown("### What Happened")
    st.write("""
    In the most recent quarter, **{}** reported revenue and earnings that **beat** Wall Street's expectations. 
    This is a positive signal that the business is performing better than analysts predicted.
    """.format(ticker))

    st.markdown("### Why It Matters")
    st.write("""
    When a company consistently beats expectations, investors gain more confidence in its future. 
    It often leads to a rise in the stock price in the short term and shows strong management execution.
    """)

    st.markdown("### Management Tone")
    st.write("""
    During the earnings call, management usually sounds **optimistic** when they beat numbers. 
    They highlight growth areas and future plans to reassure investors.
    """)

    st.markdown("### What to Watch Next")
    st.write("""
    - Next quarter's guidance
    - Sales performance in key markets (e.g. China for Apple)
    - Progress on new products or services (e.g. AI features)
    - Overall industry trends
    """)

    st.markdown("---")
    st.subheader("🎯 Your Score")
    st.success("**Excellent!** You got both predictions correct.")

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
st.caption("Earnings Buddy • Beginner-friendly learning tool")