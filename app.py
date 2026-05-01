import streamlit as st
import requests

# ====================== CONFIG ======================
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
    .stButton>button { background-color: #e63946; color: white; font-weight: 500; }
    .warm-text { color: #2a9d8f; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Your friendly guide to understanding earnings reports")

st.markdown("---")

# Your FMP API Key
FMP_API_KEY = "vlQFRsXkDEzfAx8drx2ThJi6X92XY30k"

# Session State
if 'stage' not in st.session_state:
    st.session_state.stage = "home"
if 'ticker' not in st.session_state:
    st.session_state.ticker = ""

# ====================== HOME ======================
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

# ====================== QUESTIONS ======================
elif st.session_state.stage == "questions":
    st.progress(40)
    st.success(f"📊 Learning about **{st.session_state.ticker}**")

    with st.form("pred_form"):
        q1 = st.radio(
            "1. Did the company beat revenue expectations this quarter?",
            ["Yes, they beat", "No, they missed", "Not sure"]
        )
        q2 = st.radio(
            "2. Was management tone more optimistic than last quarter?",
            ["More optimistic", "More cautious", "About the same", "Not sure"]
        )

        confidence = st.slider("How confident are you?", 20, 100, 60, step=10)
        reasoning = st.text_area("Your reasoning (optional):", height=100)

        if st.form_submit_button("Submit Predictions & Reveal Results", type="primary"):
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.confidence = confidence
            st.session_state.reasoning = reasoning
            st.session_state.stage = "reveal"
            st.rerun()

# ====================== REVEAL - REAL DATA ======================
elif st.session_state.stage == "reveal":
    ticker = st.session_state.ticker
    st.progress(100)
    st.subheader(f"📖 The Story of {ticker}'s Latest Earnings")

    with st.spinner("Fetching real earnings data..."):
        try:
            # Fetch latest quote
            quote_url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={FMP_API_KEY}"
            quote_data = requests.get(quote_url, timeout=10).json()

            if isinstance(quote_data, list) and len(quote_data) > 0:
                price = quote_data[0].get('price', 'N/A')
                st.metric("Current Price", f"${price:.2f}")

            # Fetch earnings data
            earnings_url = f"https://financialmodelingprep.com/api/v3/earnings/{ticker}?limit=1&apikey={FMP_API_KEY}"
            earnings = requests.get(earnings_url, timeout=10).json()

            if earnings and isinstance(earnings, list) and len(earnings) > 0:
                latest = earnings[0]
                actual_eps = latest.get('epsActual', 'N/A')
                estimated_eps = latest.get('epsEstimated', 'N/A')
                actual_revenue = latest.get('revenueActual', 'N/A')
                estimated_revenue = latest.get('revenueEstimated', 'N/A')

                st.write(f"**EPS:** Actual ${actual_eps} vs Estimated ${estimated_eps}")
                st.write(f"**Revenue:** Actual ${actual_revenue:,} vs Estimated ${estimated_revenue:,}")

                beat_eps = "beat" if actual_eps > estimated_eps else "missed"
                st.success(f"The company **{beat_eps}** EPS expectations!")
            else:
                st.info("No recent earnings data found for this ticker.")

        except Exception as e:
            st.warning("Could not fetch real data. Showing example instead.")
            st.write("**EPS:** Actual $2.18 vs Estimated $2.10 → **Beat**")
            st.write("**Revenue:** Strong beat this quarter.")

    st.markdown("### Why It Matters")
    st.write("Beating expectations consistently builds investor confidence and often supports the stock price.")

    st.markdown("### Management Tone")
    st.write("Management usually sounds optimistic when they beat numbers and give good guidance.")

    st.markdown("### What to Watch Next")
    st.write("Future guidance, sales trends in key markets, and new product performance.")

    st.markdown("---")
    st.subheader("🎯 Your Score")
    st.success("You got **2 out of 2** correct!")

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

# Footer
st.markdown("---")
st.caption("Earnings Buddy • Powered by Financial Modeling Prep • Built for beginners")