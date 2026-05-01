import streamlit as st

st.set_page_config(
    page_title="Earnings Buddy",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Warm & Beginner-Friendly Styling
st.markdown("""
    <style>
    .main {
        background-color: #fffaf0;
    }
    h1 {
        color: #e63946;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #e63946;
        color: white;
        font-weight: 500;
    }
    .warm-text {
        color: #2a9d8f;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Your friendly companion for learning company earnings")

st.markdown("---")

# Session State
if 'stage' not in st.session_state:
    st.session_state.stage = "home"
if 'ticker' not in st.session_state:
    st.session_state.ticker = ""

# ====================== HOME ======================
if st.session_state.stage == "home":
    st.write("👋 Welcome! Turn real earnings into an interactive learning experience.")

    col1, col2 = st.columns([3, 1])
    with col1:
        ticker = st.text_input("Enter stock ticker", 
                              placeholder="AAPL, TSLA, NVDA", 
                              help="e.g. AAPL for Apple")

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
    st.success(f"📊 Now exploring **{st.session_state.ticker}** earnings")

    st.subheader("🧠 Make Your Predictions")

    with st.form("pred_form"):
        q1 = st.radio(
            "1. Did they beat revenue expectations?",
            ["Yes, they beat", "No, they missed", "Not sure"],
            key="q1r"
        )
        q2 = st.radio(
            "2. Was management tone more optimistic than last quarter?",
            ["More optimistic", "More cautious", "About the same", "Not sure"],
            key="q2r"
        )

        confidence = st.slider("How confident are you in your answers?", 20, 100, 60, step=10)

        reasoning = st.text_area("Your reasoning (optional):", 
                                placeholder="I think they beat because...", 
                                height=80)

        if st.form_submit_button("Submit & See What Happened", type="primary"):
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.confidence = confidence
            st.session_state.reasoning = reasoning
            st.session_state.stage = "reveal"
            st.rerun()

# ====================== REVEAL ======================
elif st.session_state.stage == "reveal":
    ticker = st.session_state.ticker

    st.progress(100)
    st.subheader(f"📖 The Story of {ticker}'s Earnings")

    st.markdown("### What Happened")
    st.markdown("""
    The company announced strong results and **beat** revenue expectations. 
    This is generally seen as a positive signal.
    """)

    st.markdown("### Why It Matters")
    st.markdown("""
    Beating expectations shows the business is performing better than analysts predicted. 
    It often leads to a positive stock reaction.
    """)

    st.markdown("### Management Tone")
    st.markdown("Management sounded **optimistic** about the company's future.")

    st.markdown("### What to Watch Next")
    st.markdown("Pay attention to future guidance and performance in key markets.")

    st.markdown("---")

    st.subheader("🎯 Your Score")
    st.success("**Well done!** You got both predictions correct.")

    st.metric("Your Confidence", f"{st.session_state.get('confidence', 60)}%")

    if st.session_state.get("reasoning"):
        st.info(f"**Your Reasoning:** {st.session_state.reasoning}")

    st.balloons()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Another Stock", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key not in ["stage"]:
                    del st.session_state[key]
            st.session_state.stage = "home"
            st.rerun()

    with col2:
        if st.button("📊 My Learning Progress", use_container_width=True):
            st.info("📈 Learning profile feature coming soon!")

# Footer
st.markdown("---")
st.caption("Earnings Buddy • Making earnings easy & fun for beginners")