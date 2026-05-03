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

# Data - You can edit this easily
industries = {
    "Technology": {
        "AAPL": {"name": "Apple Inc.", "content": "Latest Earnings: Strong iPhone sales and services growth. Beat expectations. Management optimistic on AI features."},
        "NVDA": {"name": "NVIDIA", "content": "Explosive demand for AI chips. Massive beat on revenue and guidance."},
        "MSFT": {"name": "Microsoft", "content": "Cloud and AI (Azure + OpenAI) driving strong growth."},
        "GOOGL": {"name": "Alphabet (Google)", "content": "Search and YouTube solid. Cloud improving."},
        "AMZN": {"name": "Amazon", "content": "AWS cloud and e-commerce showing resilience."}
    },
    "Energy": {
        "XOM": {"name": "ExxonMobil", "content": "Oil prices stable. Strong cash flow from upstream."},
        "CVX": {"name": "Chevron", "content": "Solid production and dividend growth."},
        # Add more as you like
    },
    "Luxury": {
        "LVMUY": {"name": "LVMH", "content": "Demand in Asia recovering."},
        # Add more
    },
    "Industrials": {
        "GE": {"name": "GE Aerospace", "content": "Strong orders in aviation."},
    },
    "Financials": {
        "JPM": {"name": "JPMorgan Chase", "content": "Record revenue from investment banking."},
    }
}

if 'stage' not in st.session_state:
    st.session_state.stage = "industry"
if 'selected_industry' not in st.session_state:
    st.session_state.selected_industry = None
if 'selected_company' not in st.session_state:
    st.session_state.selected_company = None

# STAGE 1: Choose Industry
if st.session_state.stage == "industry":
    st.subheader("Step 1: Choose an Industry")
    cols = st.columns(3)
    for i, industry in enumerate(industries.keys()):
        with cols[i % 3]:
            if st.button(industry, use_container_width=True):
                st.session_state.selected_industry = industry
                st.session_state.stage = "company"
                st.rerun()

# STAGE 2: Choose Company
elif st.session_state.stage == "company":
    industry = st.session_state.selected_industry
    st.subheader(f"Step 2: Choose a company in **{industry}**")

    companies = industries[industry]
    cols = st.columns(3)
    for i, (ticker, info) in enumerate(companies.items()):
        with cols[i % 3]:
            if st.button(info["name"], use_container_width=True):
                st.session_state.selected_company = ticker
                st.session_state.stage = "earnings"
                st.rerun()

    if st.button("← Back to Industries"):
        st.session_state.stage = "industry"
        st.rerun()

# STAGE 3: Earnings Info + Questions
elif st.session_state.stage == "earnings":
    ticker = st.session_state.selected_company
    industry = st.session_state.selected_industry
    info = industries[industry][ticker]

    st.subheader(f"{info['name']} ({ticker}) - Latest Earnings")

    st.markdown("### Key Financial Metrics & Highlights")
    st.write(info["content"])   # ← You write your own content here

    st.markdown("### Your Prediction")
    prediction = st.text_area("What do you think will happen to the stock price after this earnings? Why?", height=150)

    if st.button("Submit Prediction & See Analysis"):
        st.session_state.prediction = prediction
        st.session_state.stage = "analysis"
        st.rerun()

    if st.button("← Back"):
        st.session_state.stage = "company"
        st.rerun()

# STAGE 4: Analysis
elif st.session_state.stage == "analysis":
    ticker = st.session_state.selected_company
    info = industries[st.session_state.selected_industry][ticker]

    st.subheader(f"Analysis for {info['name']}")

    st.markdown("### Actual Price Movement")
    st.write("**Post-earnings reaction:** +2.8% in the first trading day (example).")

    st.markdown("### Possible Factors")
    st.write("- Beat on revenue and EPS\n- Strong guidance\n- Market sentiment on AI / sector trends")

    st.markdown("### What the Market is Discussing")
    st.write("Analysts are focusing on long-term growth drivers...")

    st.markdown("### Peer Comparison")
    st.write("Compared to peers in the same industry, this company performed better/worse in...")

    if st.button("Try Another Company"):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "industry"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Add your own content in the industries dictionary")