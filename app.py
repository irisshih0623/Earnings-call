import streamlit as st

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Learn earnings by industry & company")

st.markdown("---")

# ================== YOUR CONTENT ==================
data = {
    "Technology": {
        "NVDA": {
            "name": "NVIDIA (NVDA)",
            "earnings": "Q4 FY2026 (ended Jan 25, 2026), reported Feb 25, 2026",
            "metrics": "Record quarterly revenue $68.1B (+73% YoY); Data Center $62.3B (+75% YoY); GAAP EPS ~$1.76 (non-GAAP $1.62, beat); Full-year FY2026 revenue $215.9B (+65% YoY). Strong gross margins (~75%).",
            "management": "CEO Jensen Huang highlighted the \"agentic AI inflection point,\" surging adoption of Blackwell/Rubin platforms, and massive demand from hyperscalers.",
            "price_movement": "Mixed/sank ~5% initially (despite beat). Investors looked past strong results amid concerns over high valuation and competition.",
            "market_discussion": "AI leadership validated but debates on bubble risks, Blackwell ramp, competition from AMD/hyperscalers' in-house chips."
        },
        "AAPL": {
            "name": "Apple (AAPL)",
            "earnings": "Q2 FY2026 (ended March 28, 2026), reported April 30, 2026",
            "metrics": "Revenue $111.2B (+17% YoY), record for March quarter; EPS $2.01 (+22% YoY, beat); iPhone ~$57B (+22%); Services record ~$31B.",
            "management": "Tim Cook cited \"extraordinary\" demand for iPhone, record install base, AI-focused silicon, and services momentum. Upbeat guidance and $100B buyback.",
            "price_movement": "Positive—rose ~3-5%. Strong beat, guidance, and iPhone/Services strength drove optimism.",
            "market_discussion": "Relief on hardware recovery (iPhone/China), services growth, and AI integration roadmap."
        },
        "GOOGL": {
            "name": "Alphabet (GOOGL)",
            "earnings": "Q1 2026 (ended March 31, 2026), reported ~April 29, 2026",
            "metrics": "Revenue $109.9B (+22% YoY, beat); Google Cloud ~$20B (+63%); EPS $5.11 (strong beat).",
            "management": "Strong AI momentum (Gemini, cloud backlog doubling); Heavy capex on AI infrastructure acknowledged.",
            "price_movement": "Strong surge (~10%). Cloud/AI acceleration seen as validation.",
            "market_discussion": "AI spending paying off; capex concerns tempered by growth."
        },
        "MSFT": {
            "name": "Microsoft (MSFT)",
            "earnings": "Q3 FY2026 (ended March 31, 2026), reported April 29, 2026",
            "metrics": "Revenue $82.9B (+18% YoY, beat); Intelligent Cloud strong (Azure +40%); EPS $4.27.",
            "management": "Satya Nadella emphasized AI/cloud demand, Copilot adoption, and foundational improvements.",
            "price_movement": "Dipped ~1-5% post-earnings. Guidance/capex concerns outweighed beat for some.",
            "market_discussion": "Solid AI/cloud execution but questions on monetization pace and high capex."
        },
        "AMZN": {
            "name": "Amazon (AMZN)",
            "earnings": "Q1 2026 (ended March 31, 2026), reported April 29, 2026",
            "metrics": "Net sales $181.5B (+17% YoY, beat); AWS $37.6B (+28%); Operating income $23.9B (record margin).",
            "management": "Andy Jassy highlighted AWS AI acceleration, retail efficiency, and aggressive capex on AI.",
            "price_movement": "Mixed/volatile (initial dips then recovered). AWS strength supportive.",
            "market_discussion": "AWS reacceleration as key AI proxy; focus on capex vs. FCF pressure."
        }
    }
    # You can add other industries here later (Energy, Luxury, etc.)
}

if 'stage' not in st.session_state:
    st.session_state.stage = "industry"
if 'selected_industry' not in st.session_state:
    st.session_state.selected_industry = None
if 'selected_company' not in st.session_state:
    st.session_state.selected_company = None

# STAGE 1: Industry
if st.session_state.stage == "industry":
    st.subheader("Step 1: Choose an Industry")
    if st.button("Technology", use_container_width=True):
        st.session_state.selected_industry = "Technology"
        st.session_state.stage = "company"
        st.rerun()

# STAGE 2: Company
elif st.session_state.stage == "company":
    st.subheader(f"Step 2: Choose a company in **{st.session_state.selected_industry}**")
    companies = data[st.session_state.selected_industry]
    
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

# STAGE 3: Earnings Summary + Prediction
elif st.session_state.stage == "earnings":
    ticker = st.session_state.selected_company
    info = data[st.session_state.selected_industry][ticker]

    st.subheader(f"{info['name']} – Latest Earnings")
    st.caption(info["earnings"])

    st.markdown("**Key Financial Metrics**")
    st.write(info["metrics"])

    st.markdown("**Management Highlights**")
    st.write(info["management"])

    st.markdown("### Your Prediction")
    prediction = st.text_area("What do you think the price movement will be after this earnings? Why?", height=150)

    if st.button("Submit Prediction & See Analysis", type="primary"):
        st.session_state.prediction = prediction
        st.session_state.stage = "analysis"
        st.rerun()

    if st.button("← Back"):
        st.session_state.stage = "company"
        st.rerun()

# STAGE 4: Analysis
elif st.session_state.stage == "analysis":
    ticker = st.session_state.selected_company
    info = data[st.session_state.selected_industry][ticker]

    st.subheader(f"Analysis for {info['name']}")

    st.markdown("### Price Movement After Earnings")
    st.write(info["price_movement"])

    st.markdown("### Market Discussion")
    st.write(info["market_discussion"])

    st.markdown("### Your Prediction")
    st.info(st.session_state.get("prediction", "No prediction provided."))

    if st.button("Try Another Company"):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "industry"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Add more industries/companies in the 'data' dictionary")