import streamlit as st

st.set_page_config(page_title="Earnings Buddy", page_icon="📚", layout="centered")

# ================== GLOBAL STYLING ==================
st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    h1 { color: #e63946; }
    .stButton>button { background-color: #e63946; color: white; font-weight: 500; }
    .section-header {
        font-size: 1.4em;
        color: #2a9d8f;
        margin-top: 24px;
        margin-bottom: 8px;
        font-weight: 600;
        border-left: 4px solid #e63946;
        padding-left: 10px;
    }

    .info-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .info-card h4 { margin: 0 0 6px 0; color: #1f2937; font-size: 1.05em; }
    .info-card p { margin: 0; color: #4b5563; font-size: 0.92em; line-height: 1.55; }

    .theme-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-left: 4px solid #f97316;
        border-radius: 10px;
        padding: 16px 18px;
        margin-bottom: 12px;
    }
    .theme-tag { font-size: 0.7em; font-weight: 700; color: #ea580c; letter-spacing: 1px; margin-bottom: 4px; }
    .theme-title { font-weight: 600; color: #111827; font-size: 1.02em; margin-bottom: 6px; }
    .theme-body { color: #4b5563; font-size: 0.9em; line-height: 1.55; }

    .metric-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .metric-card.highlight { border: 2px solid #fdba74; background: #fff7ed; }
    .metric-label { font-size: 0.85em; color: #6b7280; font-weight: 600; }
    .metric-value { font-size: 1.6em; font-weight: 700; color: #111827; margin: 4px 0; }
    .metric-badge { display: inline-block; font-size: 0.7em; font-weight: 700; padding: 2px 8px; border-radius: 999px; }
    .badge-green { background: #d1fae5; color: #065f46; }
    .badge-orange { background: #ffedd5; color: #9a3412; }
    .badge-blue { background: #dbeafe; color: #1e40af; }
    .badge-purple { background: #ede9fe; color: #5b21b6; }
    .badge-red { background: #fee2e2; color: #991b1b; }
    .metric-desc { font-size: 0.82em; color: #6b7280; font-style: italic; margin: 4px 0; }
    .metric-note { font-size: 0.85em; color: #374151; margin-top: 6px; }

    .quote-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 12px;
    }
    .quote-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
    .avatar {
        width: 40px; height: 40px;
        border-radius: 50%;
        color: white;
        display: flex; align-items: center; justify-content: center;
        font-weight: 700; font-size: 0.9em;
    }
    .avatar-ceo { background: #f97316; }
    .avatar-cfo { background: #2563eb; }
    .quote-name { font-weight: 600; color: #111827; }
    .quote-role { font-size: 0.8em; color: #6b7280; }
    .quote-text {
        border-left: 4px solid #f97316;
        padding-left: 12px;
        font-style: italic;
        color: #374151;
        font-size: 0.95em;
        line-height: 1.55;
    }
    .quote-text.cfo { border-left-color: #2563eb; }
    .quote-extra { font-size: 0.9em; color: #4b5563; margin-top: 10px; }
    .tone-banner {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        border-radius: 8px;
        padding: 12px 14px;
        margin-top: 10px;
        font-size: 0.9em;
        color: #78350f;
    }

    .timeline-item {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 14px 16px;
        margin-bottom: 10px;
        display: flex; gap: 14px; align-items: flex-start;
    }
    .timeline-item.up { background: #f0fdf4; }
    .timeline-item.down { background: #fef2f2; }
    .timeline-date { flex-shrink: 0; width: 70px; text-align: center; }
    .timeline-month { font-size: 0.7em; font-weight: 700; color: #6b7280; }
    .timeline-day { font-size: 1.6em; font-weight: 700; color: #111827; line-height: 1; }
    .timeline-change { font-size: 0.75em; font-weight: 700; margin-top: 4px; }
    .change-up { color: #059669; }
    .change-down { color: #dc2626; }
    .timeline-title { font-weight: 600; color: #111827; margin-bottom: 4px; }
    .timeline-desc { color: #4b5563; font-size: 0.88em; line-height: 1.55; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Earnings Buddy")
st.markdown("##### Interactive Earnings Learning Experience")
st.markdown("---")

# ================== COMPANY DATA ==================
companies = {
    "AMZN": {
        "name": "Amazon (AMZN)",
        "earnings_date": "Q1 2026 (ended March 31, 2026) — Reported April 29, 2026",
    },
    "TSLA": {
        "name": "Tesla (TSLA)",
        "earnings_date": "Q1 2026 (ended March 31, 2026) — Reported April 22, 2026 (after-market)",
    },
    "MSFT": {
        "name": "Microsoft (MSFT)",
        "earnings_date": "Q3 FY2026 (ended March 31, 2026) — Reported April 29, 2026 (after-market)",
    },
    "NVDA": {
        "name": "NVIDIA (NVDA)",
        "earnings_date": "Q4 FY2026 (ended January 25, 2026) — Reported February 25, 2026 (after-market)",
    },
    "TSM": {
        "name": "Taiwan Semiconductor (TSM)",
        "earnings_date": "Q1 2026 (ended March 31, 2026) — Reported April 29, 2026",
    },
}

# ================== SESSION STATE ==================
if 'stage' not in st.session_state: st.session_state.stage = "industry"
if 'industry' not in st.session_state: st.session_state.industry = None
if 'company' not in st.session_state: st.session_state.company = None


# ============================================================
# STAGE 1: Select Industry
# ============================================================
if st.session_state.stage == "industry":
    st.subheader("Step 1: Choose an Industry")
    for industry in ["Technology", "Energy", "Industrials", "Financials", "Luxury"]:
        if st.button(industry, use_container_width=True):
            st.session_state.industry = industry
            st.session_state.stage = "company"
            st.rerun()

# ============================================================
# STAGE 2: Select Company
# ============================================================
elif st.session_state.stage == "company":
    st.subheader(f"Step 2: Choose a Company in **{st.session_state.industry}**")
    
    if st.session_state.industry == "Technology":
        tech_companies = [
            ("Amazon (AMZN)", "AMZN"),
            ("Tesla (TSLA)", "TSLA"),
            ("Microsoft (MSFT)", "MSFT"),
            ("NVIDIA (NVDA)", "NVDA"),
            ("Taiwan Semiconductor (TSM)", "TSM"),
        ]
        for label, ticker in tech_companies:
            if st.button(label, use_container_width=True, key=f"btn_{ticker}"):
                st.session_state.company = ticker
                st.session_state.stage = "company_info"
                st.rerun()
    else:
        st.info("More companies will be added soon!")
    
    if st.button("← Back to Industries"):
        st.session_state.stage = "industry"
        st.rerun()

# ============================================================
# STAGE 3: Company Information
# ============================================================
elif st.session_state.stage == "company_info":
    company = st.session_state.company
    st.subheader(companies[company]["name"])
    
    # -------- AMZN --------
    if company == "AMZN":
        st.markdown('<p class="section-header">What the company does?</p>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>🛒 Online Retail</h4>
                <p>Operates the world's biggest online shopping platform with fast delivery across daily essentials, electronics, and more.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>☁️ Amazon Web Services (AWS)</h4>
                <p>A leading cloud computing provider powering websites, data storage, and advanced AI tools for businesses globally.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card" style="background:#f9fafb;">
            <p>Amazon runs the world's biggest online shopping platform where people buy everything from daily essentials to electronics with quick delivery options, while also operating Amazon Web Services (AWS) as a leading provider of cloud computing power that powers websites, data storage, and advanced artificial intelligence tools for businesses worldwide.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market Was Discussing Before Earnings</p>', unsafe_allow_html=True)
        st.caption("Key themes investors focused on going into the print.")
        
        st.markdown("""
        <div class="theme-card">
            <div class="theme-tag">THEME 01</div>
            <div class="theme-title">AWS Acceleration & AI Demand</div>
            <div class="theme-body">Could AWS pick up speed again driven by AI? Investors wanted proof that spending on training, inference, custom chips (Trainium, Graviton), and Bedrock was translating into faster revenue growth against Microsoft and Google.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 02</div>
            <div class="theme-title">Heavy Capex & Profitability</div>
            <div class="theme-body">Record-level investments in data centers and chips raised concerns about near-term pressure on free cash flow — balanced against Amazon's proven ability to scale and deliver returns over time.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 03</div>
            <div class="theme-title">Retail Resilience & Advertising</div>
            <div class="theme-body">How well was core e-commerce holding up? Prime momentum, grocery, delivery speed, plus strong double-digit advertising growth as a buffer and growth engine.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- TSLA --------
    elif company == "TSLA":
        st.markdown('<p class="section-header">What the company does?</p>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>🚗 Electric Vehicles</h4>
                <p>Designs and sells EVs including the Model 3, Model Y, Cybertruck, and upcoming Cybercab and Semi.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>🔋 Energy Storage</h4>
                <p>Builds large-scale battery systems (Megapacks) that store solar and wind power for utilities and homes.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="info-card">
                <h4>🤖 AI & Robotics</h4>
                <p>Invests heavily in self-driving software (FSD), driverless Robotaxi fleets, and humanoid robots (Optimus).</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card" style="background:#f9fafb;">
            <p>Tesla designs, builds, and sells electric cars (like the Model 3 and Cybertruck), energy products (like giant battery systems called Megapacks that store solar or wind power), and software for self-driving. It also invests heavily in AI and robots.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market Was Discussing Before Earnings</p>', unsafe_allow_html=True)
        st.caption("Key themes investors focused on going into the print.")
        
        st.markdown("""
        <div class="theme-card">
            <div class="theme-tag">THEME 01</div>
            <div class="theme-title">Is EV Demand Finally Bouncing Back?</div>
            <div class="theme-body">Tesla's car sales had slowed due to high prices, rising competition (especially from China), and buyers waiting for cheaper models. Investors watched delivery numbers and order backlog closely — missed deliveries or bloated inventory would confirm the EV boom was cooling, while stronger orders would validate Tesla's pivot to affordability and software. With cars still the biggest revenue driver, this was the #1 short-term worry.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 02</div>
            <div class="theme-title">How Fast Is the AI & Robotaxi Story Moving?</div>
            <div class="theme-body">Many investors no longer view Tesla as just a car company — they care about FSD, driverless Robotaxi vans, and humanoid Optimus robots. The market wanted fresh proof of progress: regulatory approvals, test miles, and unsupervised Robotaxi launch timelines. Vague updates or pushed timelines could hit the stock hard given how much optimism was already priced in.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 03</div>
            <div class="theme-title">How Much Will Tesla Spend on the Future?</div>
            <div class="theme-body">Tesla had warned of heavy investment in new factories, AI compute, and battery materials. Analysts debated whether guidance would rise further. Bulls argued the capex was necessary to stay ahead in AI and robotics; bears feared extended cash burn would leave less for shareholders. The market was split — bullish long term but nervous near term.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- MSFT --------
    elif company == "MSFT":
        st.markdown('<p class="section-header">What the company does?</p>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>💻 Productivity Software</h4>
                <p>Windows, Microsoft 365 (Word, Excel, Teams), and LinkedIn — tools billions use every day at work and school.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>☁️ Azure Cloud</h4>
                <p>Microsoft's cloud platform for storing data and running apps — one of the world's largest, powered by AI.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="info-card">
                <h4>🤖 AI & Copilot</h4>
                <p>AI tools like Copilot built into apps, changing how people work, create, and solve problems.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card" style="background:#f9fafb;">
            <p>Microsoft builds the software and tools that billions of people and companies use every day — things like Windows on your computer, Microsoft 365 (Word, Excel, Teams) for work, Azure for storing data and running apps in the cloud, Xbox for gaming, and LinkedIn for jobs. It matters because almost every business on Earth relies on Microsoft's products to get work done, and the company is now leading the charge in artificial intelligence (AI) tools like Copilot that are changing how we work, create, and solve problems.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market Was Discussing Before Earnings</p>', unsafe_allow_html=True)
        st.caption("Key themes investors focused on going into the print.")
        
        st.markdown("""
        <div class="theme-card">
            <div class="theme-tag">THEME 01</div>
            <div class="theme-title">Would Azure Growth Keep Accelerating — Or Hit a Wall?</div>
            <div class="theme-body">Wall Street was laser-focused on Azure, expecting ~37–39% growth in constant currency. Investors wanted proof that AI-powered cloud demand was still strong, with some worried Microsoft lacked enough data-center capacity to meet orders. The Azure number was treated like a "report card" on Microsoft's AI bet — a beat would boost confidence, a miss could tank the stock.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 02</div>
            <div class="theme-title">How Fast Were AI Products Like Copilot Making Money?</div>
            <div class="theme-body">Investors wanted hard proof AI was paying off. How many companies were buying Copilot? Was AI revenue growing fast enough to justify huge spending on data centers? The AI run-rate (annualized AI revenue) was expected to be a headline — triple-digit growth would excite bulls, anything softer would confirm bearish "AI hype ahead of reality" fears.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 03</div>
            <div class="theme-title">Are the Giant AI Spending Bills Worth It?</div>
            <div class="theme-body">Microsoft had been pouring tens of billions into new data centers and AI chips. The debate: would this capex crush margins short term, and when would it boost the bottom line? Rising memory-chip prices made the bill look even bigger. Investors wanted clear 2026 spending guidance — too high a number could scare the market even if everything else looked great.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- NVDA --------
    elif company == "NVDA":
        st.markdown('<p class="section-header">What the company does?</p>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>🎮 GPUs for Gaming & AI</h4>
                <p>Designs super-powerful chips (GPUs) that power stunning graphics and train giant AI systems like ChatGPT.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>🏭 AI Factories</h4>
                <p>Sells full computer systems and networking gear used by big tech to build massive AI data centers.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="info-card">
                <h4>🧠 AI Software Platform</h4>
                <p>Software tools (CUDA, Omniverse) make NVIDIA the platform of choice for developers building AI applications.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card" style="background:#f9fafb;">
            <p>NVIDIA designs and sells super-powerful computer chips called GPUs that make video games look amazing and help train giant artificial intelligence (AI) systems that power things like ChatGPT or self-driving cars. It also sells complete computer systems, software, and networking gear that big tech companies use to build massive "AI factories" (data centers) where all the smart computing happens.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market Was Discussing Before Earnings</p>', unsafe_allow_html=True)
        st.caption("Key themes investors focused on going into the print.")
        
        st.markdown("""
        <div class="theme-card">
            <div class="theme-tag">THEME 01</div>
            <div class="theme-title">Huge Excitement About AI Demand & Blackwell Chips</div>
            <div class="theme-body">Investors were buzzing about the pace of NVIDIA chip buying. Big Tech (Microsoft, Google, Amazon) was spending billions on AI data centers, and the new "Blackwell" platform had orders lined up for months. The question: would the AI boom keep growing at crazy speeds, or slow down once the first wave of spending finished? Most expected another monster beat.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 02</div>
            <div class="theme-title">Was the Stock Getting Too Expensive?</div>
            <div class="theme-body">With NVIDIA worth over $3 trillion, many feared the price baked in perfect growth forever. What if AI spending slowed? What if customers couldn't make enough from AI to keep buying more chips? Competition from AMD and custom chips from cloud giants was also watched closely. Still, most Wall Street experts said "buy" — but the valuation debate was loud.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 03</div>
            <div class="theme-title">Supply Shortages & the China Ban</div>
            <div class="theme-body">Two practical risks: shortage of HBM memory chips could delay orders, and U.S. rules blocked NVIDIA's strongest AI chips from China (the company assumed zero China sales). Investors wanted to know if these limits would hurt growth, or if demand from the rest of the world was big enough to more than make up for it.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- TSM --------
    elif company == "TSM":
        st.markdown('<p class="section-header">What the company does?</p>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>🏭 Chip Manufacturing</h4>
                <p>Builds the world's most advanced semiconductors in giant factories — other companies design them, TSMC makes them.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>🤝 Top-Tier Customers</h4>
                <p>Apple, NVIDIA, AMD, and others rely on TSMC to produce the chips powering phones, PCs, cars, and AI servers.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="info-card">
                <h4>⚡ Cutting-Edge Tech</h4>
                <p>Leader in the smallest, most powerful chip nodes (3nm, 2nm) — critical to AI, high-end phones, and data centers.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card" style="background:#f9fafb;">
            <p>TSMC makes the super-small computer chips (called semiconductors) that power almost everything tech-related — your phone, laptops, cars, and especially the giant AI servers that run ChatGPT-style tools. Other companies like Apple, NVIDIA, and AMD design the chips, but TSMC actually builds them in its giant factories using the world's most advanced technology.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market Was Discussing Before Earnings</p>', unsafe_allow_html=True)
        st.caption("Key themes investors focused on going into the print.")
        
        st.markdown("""
        <div class="theme-card">
            <div class="theme-tag">THEME 01</div>
            <div class="theme-title">The AI Explosion Was Carrying Everything</div>
            <div class="theme-body">AI chips were on fire — NVIDIA and others were ordering huge amounts of TSMC's most cutting-edge nodes. The market wondered: how much would AI make up for slower phone and car sales? Another record quarter was expected, but the big question was whether TSMC could keep raising prices and running factories at full speed without disruption.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 02</div>
            <div class="theme-title">Geopolitical Worries in the Background</div>
            <div class="theme-body">Based in Taiwan, TSMC investors kept one eye on China-Taiwan tensions and broader global issues (like Middle East conflicts affecting shipping and energy costs). Most said "AI demand is so strong it probably won't matter short-term," but any supply-chain drama was the one thing that could spook the stock.</div>
        </div>
        <div class="theme-card">
            <div class="theme-tag">THEME 03</div>
            <div class="theme-title">Will Profits Stay Super High — Or Get Squeezed?</div>
            <div class="theme-body">Building new factories in the U.S. and Japan, plus ramping brand-new 2nm tech, costs a lot. Memory-chip shortages were also hurting phones. The debate: would AI keep profits sky-high, or would extra spending start eating into margins?</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Continue to Latest Earnings →", type="primary", use_container_width=True):
        st.session_state.stage = "earnings"
        st.rerun()

    if st.button("← Back to Companies"):
        st.session_state.stage = "company"
        st.rerun()

# ============================================================
# STAGE 4: Earnings + Questions
# ============================================================
elif st.session_state.stage == "earnings":
    company = st.session_state.company
    st.subheader(f"From the Earnings: {companies[company]['name']}")
    st.caption(companies[company]["earnings_date"])
    
    # -------- AMZN --------
    if company == "AMZN":
        st.markdown('<p class="section-header">Key Financial Metrics</p>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Net Sales</span>
                    <span class="metric-badge badge-green">+17% YoY</span>
                </div>
                <div class="metric-value">$181.5B</div>
                <div class="metric-desc">Total revenue across all businesses.</div>
                <div class="metric-note">Solid top-line growth from healthy retail unit gains and especially strong AWS momentum driven by AI demand.</div>
            </div>
            <div class="metric-card highlight">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">AWS Sales</span>
                    <span class="metric-badge badge-orange">+28% YoY 🔥</span>
                </div>
                <div class="metric-value">$37.6B</div>
                <div class="metric-desc">Cloud computing revenue.</div>
                <div class="metric-note">Acceleration powered by booming adoption of AI services, custom chips, and infrastructure offerings.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Capital Expenditure</span>
                    <span class="metric-badge badge-purple">Elevated</span>
                </div>
                <div class="metric-value">$43.2B</div>
                <div class="metric-desc">Investment in future capacity.</div>
                <div class="metric-note">Aligned with plans to aggressively build capacity in response to strong AI demand signals.</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Operating Income</span>
                    <span class="metric-badge badge-green">vs $18.4B</span>
                </div>
                <div class="metric-value">$23.9B</div>
                <div class="metric-desc">Core profit from operations.</div>
                <div class="metric-note">Reflects better cost management, higher-margin AWS and advertising contributions, and continued efficiencies.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Diluted EPS</span>
                    <span class="metric-badge badge-blue">Per Share</span>
                </div>
                <div class="metric-value">$2.78</div>
                <div class="metric-desc">Bottom-line profit per share.</div>
                <div class="metric-note">Strong result from robust operations plus one-time investment gains (e.g., stake in Anthropic).</div>
            </div>
            <div class="metric-card" style="background:linear-gradient(135deg,#1e293b,#0f172a); color:white; border:none;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label" style="color:#cbd5e1;">Q2 Guidance</span>
                    <span class="metric-badge" style="background:#f97316; color:white;">Outlook</span>
                </div>
                <div class="metric-value" style="color:white; font-size:1.2em;">$194B – $199B</div>
                <div class="metric-desc" style="color:#cbd5e1;">Net sales (≈16–19% growth)</div>
                <div class="metric-note" style="color:#e2e8f0;">Operating income guided to <b style="color:#fdba74;">$20B–$24B</b>. Management noted strong trends carrying into Q2.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What did Management Highlight in the Earnings Call?</p>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-ceo">AJ</div>
                    <div>
                        <div class="quote-name">Andy Jassy</div>
                        <div class="quote-role">Chief Executive Officer</div>
                    </div>
                </div>
                <div class="quote-text">"AWS is growing 28% year-over-year, the fastest growth rate in 15 quarters… We've never seen a technology grow as rapidly as AI."</div>
                <div class="quote-extra">Jassy described the current AI wave as <b>"some of the biggest inflections of our lifetime,"</b> remaining "very optimistic about what's ahead."</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-cfo">BO</div>
                    <div>
                        <div class="quote-name">Brian Olsavsky</div>
                        <div class="quote-role">Chief Financial Officer</div>
                    </div>
                </div>
                <div class="quote-text cfo">"We continue to see strong sales trends carrying into Q2."</div>
                <div class="quote-extra">Guided Q2 net sales to <b>$194B–$199B</b> and operating income to <b>$20B–$24B</b>, with context around Prime Day timing and a modest FX headwind.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="tone-banner">
            <b>Overall tone:</b> Confident and constructive — acknowledging continued heavy investment while emphasizing momentum in retail units, record margins, and AI leadership.
        </div>
        """, unsafe_allow_html=True)
    
    # -------- TSLA --------
    elif company == "TSLA":
        st.markdown('<p class="section-header">Key Financial Metrics</p>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Total Revenue</span>
                    <span class="metric-badge badge-green">+16% YoY</span>
                </div>
                <div class="metric-value">$22.4B</div>
                <div class="metric-desc">Money collected from cars, energy, services, and software.</div>
                <div class="metric-note">Healthy growth signaling recovery in demand after a weaker 2025, led by vehicle deliveries and fast-growing energy storage.</div>
            </div>
            <div class="metric-card highlight">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Gross Margin</span>
                    <span class="metric-badge badge-orange">21.1% 🔥</span>
                </div>
                <div class="metric-value">21.1%</div>
                <div class="metric-desc">vs 16.3% last year — a big jump.</div>
                <div class="metric-note">Reflects better cost control, manufacturing efficiency, and more favorable pricing — a key bright spot of the quarter.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Vehicle Deliveries</span>
                    <span class="metric-badge badge-blue">+6% YoY</span>
                </div>
                <div class="metric-value">358,023</div>
                <div class="metric-desc">Cars customers actually took home.</div>
                <div class="metric-note">Modest growth, but paired with the strongest Q1 order backlog in over two years — a sign demand is re-accelerating.</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Adjusted EPS</span>
                    <span class="metric-badge badge-green">+52% YoY</span>
                </div>
                <div class="metric-value">$0.41</div>
                <div class="metric-desc">Profit per share (beat estimates).</div>
                <div class="metric-note">Clean profit number investors watch most closely — strong beat driven by margin expansion and operational discipline.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Free Cash Flow</span>
                    <span class="metric-badge badge-green">+117% YoY</span>
                </div>
                <div class="metric-value">$1.4B</div>
                <div class="metric-desc">Cash left after paying for factories and equipment.</div>
                <div class="metric-note">Strong positive FCF this quarter — but management warned of negative FCF for the rest of 2026 as heavy spending ramps up.</div>
            </div>
            <div class="metric-card" style="background:linear-gradient(135deg,#1e293b,#0f172a); color:white; border:none;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label" style="color:#cbd5e1;">2026 Capex Guidance</span>
                    <span class="metric-badge" style="background:#dc2626; color:white;">Raised</span>
                </div>
                <div class="metric-value" style="color:white; font-size:1.3em;">$25B+</div>
                <div class="metric-desc" style="color:#cbd5e1;">Up ~$5B from prior guidance</div>
                <div class="metric-note" style="color:#e2e8f0;">Funds new AI factories, Robotaxi, Optimus, and battery plants. Expect <b style="color:#fca5a5;">negative FCF</b> for the remainder of 2026.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What did Management Highlight in the Earnings Call?</p>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-ceo">EM</div>
                    <div>
                        <div class="quote-name">Elon Musk</div>
                        <div class="quote-role">Chief Executive Officer</div>
                    </div>
                </div>
                <div class="quote-text">"We're going to be substantially increasing our investments in the future… well justified for a substantially increased future revenue stream."</div>
                <div class="quote-extra">Musk confirmed <b>unsupervised Robotaxi rides have started in Dallas and Houston</b>, and said Cybercab and Tesla Semi are on track for volume production later in 2026. Called the future <b>"incredibly bright."</b></div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-cfo">VT</div>
                    <div>
                        <div class="quote-name">Vaibhav Taneja</div>
                        <div class="quote-role">Chief Financial Officer</div>
                    </div>
                </div>
                <div class="quote-text cfo">"We saw continued growth in demand… rebound of demand in both EMEA and North America."</div>
                <div class="quote-extra">Highlighted the <b>highest Q1 order backlog in over two years</b>, but cautioned investors to expect <b>negative free cash flow</b> for the rest of 2026 due to a heavy "capital investment phase."</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="tone-banner">
            <b>Overall tone:</b> Excited and confident about AI/robotics becoming huge long term, but realistic that 2026 will be a heavy-investment year with short-term pain before the bigger payoff.
        </div>
        """, unsafe_allow_html=True)
    
    # -------- MSFT --------
    elif company == "MSFT":
        st.markdown('<p class="section-header">Key Financial Metrics</p>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Total Revenue</span>
                    <span class="metric-badge badge-green">+18% YoY</span>
                </div>
                <div class="metric-value">$82.9B</div>
                <div class="metric-desc">Total money from software, cloud, ads, games.</div>
                <div class="metric-note">Strong top-line growth led by cloud and AI momentum across all segments.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Diluted EPS</span>
                    <span class="metric-badge badge-blue">+23% YoY</span>
                </div>
                <div class="metric-value">$4.27</div>
                <div class="metric-desc">Profit per share after all expenses.</div>
                <div class="metric-note">Robust bottom-line growth outpaced revenue thanks to operating leverage and mix shift to high-margin cloud.</div>
            </div>
            <div class="metric-card highlight">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Azure Growth</span>
                    <span class="metric-badge badge-orange">+40% 🔥</span>
                </div>
                <div class="metric-value">+40%</div>
                <div class="metric-desc">Azure and other cloud services growth.</div>
                <div class="metric-note">Blew past analyst estimates of 37–39% — the clearest sign that AI-powered cloud demand is still accelerating.</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Microsoft Cloud Revenue</span>
                    <span class="metric-badge badge-green">+29% YoY</span>
                </div>
                <div class="metric-value">$54.5B</div>
                <div class="metric-desc">Azure + other online services revenue.</div>
                <div class="metric-note">Microsoft's fastest-growing and most important area — businesses keep renting software instead of buying it outright.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">AI Annual Run-Rate</span>
                    <span class="metric-badge badge-green">+123% YoY</span>
                </div>
                <div class="metric-value">$37B+</div>
                <div class="metric-desc">Current annualized speed of AI revenue.</div>
                <div class="metric-note">Shows Copilot and AI services are exploding — a headline number bulls celebrated as proof the AI bet is working.</div>
            </div>
            <div class="metric-card" style="background:linear-gradient(135deg,#1e293b,#0f172a); color:white; border:none;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label" style="color:#cbd5e1;">FY2026 Capex Guidance</span>
                    <span class="metric-badge" style="background:#dc2626; color:white;">Raised</span>
                </div>
                <div class="metric-value" style="color:white; font-size:1.3em;">~$190B</div>
                <div class="metric-desc" style="color:#cbd5e1;">Above analyst expectations</div>
                <div class="metric-note" style="color:#e2e8f0;">Higher than expected due to <b style="color:#fca5a5;">rising memory-chip prices</b>. The spending surprise drove the post-earnings drop.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What did Management Highlight in the Earnings Call?</p>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-ceo">SN</div>
                    <div>
                        <div class="quote-name">Satya Nadella</div>
                        <div class="quote-role">Chief Executive Officer</div>
                    </div>
                </div>
                <div class="quote-text">"It was a record third quarter, powered by the continued strength of the Microsoft Cloud… our AI business annual revenue run rate surpassed $37 billion this quarter, growing 123% year-over-year."</div>
                <div class="quote-extra">Nadella talked about AI "agents" becoming normal coworkers and said demand is so strong that <b>Azure growth will actually accelerate in the second half of 2026</b>.</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-cfo">AH</div>
                    <div>
                        <div class="quote-name">Amy Hood</div>
                        <div class="quote-role">Chief Financial Officer</div>
                    </div>
                </div>
                <div class="quote-text cfo">"We feel good about working through physical limitations and the ROI on our investments."</div>
                <div class="quote-extra">Guided Q4 revenue to <b>$86.7–$87.8B</b>, Azure growth to <b>39–40%</b>, and full-year capex ~<b>$190B</b>. Said FY2027 should still deliver double-digit revenue and operating-income growth.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="tone-banner">
            <b>Overall tone:</b> Confident and upbeat — Nadella framed this as a platform-shift moment for AI, while Hood acknowledged higher spending but stood firmly behind long-term ROI and double-digit growth in FY2027.
        </div>
        """, unsafe_allow_html=True)
    
    # -------- NVDA --------
    elif company == "NVDA":
        st.markdown('<p class="section-header">Key Financial Metrics</p>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Total Revenue</span>
                    <span class="metric-badge badge-green">+73% YoY</span>
                </div>
                <div class="metric-value">$68.1B</div>
                <div class="metric-desc">Total Q4 sales from chips, systems, and software.</div>
                <div class="metric-note">Yet another record — top-line growth stayed explosive as AI data center demand showed no signs of slowing.</div>
            </div>
            <div class="metric-card highlight">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Data Center Revenue</span>
                    <span class="metric-badge badge-orange">+75% YoY 🔥</span>
                </div>
                <div class="metric-value">$62.3B</div>
                <div class="metric-desc">Sales to AI/cloud customers (>90% of revenue).</div>
                <div class="metric-note">The engine of the business — growth came from Blackwell ramp and massive cloud hyperscaler spending on AI infrastructure.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Full-Year FY26 Revenue</span>
                    <span class="metric-badge badge-green">+65% YoY</span>
                </div>
                <div class="metric-value">$215.9B</div>
                <div class="metric-desc">Total for the whole fiscal year.</div>
                <div class="metric-note">A record year that turned the AI boom into sustained, massive annual revenue — not just a quarterly spike.</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Non-GAAP EPS</span>
                    <span class="metric-badge badge-green">+82% YoY</span>
                </div>
                <div class="metric-value">$1.62</div>
                <div class="metric-desc">Profit per share, adjusted (beat estimates).</div>
                <div class="metric-note">Easily beat Wall Street expectations thanks to strong pricing and scale.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Non-GAAP Gross Margin</span>
                    <span class="metric-badge badge-blue">Elite</span>
                </div>
                <div class="metric-value">75.2%</div>
                <div class="metric-desc">Profit kept per dollar of sales.</div>
                <div class="metric-note">Stayed near industry-leading levels even through fast Blackwell ramp — a big signal of pricing power.</div>
            </div>
            <div class="metric-card" style="background:linear-gradient(135deg,#064e3b,#0f172a); color:white; border:none;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label" style="color:#cbd5e1;">Next Quarter Guidance</span>
                    <span class="metric-badge" style="background:#10b981; color:white;">Beat Est.</span>
                </div>
                <div class="metric-value" style="color:white; font-size:1.3em;">$78B ± 2%</div>
                <div class="metric-desc" style="color:#cbd5e1;">Above Wall Street consensus</div>
                <div class="metric-note" style="color:#e2e8f0;">Management expects <b style="color:#6ee7b7;">sequential growth throughout calendar 2026</b>, exceeding the $500B Blackwell/Rubin opportunity shared earlier.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What did Management Highlight in the Earnings Call?</p>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-ceo">JH</div>
                    <div>
                        <div class="quote-name">Jensen Huang</div>
                        <div class="quote-role">Chief Executive Officer</div>
                    </div>
                </div>
                <div class="quote-text">"The agentic AI inflection point has arrived… enterprise adoption of agents is skyrocketing."</div>
                <div class="quote-extra">Huang said new platforms like <b>Vera Rubin are already shipping samples</b>, and noted the company has <b>supply locked in through 2027</b>.</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-cfo">CK</div>
                    <div>
                        <div class="quote-name">Colette Kress</div>
                        <div class="quote-role">Chief Financial Officer</div>
                    </div>
                </div>
                <div class="quote-text cfo">"Total revenue is expected to be $78 billion, plus or minus 2%."</div>
                <div class="quote-extra">Guided to <b>sequential revenue growth throughout calendar 2026</b>, exceeding the $500B Blackwell and Rubin revenue opportunity shared last year.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="tone-banner">
            <b>Overall tone:</b> Confident and forward-looking — management was excited about AI demand staying strong, new products (Blackwell, Rubin) ramping, and customers racing to build more AI systems. No worries about a slowdown.
        </div>
        """, unsafe_allow_html=True)
    
    # -------- TSM --------
    elif company == "TSM":
        st.markdown('<p class="section-header">Key Financial Metrics</p>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Total Revenue</span>
                    <span class="metric-badge badge-green">+6.4% QoQ</span>
                </div>
                <div class="metric-value">$35.9B</div>
                <div class="metric-desc">Total money from manufacturing chips.</div>
                <div class="metric-note">A huge YoY jump — AI demand drove another record quarter as hyperscalers and NVIDIA ordered more leading-edge wafers.</div>
            </div>
            <div class="metric-card highlight">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Gross Margin</span>
                    <span class="metric-badge badge-orange">Record 🔥</span>
                </div>
                <div class="metric-value">66.2%</div>
                <div class="metric-desc">Profit kept after making the chips.</div>
                <div class="metric-note">A new record and above guidance — powerful evidence of pricing leverage from AI demand and advanced-node mix.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Operating Margin</span>
                    <span class="metric-badge badge-blue">Beat Est.</span>
                </div>
                <div class="metric-value">58.1%</div>
                <div class="metric-desc">Profit after all factory operating costs.</div>
                <div class="metric-note">Strong result from high factory utilization and operational excellence — proving scale advantages.</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">EPS (per ADR)</span>
                    <span class="metric-badge badge-green">Beat Est.</span>
                </div>
                <div class="metric-value">$3.49</div>
                <div class="metric-desc">Profit for each share an investor owns.</div>
                <div class="metric-note">Beat Wall Street's estimate of ~$3.31 — another clean quarter of execution.</div>
            </div>
            <div class="metric-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label">Advanced Tech (≤7nm)</span>
                    <span class="metric-badge badge-purple">74% of wafers</span>
                </div>
                <div class="metric-value">74%</div>
                <div class="metric-desc">Share from newest, most powerful chips (3nm = 25%).</div>
                <div class="metric-note">Proof that AI and high-end phones are driving growth at TSMC's most profitable leading-edge nodes.</div>
            </div>
            <div class="metric-card" style="background:linear-gradient(135deg,#064e3b,#0f172a); color:white; border:none;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="metric-label" style="color:#cbd5e1;">2026 Revenue Guidance</span>
                    <span class="metric-badge" style="background:#10b981; color:white;">Raised</span>
                </div>
                <div class="metric-value" style="color:white; font-size:1.3em;">>30% Growth</div>
                <div class="metric-desc" style="color:#cbd5e1;">Raised from "close to 30%"</div>
                <div class="metric-note" style="color:#e2e8f0;">Q2 revenue guided to <b style="color:#6ee7b7;">$39.0–$40.2B</b>. Capex toward high end of <b>$52–56B</b> to build AI capacity.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What did Management Highlight in the Earnings Call?</p>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-ceo">CW</div>
                    <div>
                        <div class="quote-name">C.C. Wei</div>
                        <div class="quote-role">Chief Executive Officer</div>
                    </div>
                </div>
                <div class="quote-text">"AI-related demand continues to be extremely robust."</div>
                <div class="quote-extra">Wei talked about AI moving from "ask me questions" to "do stuff for you" (<b>agentic AI</b>), meaning even more compute and chips needed. Cited tech leadership and broad customer base as sources of "strong confidence."</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="quote-card">
                <div class="quote-header">
                    <div class="avatar avatar-cfo">WH</div>
                    <div>
                        <div class="quote-name">Wendell Huang</div>
                        <div class="quote-role">Chief Financial Officer</div>
                    </div>
                </div>
                <div class="quote-text cfo">"We are prudently managing through macro uncertainties while investing for the long-term AI opportunity."</div>
                <div class="quote-extra">Guided Q2 revenue to <b>$39.0–$40.2B</b>, raised full-year 2026 growth to <b>above 30%</b>, and committed to capex at the high end of <b>$52–56B</b> to support AI capacity buildout.</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="tone-banner">
            <b>Overall tone:</b> Super positive on the multi-year AI trend, confident on demand and tech leadership — while staying "prudent" about macro uncertainties like rising component prices and geopolitical events.
        </div>
        """, unsafe_allow_html=True)
    
    # -------- Questions (shared) --------
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

# ============================================================
# STAGE 5: Analysis
# ============================================================
elif st.session_state.stage == "analysis":
    company = st.session_state.company
    st.subheader(f"Analysis — {companies[company]['name']}")
    
    # -------- AMZN --------
    if company == "AMZN":
        st.markdown('<p class="section-header">How did the Price Move after Earnings?</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="timeline-item">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">29</div>
                <div class="timeline-change change-down">−0.8% to −3%</div>
            </div>
            <div>
                <div class="timeline-title">After-hours — Initial Dip</div>
                <div class="timeline-desc">Stock traded down despite the beats. Early reaction tied to the high capex figure and concerns about near-term margin pressure from ongoing AI infrastructure builds.</div>
            </div>
        </div>
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">30</div>
                <div class="timeline-change change-up">+0.8% to +1.3%</div>
            </div>
            <div>
                <div class="timeline-title">Next Day — Recovery</div>
                <div class="timeline-desc">Shares recovered to close modestly higher after the call. Jassy's bullish AI commentary and AWS acceleration shifted sentiment toward longer-term opportunities.</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">
                <div class="timeline-month">MAY</div>
                <div class="timeline-day">1w</div>
                <div class="timeline-change change-up">+1% to +2%</div>
            </div>
            <div>
                <div class="timeline-title">First Week — Modest Gains</div>
                <div class="timeline-desc">Trading in the <b>$265–$273</b> range. Positive analyst commentary on record margins, backlog strength, and AI re-rating supported the move — though reaction stayed muted as the market digested capex scale.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market is Discussing Now</p>', unsafe_allow_html=True)
        st.caption("One week after the print — where the conversation has shifted.")
        st.markdown("""
        <div class="theme-card" style="border-left-color:#f97316;">
            <div class="theme-tag">TOPIC 01</div>
            <div class="theme-title">AWS Momentum & AI Monetization</div>
            <div class="theme-body">Can Amazon build on the 28% AWS growth rate? Investors point to sold-out Trainium chips, deals with OpenAI and Anthropic, and a <b>$150B annualized run rate</b> as evidence the AI inflection is real. Analysts are raising estimates, though many want clearer proof of accelerating high-margin revenue.</div>
        </div>
        <div class="theme-card" style="border-left-color:#2563eb;">
            <div class="theme-tag" style="color:#1d4ed8;">TOPIC 02</div>
            <div class="theme-title">Sustainability of Heavy Capex & Free Cash Flow</div>
            <div class="theme-body">Full-year 2026 capex is expected around <b>$200 billion</b>. The market is weighing near-term pressure on FCF and margins against eventual payoff in <b>2027–2028</b> as new capacity comes online — watching closely for execution risk or slower utilization.</div>
        </div>
        <div class="theme-card" style="border-left-color:#059669;">
            <div class="theme-tag" style="color:#047857;">TOPIC 03</div>
            <div class="theme-title">Retail Strength, Ads & Valuation Re-rating</div>
            <div class="theme-body">Strong unit sales, Prime momentum, grocery gains, and advertising partnerships support resilience. With multiple analyst upgrades pushing price targets toward <b>$310–$315</b>, the debate is how much of a valuation premium AMZN deserves given its AI leadership and diversified growth.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- TSLA --------
    elif company == "TSLA":
        st.markdown('<p class="section-header">How did the Price Move after Earnings?</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">22</div>
                <div class="timeline-change change-up">+4%</div>
            </div>
            <div>
                <div class="timeline-title">After-hours — Initial Pop</div>
                <div class="timeline-desc">Stock jumped ~4% in extended trading right after the release. Investors cheered the profit beat, big margin improvement, and positive demand commentary.</div>
            </div>
        </div>
        <div class="timeline-item down">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">23</div>
                <div class="timeline-change change-down">−3.6%</div>
            </div>
            <div>
                <div class="timeline-title">Next Day — Sharp Reversal</div>
                <div class="timeline-desc">Closed around <b>$374</b> after management unveiled the raised <b>$25B+ capex plan</b> and warned of negative free cash flow. Investors got nervous about cash burn and delayed profits from Robotaxi/Optimus.</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">End</div>
                <div class="timeline-change change-up">≈ Flat</div>
            </div>
            <div>
                <div class="timeline-title">Late April — Stabilization</div>
                <div class="timeline-desc">Stock bounced around but stayed roughly flat to slightly up from the post-earnings low. Sentiment shifted back toward "long-term AI bet is worth it," with analysts highlighting strong margins and Robotaxi progress.</div>
            </div>
        </div>
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">MAY</div>
                <div class="timeline-day">2w</div>
                <div class="timeline-change change-up">Recovered</div>
            </div>
            <div>
                <div class="timeline-title">Two Weeks Later — High $380s</div>
                <div class="timeline-desc">Stock recovered most of the immediate drop, trading in the <b>high $380s</b> — still below pre-earnings levels but showing the market has shifted focus to execution rather than panic.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market is Discussing Now</p>', unsafe_allow_html=True)
        st.caption("Two weeks after the print — where the conversation has shifted.")
        st.markdown("""
        <div class="theme-card" style="border-left-color:#dc2626;">
            <div class="theme-tag" style="color:#b91c1c;">TOPIC 01</div>
            <div class="theme-title">Can Tesla Afford the Giant Spending Spree?</div>
            <div class="theme-body">The $25B+ capex figure and warning of negative FCF for the rest of 2026 surprised investors. The debate: is this "investment phase" smart or too aggressive? Bulls cite improving margins and AI/robotics upside by <b>2027–2028</b>; bears worry it pressures the stock if Robotaxi takes longer than hoped.</div>
        </div>
        <div class="theme-card" style="border-left-color:#f97316;">
            <div class="theme-tag">TOPIC 02</div>
            <div class="theme-title">Is the AI/Robotics Pivot Real Enough for the Valuation?</div>
            <div class="theme-body">With car demand only modestly up and competition fierce, the conversation has shifted even more toward FSD, Robotaxi expansion (already live in <b>Dallas and Houston</b>), and Optimus. Management gave concrete progress examples, but many investors still want proof these will become big businesses soon — not just promises.</div>
        </div>
        <div class="theme-card" style="border-left-color:#059669;">
            <div class="theme-tag" style="color:#047857;">TOPIC 03</div>
            <div class="theme-title">Will Higher Margins & Regional Demand Hold Up?</div>
            <div class="theme-body">The jump to <b>21.1% gross margin</b> and rebound in European and Asian orders were bright spots. Investors ask whether these improvements can offset heavy spending on future projects. The real test: can full-year 2026 deliveries grow meaningfully while Tesla invests so aggressively?</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- MSFT --------
    elif company == "MSFT":
        st.markdown('<p class="section-header">How did the Price Move after Earnings?</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="timeline-item down">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">30</div>
                <div class="timeline-change change-down">−3.9%</div>
            </div>
            <div>
                <div class="timeline-title">Next Day — Sharp Drop</div>
                <div class="timeline-desc">Closed at <b>$407.78</b> (from $424.46). The market ignored the revenue and Azure beats, zeroing in on the <b>$190B capex guidance</b> — investors worried the spending bill was bigger and faster than expected.</div>
            </div>
        </div>
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">MAY</div>
                <div class="timeline-day">1</div>
                <div class="timeline-change change-up">+1.6%</div>
            </div>
            <div>
                <div class="timeline-title">Next Session — Partial Recovery</div>
                <div class="timeline-desc">Rebounded to <b>$414.44</b>. Some analysts called the drop an overreaction and pointed to accelerating AI and cloud numbers as proof the long-term story is still strong.</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">
                <div class="timeline-month">MAY</div>
                <div class="timeline-day">1w</div>
                <div class="timeline-change change-down">~ −3%</div>
            </div>
            <div>
                <div class="timeline-title">One Week Later — Hovering</div>
                <div class="timeline-desc">Stock traded around <b>$411–$413</b>, still down ~3% from pre-earnings. Volume calmed down. Analysts remained mostly bullish (avg price target <b>$560–$576</b>, implying 35–40% upside) — noting MSFT now trades at a "multi-year low" valuation relative to its growth.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market is Discussing Now</p>', unsafe_allow_html=True)
        st.caption("One week after the print — where the conversation has shifted.")
        st.markdown("""
        <div class="theme-card" style="border-left-color:#dc2626;">
            <div class="theme-tag" style="color:#b91c1c;">TOPIC 01</div>
            <div class="theme-title">Will the $190B Capex Bill Pay Off Soon?</div>
            <div class="theme-body">Investors debate whether the massive data-center and AI-chip spending will boost profits this year — or keep pressuring margins for longer. The <b>$25B surprise from memory chips</b> was the real shock; bulls point to record Azure growth as proof the investments are already working. The question has shifted from "will they spend too much?" to "when do we see the return?"</div>
        </div>
        <div class="theme-card" style="border-left-color:#f97316;">
            <div class="theme-tag">TOPIC 02</div>
            <div class="theme-title">AI Agents & Copilot — Is This the Turning Point?</div>
            <div class="theme-body">With <b>Copilot seats up 250%</b> and AI run-rate over $37B, analysts are excited that "agentic AI" is moving from hype to real customer spending. The market now watches how fast companies adopt these tools and whether usage-based pricing will make revenue more predictable. Bulls say this validates Nadella's platform-shift thesis; skeptics want more quarters of data.</div>
        </div>
        <div class="theme-card" style="border-left-color:#059669;">
            <div class="theme-tag" style="color:#047857;">TOPIC 03</div>
            <div class="theme-title">Is MSFT Now a Bargain After the Dip?</div>
            <div class="theme-body">After the 4% drop, many analysts say Microsoft is trading at its cheapest valuation in years relative to its growth and <b>$627B backlog</b>. The debate: was the sell-off an overreaction driven by short-term capex fears, or does higher-for-longer spending really change the math? Wall Street's average target still points to big upside, and some big investors are calling the dip a "buying opportunity."</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- NVDA --------
    elif company == "NVDA":
        st.markdown('<p class="section-header">How did the Price Move after Earnings?</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">FEB</div>
                <div class="timeline-day">25</div>
                <div class="timeline-change change-up">+2%</div>
            </div>
            <div>
                <div class="timeline-title">After-hours — Initial Pop</div>
                <div class="timeline-desc">Rose about 2% right after the report. The revenue beat and strong <b>$78B guidance</b> beat expectations — investors cheered at first.</div>
            </div>
        </div>
        <div class="timeline-item down">
            <div class="timeline-date">
                <div class="timeline-month">FEB</div>
                <div class="timeline-day">26</div>
                <div class="timeline-change change-down">−5%</div>
            </div>
            <div>
                <div class="timeline-title">Next Day — Sell the News</div>
                <div class="timeline-desc">Fell roughly 5% (closed around <b>$186</b>). Even though results were great, the bar was so high that a huge beat still felt like "not enough." Worries about AI monetization and long-term spending popped up again.</div>
            </div>
        </div>
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">L</div>
                <div class="timeline-change change-up">All-Time High</div>
            </div>
            <div>
                <div class="timeline-title">Late April — Fresh Peak Near $216</div>
                <div class="timeline-desc">Stock recovered and climbed to an all-time high near <b>$216</b>. Positive news on Blackwell shipments, agentic AI demos, and Vera Rubin progress lifted sentiment.</div>
            </div>
        </div>
        <div class="timeline-item down">
            <div class="timeline-date">
                <div class="timeline-month">MAY</div>
                <div class="timeline-day">1w</div>
                <div class="timeline-change change-down">~ −7%</div>
            </div>
            <div>
                <div class="timeline-title">Early May — Mild Pullback</div>
                <div class="timeline-desc">Pulled back to the <b>$196–$207</b> range. A "sector rotation" moved money from NVDA to suppliers like Micron (memory) and optics companies as AI data centers now face shortages in those parts, not just GPUs.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market is Discussing Now</p>', unsafe_allow_html=True)
        st.caption("Two-plus months after the print — where the conversation has shifted.")
        st.markdown("""
        <div class="theme-card" style="border-left-color:#f97316;">
            <div class="theme-tag">TOPIC 01</div>
            <div class="theme-title">Shift to the Rest of the AI Supply Chain</div>
            <div class="theme-body">Investors are talking about bottlenecks beyond GPUs. <b>HBM memory and fast optical connections</b> are in short supply, driving big gains in names like Micron and Lumentum while NVIDIA has dipped. Analysts call this healthy — proof the AI build-out is real and spreading. NVDA is still the leader, but these shortages could slow how fast new AI factories come online.</div>
        </div>
        <div class="theme-card" style="border-left-color:#dc2626;">
            <div class="theme-tag" style="color:#b91c1c;">TOPIC 02</div>
            <div class="theme-title">When Will AI Actually Make Money?</div>
            <div class="theme-body">Even after strong results, some investors ask: when will big companies earn real profits from all this AI spending? Hyperscalers are spending billions, but <b>token prices are falling</b> and cash-flow worries remain. The market wants proof huge investments will pay off soon. Management keeps saying demand is "exponential" — Wall Street wants signals growth stays super-strong into 2027+.</div>
        </div>
        <div class="theme-card" style="border-left-color:#059669;">
            <div class="theme-tag" style="color:#047857;">TOPIC 03</div>
            <div class="theme-title">Excitement for Next Earnings & New Products</div>
            <div class="theme-body">Everyone is looking forward to the <b>May 20 Q1 2027 print</b> and GTC updates on Vera Rubin. Investors want to see how fast Blackwell is ramping and whether Rubin will keep NVIDIA ahead. Other tailwinds: "sovereign AI" (countries building their own systems) and fast enterprise AI agent adoption. Tone is mostly positive — but the stock has been volatile and needs more sequential growth and clear supply updates.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- TSM --------
    elif company == "TSM":
        st.markdown('<p class="section-header">How did the Price Move after Earnings?</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="timeline-item down">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">17</div>
                <div class="timeline-change change-down">−3.1%</div>
            </div>
            <div>
                <div class="timeline-title">Next Day — Classic "Sell the News"</div>
                <div class="timeline-desc">Stock fell ~3.1% (options had priced in a ±4.7% move). Even though results beat expectations, investors locked in profits after a big run-up, and the <b>higher capex number</b> raised short-term cash-flow worries.</div>
            </div>
        </div>
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">APR</div>
                <div class="timeline-day">2w</div>
                <div class="timeline-change change-up">New Highs</div>
            </div>
            <div>
                <div class="timeline-title">Next 1–2 Weeks — Strong Recovery</div>
                <div class="timeline-desc">Stock recovered and hit new highs. The CEO's strong AI comments and <b>raised full-year guidance</b> convinced investors the long-term story was even better than expected.</div>
            </div>
        </div>
        <div class="timeline-item up">
            <div class="timeline-date">
                <div class="timeline-month">MAY</div>
                <div class="timeline-day">3w</div>
                <div class="timeline-change change-up">Above Pre-Earnings</div>
            </div>
            <div>
                <div class="timeline-title">Early May — Meaningfully Higher</div>
                <div class="timeline-desc">Shares were trading meaningfully above pre-earnings levels. The market shifted from <b>"wait, is this too expensive?"</b> to <b>"AI demand is real and growing faster."</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-header">What the Market is Discussing Now</p>', unsafe_allow_html=True)
        st.caption("Three weeks after the print — where the conversation has shifted.")
        st.markdown("""
        <div class="theme-card" style="border-left-color:#059669;">
            <div class="theme-tag" style="color:#047857;">TOPIC 01</div>
            <div class="theme-title">AI Demand Is Even Stronger Than We Thought</div>
            <div class="theme-body">Analysts say the AI boom just stepped up another level thanks to new kinds of AI (<b>agentic/command-and-action</b>). TSMC's raised full-year guidance and record margins proved the megatrend is real and accelerating. People are calling it a <b>multi-year growth story still in early days</b>.</div>
        </div>
        <div class="theme-card" style="border-left-color:#f97316;">
            <div class="theme-tag">TOPIC 02</div>
            <div class="theme-title">Higher Spending Is the Price of Staying #1</div>
            <div class="theme-body">TSMC is spending huge amounts on new factories and 2nm tech — but investors now see it as <b>necessary</b> to keep up with NVIDIA, Apple, and others. Some worried about short-term margin dilution, but the stock rebound shows most view it as smart long-term investment.</div>
        </div>
        <div class="theme-card" style="border-left-color:#2563eb;">
            <div class="theme-tag" style="color:#1d4ed8;">TOPIC 03</div>
            <div class="theme-title">Geopolitics & Macro Risks Still There — But AI Wins</div>
            <div class="theme-body">The same Taiwan and global concerns remain, but the earnings beat and confident tone redirected focus to fundamentals. Analysts are mostly raising price targets and calling any dip a buying opportunity. The market sees TSMC as the <b>must-own AI infrastructure play</b>.</div>
        </div>
        """, unsafe_allow_html=True)
    
    # -------- User predictions recap (shared) --------
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("**Your Predictions**")
    q1, q2, q3, reason = st.session_state.answers
    st.write(f"**1. Beat Expectations:** {q1}")
    st.write(f"**2. Management Tone:** {q2}")
    st.write(f"**3. Price Movement:** {q3}")
    if reason:
        st.info(f"**Your Reasoning:** {reason}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Try Another Company", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ["stage"]:
                del st.session_state[key]
        st.session_state.stage = "industry"
        st.rerun()

st.markdown("---")
st.caption("Earnings Buddy • Informational Purpose Only • Not Investment Advice")