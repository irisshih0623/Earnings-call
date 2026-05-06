import streamlit as st

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; font-weight: 500; }
    .section { background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Your friendly guide to understanding earnings")

st.markdown("---")

# ================== AMAZON CONTENT ==================
amzn = {
    "name": "Amazon (AMZN)",
    "what_company_does": "Amazon runs the world’s biggest online shopping platform where people buy everything from daily essentials to electronics with quick delivery options, while also operating Amazon Web Services (AWS) — a leading provider of cloud computing power that powers websites, data storage, and advanced artificial intelligence tools for businesses worldwide.",
    
    "pre_market": """
    • AWS Acceleration & AI Demand  
    • Heavy Capital Spending vs Future Growth  
    • Retail Resilience & Advertising Growth
    """,
    
    "earnings_date": "Q1 2026 (ended March 31, 2026) — Reported April 29, 2026",
    
    "key_metrics": """
    • Net Sales: **$181.5 billion** (+17% YoY)  
    • Operating Income: **$23.9 billion**  
    • AWS Sales: **$37.6 billion** (+28% YoY)  
    • Diluted EPS: **$2.78**  
    • Capital Expenditure: **$43.2 billion**
    """,
    
    "management": "CEO Andy Jassy was upbeat: “AWS is growing 28% year-over-year, the fastest growth rate in 15 quarters... We’ve never seen a technology grow as rapidly as AI.” He expressed strong confidence in Amazon’s AI position and long-term outlook.",
    
    "price_movement": "After-hours: initially down 0.8–3% → Next day: recovered and closed modestly higher (~0.8–1.3%). Over the following week: modest gains of 1–2%.",
    
    "post_market": """
    • AWS Momentum and AI Monetization  
    • Sustainability of Heavy Capex  
    • Retail Strength & Advertising Growth
    """
}

# Session State
if 'stage' not in st.session_state:
    st.session_state.stage = "overview"

# ================== STAGES ==================

if st.session_state.stage == "overview":
    st.subheader(amzn["name"])
    
    with st.container():
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("**What the company does?**")
        st.write(amzn["what_company_does"])
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown("**What the Market Was Discussing Before Earnings**")
        st.write(amzn["pre_market"])
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Go to Earnings Analysis →", type="primary", use_container_width=True):
        st.session_state.stage = "earnings"
        st.rerun()

elif st.session_state.stage == "earnings":
    st.subheader(f"From the Earnings — {amzn['name']}")
    st.caption(amzn["earnings_date"])

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Key Financial Metrics**")
        st.write(amzn["key_metrics"])
    
    with col2:
        st.markdown("**What Management Highlighted**")
        st.write(amzn["management"])

    st.markdown("---")
    st.subheader("Your Predictions")

    q1 = st.radio("1. Did the company beat expectations?", 
                  ["Yes, clear beat", "Slight beat", "Met expectations", "Missed"])
    q2 = st.radio("2. Did management sound confident?", 
                  ["Very confident & optimistic", "Cautiously optimistic", "Neutral", "Concerned"])
    q3 = st.radio("3. Predict the stock price movement", 
                  ["Flat (±1%)", "±1–5%", "±5–10%", "10% or more up", "10% or more down"])

    reason = st.text_area("Why do you think so? (Your reasoning)", height=100)

    if st.button("Submit Predictions & See Results", type="primary", use_container_width=True):
        st.session_state.answers = (q1, q2, q3, reason)
        st.session_state.stage = "results"
        st.rerun()

elif st.session_state.stage == "results":
    st.subheader(f"Results — {amzn['name']}")

    st.markdown("**How did the Price Move after Earnings?**")
    st.write(amzn["price_movement"])

    st.markdown("**What the Market is Discussing Now?**")
    st.write(amzn["post_market"])

    st.success("**Your Predictions**")
    q1, q2, q3, reason = st.session_state.answers
    st.write(f"• Beat Expectations: **{q1}**")
    st.write(f"• Management Tone: **{q2}**")
    st.write(f"• Predicted Price Move: **{q3}**")
    if reason:
        st.info(f"**Your Reasoning:** {reason}")

    if st.button("Restart with Another Company", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "overview"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Amazon Case Study")