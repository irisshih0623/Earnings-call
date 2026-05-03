import streamlit as st

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Learn earnings by industry & company")

st.markdown("---")

# ================== YOUR CONTENT HERE ==================
industries = {
    "Technology": {
        "NVDA": {
            "name": "NVIDIA (NVDA)",
            "content": """**Latest:** Q4 FY2026 (ended Jan 25, 2026), reported Feb 25, 2026

**Key financial metrics:** Record quarterly revenue $68.1B (+73% YoY); Data Center $62.3B (+75% YoY); Strong gross margins (~75%).

**Management highlights:** CEO Jensen Huang highlighted the "agentic AI inflection point", surging adoption of Blackwell/Rubin platforms, and massive demand from hyperscalers.

**Price movement:** Mixed/sank ~5% initially despite beat — concerns over valuation and competition.

**Market discussion:** AI leadership validated but debates on bubble risks and sustainability of growth."""
        },
        "AAPL": {
            "name": "Apple (AAPL)",
            "content": """**Latest:** Q2 FY2026 (ended March 28, 2026), reported April 30, 2026

**Key financial metrics:** Revenue $111.2B (+17% YoY), record March quarter; iPhone strong; Services record.

**Management highlights:** Tim Cook cited extraordinary iPhone demand, AI features, and services momentum. Upbeat guidance + buyback.

**Price movement:** Positive — rose ~3-5%.

**Market discussion:** Relief on hardware recovery and AI integration roadmap."""
        },
        "GOOGL": {
            "name": "Alphabet (GOOGL)",
            "content": """**Latest:** Q1 2026 (ended March 31, 2026)

**Key financial metrics:** Revenue $109.9B (+22% YoY); Google Cloud strong growth.

**Management highlights:** Strong AI momentum with Gemini and cloud backlog.

**Price movement:** Strong surge (~10%).

**Market discussion:** AI spending paying off."""
        },
        "MSFT": {
            "name": "Microsoft (MSFT)",
            "content": """**Latest:** Q3 FY2026 (ended March 31, 2026)

**Key financial metrics:** Revenue $82.9B (+18% YoY); Azure +40%.

**Management highlights:** Emphasis on AI/cloud demand and Copilot adoption.

**Price movement:** Dipped slightly post-earnings.

**Market discussion:** Solid execution but capex concerns."""
        },
        "AMZN": {
            "name": "Amazon (AMZN)",
            "content": """**Latest:** Q1 2026 (ended March 31, 2026)

**Key financial metrics:** Net sales $181.5B (+17% YoY); AWS strong growth.

**Management highlights:** AWS AI acceleration and retail efficiency.

**Price movement:** Mixed/volatile.

**Market discussion:** Positive on AI/cloud momentum but capex focus."""
        }
    },
    # You can add more industries here later
}

# ================== APP LOGIC ==================
if 'stage' not in st.session_state:
    st.session_state.stage = "industry"
if 'selected_industry' not in st.session_state:
    st.session_state.selected_industry = None
if 'selected_company' not in st.session_state:
    st.session_state.selected_company = None

# Stage 1: Industry
if st.session_state.stage == "industry":
    st.subheader("Step 1: Choose an Industry")
    for industry in industries.keys():
        if st.button(industry, use_container_width=True):
            st.session_state.selected_industry = industry
            st.session_state.stage = "company"
            st.rerun()

# Stage 2: Company
elif st.session_state.stage == "company":
    industry = st.session_state.selected_industry
    st.subheader(f"Step 2: Companies in **{industry}**")

    for ticker, data in industries[industry].items():
        if st.button(data["name"], use_container_width=True):
            st.session_state.selected_company = ticker
            st.session_state.stage = "earnings"
            st.rerun()

    if st.button("← Back to Industries"):
        st.session_state.stage = "industry"
        st.rerun()

# Stage 3: Earnings + Questions
elif st.session_state.stage == "earnings":
    industry = st.session_state.selected_industry
    ticker = st.session_state.selected_company
    data = industries[industry][ticker]

    st.subheader(data["name"])
    st.markdown("### Latest Earnings Summary")
    st.write(data["content"])

    st.markdown("### Your Prediction")
    prediction = st.text_area("What do you think will happen to the stock price after this earnings? Why?", height=150)

    if st.button("Submit Prediction"):
        st.session_state.prediction = prediction
        st.success("Prediction saved! (Analysis section coming soon)")

    if st.button("← Back to Companies"):
        st.session_state.stage = "company"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Edit the 'industries' dictionary in the code to add more content")