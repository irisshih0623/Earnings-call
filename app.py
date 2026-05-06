import streamlit as st

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; font-weight: 500; }
    .section-header { font-size: 1.5em; color: #2a9d8f; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Interactive Earnings Learning Experience")

st.markdown("---")

# ================== FULL AMAZON CONTENT ==================
amzn_data = {
    "name": "Amazon (AMZN)",
    "what_company_does": "Amazon runs the world’s biggest online shopping platform where people buy everything from daily essentials to electronics with quick delivery options, while also operating Amazon Web Services (AWS) as a leading provider of cloud computing power that powers websites, data storage, and advanced artificial intelligence tools for businesses worldwide.",
    "pre_market_discussion": """1. AWS Acceleration and AI Demand: Investors were closely watching whether AWS could pick up speed due to surging AI interest.\n\n2. Heavy Capital Spending: Concerns about very large investments in data centers and chips weighing on near-term profitability.\n\n3. Retail Resilience & Advertising: How well the core shopping business and high-margin advertising were performing.""",
    "earnings_date": "Q1 2026 (ended March 31, 2026) — Reported April 29, 2026",
    "key_metrics": "• Net Sales: $181.5 billion (+17% YoY)\n• Operating Income: $23.9 billion\n• AWS Sales: $37.6 billion (+28% YoY)\n• Diluted EPS: $2.78\n• Capital Expenditure: $43.2 billion",
    "management_highlight": "CEO Andy Jassy was upbeat: “AWS is growing 28% year-over-year, the fastest growth rate in 15 quarters... We’ve never seen a technology grow as rapidly as AI.” He called it one of the biggest inflections of our lifetime.",
    "price_movement": "After-hours initially dipped 0.8–3%. The next day it recovered and closed modestly higher (~0.8–1.3%). Over the following week it showed modest gains of 1–2%.",
    "post_market_discussion": "1. AWS Momentum and AI Monetization Progress\n2. Sustainability of Heavy Capex and Path to Higher Free Cash Flow\n3. Retail Strength, Advertising, and Valuation Re-rating"
}

if 'stage' not in st.session_state: st.session_state.stage = "industry"
if 'industry' not in st.session_state: st.session_state.industry = None
if 'company' not in st.session_state: st.session_state.company = None

# STAGE 1: Select Industry
if st.session_state.stage == "industry":
    st.subheader("Step 1: Choose an Industry")
    for industry in ["Technology", "Energy", "Industrials", "Financials", "Luxury"]:
        if st.button(industry, use_container_width=True):
            st.session_state.industry = industry
            st.session_state.stage = "company"
            st.rerun()

# STAGE 2: Select Company
elif st.session_state.stage == "company":
    st.subheader(f"Step 2: Choose a Company in **{st.session_state.industry}**")
    
    if st.session_state.industry == "Technology":
        if st.button("Amazon (AMZN)", use_container_width=True):
            st.session_state.company = "AMZN"
            st.session_state.stage = "company_info"
            st.rerun()
    else:
        st.info("More companies will be added soon!")
    
    if st.button("← Back to Industries"):
        st.session_state.stage = "industry"
        st.rerun()

# STAGE 3: Company Information
elif st.session_state.stage == "company_info":
    st.subheader(amzn_data["name"])
    
    st.markdown('<p class="section-header">What the company does?</p>', unsafe_allow_html=True)
    st.write(amzn_data["what_company_does"])
    
    st.markdown('<p class="section-header">What the Market Was Discussing Before Earnings</p>', unsafe_allow_html=True)
    with st.expander("Click to read the full pre-earnings discussion"):
        st.write(amzn_data["pre_market_discussion"])
    
    if st.button("Continue to Latest Earnings →", type="primary", use_container_width=True):
        st.session_state.stage = "earnings"
        st.rerun()

    if st.button("← Back to Companies"):
        st.session_state.stage = "company"
        st.rerun()

# STAGE 4: Earnings + Questions
elif st.session_state.stage == "earnings":
    st.subheader(f"From the Earnings: {amzn_data['name']}")
    st.caption(amzn_data["earnings_date"])
    
    st.markdown('<p class="section-header">Key Financial Metrics</p>', unsafe_allow_html=True)
    st.write(amzn_data["key_metrics"])
    
    st.markdown('<p class="section-header">What did Management Highlight in the Earnings Call?</p>', unsafe_allow_html=True)
    st.write(amzn_data["management_highlight"])
    
    st.markdown("---")
    st.subheader("Your Predictions")
    
    q1 = st.radio("1. Did the company beat expectations?", ["Yes, clear beat", "Slight beat", "Met expectations", "Missed"])
    q2 = st.radio("2. Did management sound confident?", ["Very confident & optimistic", "Cautiously optimistic", "Neutral", "Concerned"])
    q3 = st.radio("3. Predict price movement after earnings", ["Flat (±1%)", "±1–5%", "±5–10%", "10%+ Up", "10%+ Down"])
    
    reason = st.text_area("Why do you think so?", height=120)
    
    if st.button("Submit Predictions & See Results", type="primary", use_container_width=True):
        st.session_state.answers = (q1, q2, q3, reason)
        st.session_state.stage = "analysis"
        st.rerun()

# STAGE 5: Analysis
elif st.session_state.stage == "analysis":
    st.subheader(f"Analysis — {amzn_data['name']}")
    
    st.markdown('<p class="section-header">How did the Price Move after Earnings?</p>', unsafe_allow_html=True)
    st.write(amzn_data["price_movement"])
    
    st.markdown('<p class="section-header">What the Market is Discussing Now?</p>', unsafe_allow_html=True)
    with st.expander("Click to read current market discussion"):
        st.write(amzn_data["post_market_discussion"])
    
    st.success("**Your Predictions**")
    q1, q2, q3, reason = st.session_state.answers
    st.write(f"1. Beat Expectations: {q1}")
    st.write(f"2. Management Tone: {q2}")
    st.write(f"3. Price Movement: {q3}")
    if reason:
        st.info(f"Your Reasoning: {reason}")
    
    if st.button("Try Another Company", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "industry"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Technology Focus • AMZN Example")