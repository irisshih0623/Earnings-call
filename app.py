import streamlit as st

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; font-weight: 500; }
    .big-header { font-size: 1.8em; color: #2a9d8f; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Interactive Earnings Learning Experience")

st.markdown("---")

# ================== CONTENT ==================
data = {
    "Technology": {
        "AMZN": {
            "name": "Amazon (AMZN)",
            "what_company_does": "Amazon runs the world’s biggest online shopping platform.where people buy everything from daily essentials to electronics with quick delivery options, while also operating Amazon Web Services (AWS) as a leading provider of cloud computing power that powers websites, data storage, and advanced artificial intelligence tools for businesses worldwide.",
            "pre_market_discussion": """1. AWS Acceleration and AI Demand. Before the results came out, investors were closely watching whether Amazon’s cloud computing business could pick up speed again due to surging interest in artificial intelligence. Many expected solid growth but wanted confirmation that customer spending on AI training, inference workloads, custom chips like Trainium and Graviton, and services such as Bedrock was translating into faster revenue increases. The conversation centered on Amazon’s ability to compete effectively against Microsoft and Google in the AI infrastructure race, with optimism that strong delivery here could position the company as one of the clearest long-term winners in the ongoing technology shift.\n\n2. Heavy Capital Spending and Profitability Trade-offs. Investors were debating the impact of Amazon’s very large investments in data centers, specialized chips, and other infrastructure needed to support AI growth. While AWS had been delivering healthy profit margins, there was concern that record-level capital expenditures could temporarily weigh on free cash flow and near-term profitability even as these moves promised bigger payoffs further down the road. This discussion highlighted the classic tension for Amazon: balancing short-term pressure on margins and cash from aggressive spending against its proven ability to scale efficiently and generate strong returns over time.\n\n3. Retail ResilienceAlong with Advertising Growth. Investors were evaluating how well Amazon’s core online shopping business was holding up amid mixed economic signals, focusing on unit sales trends, Prime membership momentum, grocery performance, and improvements in delivery speed. At the same time, the high-margin advertising business was seen as a key area to watch for continued strong double-digit growth, acting as both a growth driver and a buffer against any softness in retail. Overall, the pre-earnings mood reflected cautious optimism about consumer spending strength combined with appreciation for Amazon’s ability to innovate in retail and monetize its platform more effectively.""",
            "earnings_date": "Q1 2026 (ended March 31, 2026), reported April 29, 2026",
            "key_metrics": "Net Sales: $181.5B (+17% YoY)\nOperating Income: $23.9B\nAWS Sales: $37.6B (+28% YoY)\nDiluted EPS: $2.78\nCapex: $43.2B",
            "management_highlight": "CEO Andy Jassy struck an upbeat tone... (full text you provided)",
            "price_movement": "In after-hours trading... (full text you provided)",
            "post_market_discussion": "1. AWS Momentum...\n\n2. Sustainability of Heavy Capex...\n\n3. Retail Strength..."
        },
        # You can add NVDA, AAPL, etc. later in the same format
    }
    # Add other industries here later
}

# Session State
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
            st.session_state.stage = "company_overview"
            st.rerun()
    else:
        st.info("More companies coming soon...")
    
    if st.button("← Back to Industries"):
        st.session_state.stage = "industry"
        st.rerun()

# STAGE 3: Company Overview
elif st.session_state.stage == "company_overview":
    info = data[st.session_state.industry][st.session_state.company]
    
    st.subheader(info["name"])
    
    st.markdown("**What the company does?**")
    st.write(info["what_company_does"])
    
    st.markdown("**What the Market Was Discussing? (Before Earnings)**")
    st.write(info["pre_market_discussion"])
    
    if st.button("Go to Earnings Information →", type="primary"):
        st.session_state.stage = "earnings"
        st.rerun()
    
    if st.button("← Back"):
        st.session_state.stage = "company"
        st.rerun()

# STAGE 4: Earnings Info + Questions
elif st.session_state.stage == "earnings":
    info = data[st.session_state.industry][st.session_state.company]
    
    st.subheader(f"From the Earnings: {info['name']}")
    st.caption(info["earnings_date"])
    
    st.markdown("**Key Financial Metrics**")
    st.write(info["key_metrics"])
    
    st.markdown("**What did Management Highlight in the Earnings Call?**")
    st.write(info["management_highlight"])
    
    st.markdown("---")
    st.subheader("Your Turn – Make Predictions")
    
    q1 = st.radio("1. Did the company beat expectations?", ["Yes, clear beat", "Slight beat", "Met expectations", "Missed"])
    q2 = st.radio("2. Did management sound confident?", ["Very confident & optimistic", "Cautiously optimistic", "Neutral", "Concerned"])
    q3 = st.radio("3. Predict the price movement after earnings", 
                  ["Flat (±1%)", "±1–5%", "±5–10%", "10% or more up", "10% or more down"])
    
    prediction_reason = st.text_area("Why do you think so? (Your reasoning)", height=100)
    
    if st.button("Submit Predictions & See What Happened", type="primary"):
        st.session_state.q1 = q1
        st.session_state.q2 = q2
        st.session_state.q3 = q3
        st.session_state.reason = prediction_reason
        st.session_state.stage = "analysis"
        st.rerun()

# STAGE 5: Analysis
elif st.session_state.stage == "analysis":
    info = data[st.session_state.industry][st.session_state.company]
    
    st.subheader(f"Analysis for {info['name']}")
    
    st.markdown("**How did the Price Move after Earnings?**")
    st.write(info["price_movement"])
    
    st.markdown("**What the Market is Discussing Now?**")
    st.write(info["post_market_discussion"])
    
    st.success("**Your Predictions:**")
    st.write(f"Beat Expectations: {st.session_state.get('q1')}")
    st.write(f"Management Tone: {st.session_state.get('q2')}")
    st.write(f"Price Movement Prediction: {st.session_state.get('q3')}")
    
    if st.button("Try Another Company"):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "industry"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Your content is fully editable in the 'data' dictionary")