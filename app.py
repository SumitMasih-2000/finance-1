"""
FinanceIQ — Personal Finance Assistant
Run  :  streamlit run app.py
Deps :  pip install streamlit pandas matplotlib numpy
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import html as _html

# ═══════════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="FinanceIQ",
    page_icon="₹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════════
#  DESIGN TOKENS
# ═══════════════════════════════════════════════════════════════════
N     = "#0D1B2A"   # navy (primary)
N2    = "#1B2E44"   # navy hover
GOLD  = "#E8A000"   # gold accent
GOLD2 = "#F5C842"   # gold light
SAGE  = "#4E9B7E"   # sage green (positive)
RED   = "#B91C1C"   # red (warning)
CREAM = "#F8F7F4"   # background
WHITE = "#FFFFFF"   # card background
TEXT  = "#1A1A2E"   # body text
MUTED = "#64748B"   # muted text
BORD  = "#E4E8EE"   # border

CPAL  = [N, GOLD, SAGE, RED, "#7C3AED", "#0891B2", "#D97706"]

# ═══════════════════════════════════════════════════════════════════
#  GLOBAL CSS
# ═══════════════════════════════════════════════════════════════════
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Reset ── */
*, body {{ font-family: 'Inter', sans-serif; color: {TEXT}; }}
[data-testid="stAppViewContainer"] {{ background: {CREAM}; }}
[data-testid="block-container"] {{ padding-top: 1.8rem; padding-bottom: 3rem; }}
footer {{ display: none; }}
div[data-baseweb="notification"] {{ display: none; }}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{ background: {N} !important; }}
[data-testid="stSidebar"] * {{ color: #B8CAD9 !important; }}
[data-testid="stSidebar"] hr {{ border-color: #1E3650 !important; }}
[data-testid="stSidebar"] .stRadio [role="radiogroup"] label p {{
    font-size: 0.875rem !important;
    font-family: 'Inter', sans-serif !important;
}}

/* ── Metric Cards ── */
div[data-testid="metric-container"] {{
    background: {WHITE};
    border-radius: 10px;
    padding: 20px 18px;
    border-left: 4px solid {GOLD};
    box-shadow: 0 1px 5px rgba(13,27,42,0.06);
}}
div[data-testid="metric-container"] label {{
    font-size: 0.71rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: {MUTED} !important;
}}
[data-testid="stMetricValue"] > div {{
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.55rem !important;
    font-weight: 700 !important;
    color: {N} !important;
}}
[data-testid="stMetricDelta"] {{
    font-size: 0.78rem !important;
    color: {SAGE} !important;
}}

/* ── Typography ── */
h1, h2, h3, h4 {{ font-family: 'Space Grotesk', sans-serif !important; color: {N}; }}

/* ── Progress ── */
.stProgress > div > div > div > div {{ background: {GOLD} !important; }}

/* ── Buttons ── */
.stButton > button {{
    background: {N} !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.025em !important;
    padding: 0.5rem 1.4rem !important;
    transition: background .15s !important;
}}
.stButton > button:hover {{ background: {N2} !important; }}

/* ── Inputs ── */
.stNumberInput input, .stTextArea textarea, .stTextInput input, .stSelectbox div {{
    border-radius: 7px !important;
    border: 1.5px solid {BORD} !important;
    font-family: 'Inter', sans-serif !important;
}}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {{ border-bottom: 2px solid {BORD}; gap: 0; }}
.stTabs [data-baseweb="tab"] {{
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.87rem !important;
    font-weight: 500 !important;
    padding: 8px 20px;
    color: {MUTED} !important;
    border-radius: 0 !important;
}}
.stTabs [aria-selected="true"] {{
    color: {N} !important;
    border-bottom: 2px solid {GOLD} !important;
    font-weight: 700 !important;
}}

/* ── Expanders ── */
.stExpander {{ border: 1px solid {BORD} !important; border-radius: 10px !important; }}
.stExpander summary {{ font-family: 'Space Grotesk', sans-serif !important; font-weight: 600 !important; }}

/* ── DataFrames ── */
.stDataFrame {{ border-radius: 10px !important; overflow: hidden; }}

/* ── Custom HTML helpers ── */
.eyebrow {{
    font-size: 0.67rem; font-weight: 700;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: {GOLD}; margin-bottom: 2px;
}}
.page-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.65rem; font-weight: 700; color: {N};
    margin-bottom: 0.05rem;
}}
.page-sub {{ font-size: 0.9rem; color: {MUTED}; margin-bottom: 1.5rem; line-height: 1.5; }}
.card {{
    background: {WHITE}; border-radius: 12px;
    padding: 20px 22px; border: 1px solid {BORD};
    box-shadow: 0 1px 5px rgba(13,27,42,.05); margin-bottom: 14px;
}}
.card-gold {{ border-left: 4px solid {GOLD}; }}
.dark-banner {{ background: {N}; border-radius: 12px; padding: 20px 24px; margin-bottom: 16px; }}
.dark-banner p {{ color: #B8CAD9; font-size: 0.9rem; line-height: 1.65; margin: 0; }}
.dark-banner strong {{ color: {GOLD2}; }}
.principle-row {{ display: flex; align-items: flex-start; gap: 12px; padding: 11px 0; border-bottom: 1px solid {BORD}; }}
.principle-icon {{ font-size: 1.05rem; padding-top: 1px; flex-shrink: 0; }}
.principle-body {{ font-size: 0.9rem; line-height: 1.55; color: {TEXT}; }}
.principle-body b {{ color: {N}; }}
.chat-bubble-user {{
    background: {N}; color: #FAFAF8; padding: 10px 14px;
    border-radius: 10px 10px 3px 10px; margin: 6px 0 6px 16%; font-size: 0.86rem; line-height: 1.55;
}}
.chat-bubble-ai {{
    background: {WHITE}; color: {TEXT}; border: 1px solid {BORD}; border-left: 3px solid {GOLD};
    padding: 10px 14px; border-radius: 10px 10px 10px 3px; margin: 6px 16% 6px 0; font-size: 0.86rem; line-height: 1.65;
    white-space: pre-wrap;
}}
.chat-wrap {{ max-height: 350px; overflow-y: auto; background: {CREAM}; border-radius: 10px; padding: 8px; margin-bottom: 10px; }}
.score-circle {{
    display: flex; align-items: center; justify-content: center; width: 128px; height: 128px;
    border-radius: 50%; font-family: 'Space Grotesk', sans-serif; font-size: 2.8rem; font-weight: 700; border-width: 7px;
    border-style: solid; margin: 0 auto 12px;
}}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════
if "qa_log" not in st.session_state:
    st.session_state.qa_log = []

# ═══════════════════════════════════════════════════════════════════
#  CHART HELPERS
# ═══════════════════════════════════════════════════════════════════
def new_fig(w=6.0, h=4.5):
    fig, ax = plt.subplots(figsize=(w, h), facecolor=WHITE)
    ax.set_facecolor(WHITE)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(BORD)
    ax.spines["bottom"].set_color(BORD)
    ax.tick_params(colors=MUTED, labelsize=8)
    return fig, ax

def pie_fig(values, labels, colors=None, w=5.5, h=5.0):
    colors = colors or CPAL
    fig, ax = plt.subplots(figsize=(w, h), facecolor=WHITE)
    wedge_props = {"linewidth": 2.5, "edgecolor": WHITE}
    ax.pie(values, labels=labels, colors=colors,
           autopct="%1.1f%%", startangle=90,
           wedgeprops=wedge_props, pctdistance=0.78,
           textprops={"fontsize": 9.5, "color": TEXT})
    return fig, ax

# ═══════════════════════════════════════════════════════════════════
#  RULE-BASED Q&A ENGINE
# ═══════════════════════════════════════════════════════════════════
_QA = {
    "budget": {
        "heading": "Budgeting — The 50-30-20 Framework",
        "answer": (
            "The 50-30-20 rule splits your take-home pay into three buckets:\n\n"
            "• 50% — Needs: rent/EMI, groceries, utilities, transport, insurance premiums.\n"
            "• 30% — Wants: dining out, OTT subscriptions, travel, gadgets.\n"
            "• 20% — Savings: SIPs, emergency fund, PPF, NPS.\n\n"
            "Getting started:\n"
            "1. Pull up one month of UPI / bank statements and tag every expense.\n"
            "2. See which bucket is overfull and by how much.\n"
            "3. Set an automatic transfer to savings on the day your salary credits.\n"
            "4. Review every 3 months — income and expenses both change.\n\n"
            "If you live in Mumbai or Bangalore and 50% isn't enough for needs, "
            "adjust to 60-25-15. The exact split matters less than the habit."
        ),
    },
    "savings": {
        "heading": "Savings — Where and How Much",
        "answer": (
            "Target at least 20% of take-home pay. If you're starting from zero, "
            "begin at 5% and add 1–2% every month until you reach 20%.\n\n"
            "Where to save, in order of priority:\n"
            "1. Emergency fund (3–6 months of expenses) in a liquid mutual fund.\n"
            "2. Employer EPF match — if your employer matches, maximise it. "
               "It's a guaranteed 100% return with tax benefits.\n"
            "3. PPF — sovereign-backed, currently ~7.1%, fully tax-free.\n"
            "4. ELSS SIP — saves tax under 80C and builds equity wealth.\n"
            "5. Additional index fund SIPs for long-term goals.\n\n"
            "Golden rule: pay yourself first. Set the auto-debit before you spend, not after."
        ),
    },
    "debt": {
        "heading": "Debt Management — Avalanche vs Snowball",
        "answer": (
            "Two proven methods:\n\n"
            "Avalanche — Pay minimums on all debts. Put every extra rupee toward "
            "the highest interest rate debt first. Mathematically saves the most money.\n\n"
            "Snowball — Pay minimums on all debts. Put every extra rupee toward "
            "the smallest balance first. Clears accounts faster and builds motivation.\n\n"
            "Priority order for most Indians:\n"
            "1. Credit card dues (36–42% p.a.) — eliminate immediately, always.\n"
            "2. Personal loans (14–24% p.a.).\n"
            "3. Vehicle loans (8–12% p.a.).\n"
            "4. Home loan (8–9% p.a.) — lowest priority; interest gives tax benefit.\n\n"
            "Never pay only the minimum on a credit card. On ₹1 L at 3%/month, "
            "a ₹3,000 minimum payment means you never fully repay it."
        ),
    },
    "invest": {
        "heading": "Investing — How to Start",
        "answer": (
            "Pre-requisites before investing:\n"
            "• Emergency fund of 3–6 months in place.\n"
            "• High-interest debt (credit cards, personal loans) cleared.\n"
            "• Basic term + health insurance active.\n\n"
            "Suggested options by time horizon:\n"
            "• Less than 1 year   → Liquid MF or short FD   (5–7%)\n"
            "• 1–3 years          → Debt MF or FD            (6–8%)\n"
            "• 3–5 years          → Balanced Advantage Fund  (9–11%)\n"
            "• 5+ years           → Index fund / Flexi-cap   (11–14% historical)\n\n"
            "Simplest start: a monthly SIP of any amount in a Nifty 50 Index Fund. "
            "Low cost, diversified, no fund manager risk.\n\n"
            "Do not try to time the market. Time in the market beats timing the market."
        ),
    },
    "emergency": {
        "heading": "Emergency Fund — Your Financial Safety Net",
        "answer": (
            "An emergency fund = 3 to 6 months of essential monthly expenses, "
            "kept in liquid, safe instruments.\n\n"
            "Essential expenses include: rent/EMI, groceries, utilities, transport, "
            "insurance premiums, minimum loan payments. Not dining out or shopping.\n\n"
            "Where to keep it:\n"
            "1. Liquid Mutual Fund — best option (~6–7%, accessible in 1 business day).\n"
            "2. High-yield savings account — convenient, ~3–4%.\n"
            "3. Sweep-in FD — automatically earns FD rates on idle balance.\n\n"
            "Do not invest your emergency fund in stocks, real estate, or long FDs. "
            "The entire point is zero-penalty instant access.\n\n"
            "Build it in stages: first get to 1 month, then 3, then 6. "
            "Once fully funded, direct all surplus to investments."
        ),
    },
    "insurance": {
        "heading": "Insurance — Protect Before You Invest",
        "answer": (
            "Term Life Insurance (if you have dependents):\n"
            "• Cover: 10–15× your annual gross income.\n"
            "• Tenure: up to age 60–65 (until financial independence).\n"
            "• Type: pure term only. Avoid ULIPs, endowment, money-back plans.\n"
            "• Cost: roughly ₹12,000–₹20,000/year for ₹1 Cr cover at age 30.\n\n"
            "Health Insurance:\n"
            "• Minimum ₹5 L individual / ₹10 L family floater.\n"
            "• Add a super top-up (₹90 L over ₹10 L deductible) for very low premium.\n"
            "• Buy early — premiums rise steeply with age and pre-conditions.\n"
            "• Do not rely only on employer cover — it ends when employment ends.\n\n"
            "Avoid: ULIPs (combines insurance + investment badly), "
            "endowment plans (misleadingly low returns), "
            "and any plan where the agent says your 'money grows and is also protected'."
        ),
    },
    "tax": {
        "heading": "Tax Saving — Key Deductions to Know",
        "answer": (
            "Section 80C (₹1.5 L combined limit):\n"
            "ELSS, PPF, EPF, NPS, NSC, SCSS, life insurance premium, "
            "home loan principal repayment, children's tuition.\n\n"
            "Section 80D (health insurance premiums):\n"
            "• ₹25,000 for self/spouse/children.\n"
            "• Additional ₹25,000 for parents (₹50,000 if parents are senior citizens).\n\n"
            "Other useful deductions:\n"
            "• 80CCD(1B): ₹50,000 extra for NPS (above the 80C limit).\n"
            "• 24(b): Home loan interest up to ₹2 L (self-occupied property).\n"
            "• HRA: Exemption if you pay rent and receive HRA from employer.\n\n"
            "Old vs New Regime: New regime has lower slab rates but no deductions. "
            "Old regime wins if your total deductions exceed ~₹3.75 L. "
            "Calculate both on the IT portal before filing."
        ),
    },
    "retire": {
        "heading": "Retirement Planning — The Earlier the Better",
        "answer": (
            "Core equation (4% withdrawal rule):\n"
            "Target corpus = Annual retirement expenses × 25\n\n"
            "Example: Need ₹60,000/month in retirement (₹7.2 L/year) → Target = ₹1.8 Cr minimum.\n\n"
            "Best instruments for retirement:\n"
            "• NPS — market-linked, tax-efficient, 60% lump sum + 40% annuity at 60.\n"
            "• EPF + VPF — guaranteed ~8.1%, fully tax-free at maturity.\n"
            "• ELSS + Index Funds — equity growth over 20–30 years.\n"
            "• PPF — tax-free at all three stages (invest, accumulate, withdraw).\n\n"
            "The cost of waiting:\n"
            "₹5,000/month at 12% for 30 years = ₹1.76 Cr.\n"
            "₹10,000/month at 12% for 20 years = ₹99 L (double the monthly, half the result).\n\n"
            "Start today, with whatever amount you can. Increase annually."
        ),
    },
}

_TOPIC_KEYWORDS = {
    "budget":    ["budget", "50-30-20", "spend", "expense", "allocat", "monthly plan", "track"],
    "savings":   ["sav", "ppf", "fd", "fixed deposit", "how much", "park money", "recurring"],
    "debt":      ["debt", "loan", "emi", "credit card", "borrow", "repay", "avalanche", "snowball", "interest"],
    "invest":    ["invest", "mutual fund", "sip", "stock", "equity", "nifty", "index", "return", "portfolio", "elss"],
    "emergency": ["emergency", "rainy", "liquid", "cash reserve", "3 month", "6 month", "safety net"],
    "insurance": ["insur", "term", "health cover", "ulip", "cover", "policy", "life"],
    "tax":       ["tax", "80c", "80d", "hra", "deduction", "itr", "regime", "nps", "elss"],
    "retire":    ["retire", "pension", "corpus", "old age", "financial independence", "fire", "nest egg"],
}

def rule_based_answer(question: str) -> str:
    q = question.lower()
    matched = [t for t, kws in _TOPIC_KEYWORDS.items() if any(k in q for k in kws)]

    if not matched:
        return (
            "I can answer questions on: budgeting, savings, debt management, "
            "investing, emergency funds, insurance, tax saving, and retirement planning.\n\n"
            "Try asking:\n"
            "  • What is the 50-30-20 rule?\n"
            "  • How do I start saving with ₹5,000/month?\n"
            "  • How do I pay off credit card debt faster?\n"
            "  • Where should I invest for 5 years?"
        )

    parts = []
    for topic in matched[:2]:
        d = _QA[topic]
        parts.append(f"[ {d['heading']} ]\n\n{d['answer']}")

    return "\n\n───────────────\n\n".join(parts)

# ═══════════════════════════════════════════════════════════════════
#  SIDEBAR
# ═══════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='padding:6px 0 4px;'>
        <span style='font-family:Space Grotesk,sans-serif;font-size:1.45rem;
                     font-weight:700;color:#fff;letter-spacing:-0.02em;'>FinanceIQ</span>
        <div style='font-size:0.68rem;color:#5D7A99;letter-spacing:0.1em;
                     text-transform:uppercase;margin-top:3px;'>Personal Finance</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "nav",
        ["Home", "Budget Planner", "Savings Goal",
         "Debt Manager", "Emergency Fund", "Health Score", "Finance Q&A"],
        label_visibility="collapsed",
        format_func=lambda x: {
            "Home":           "  Home",
            "Budget Planner": "  Budget Planner",
            "Savings Goal":   "  Savings Goal",
            "Debt Manager":   "  Debt Manager",
            "Emergency Fund": "  Emergency Fund",
            "Health Score":   "  Health Score",
            "Finance Q&A":    "  Finance Q&A",
        }[x],
    )

    st.markdown("---")
    st.markdown(f"""
    <p style='font-size:0.72rem;color:#4A6580;line-height:1.65;'>
        General information only.<br>
        Consult a SEBI-registered advisor<br>for a personalised plan.
    </p>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  ── HOME ────────────────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════
if page == "Home":
    st.markdown("""
    <div class='eyebrow'>Personal Finance Assistant</div>
    <div class='page-title'>Make every rupee count.</div>
    <div class='page-sub'>
        Practical tools for budgeting, savings, debt, and long-term wealth — all in one place.
    </div>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Savings Target",        "≥ 20%",    "of take-home pay")
    k2.metric("Emergency Fund",        "6 Months", "essential expenses")
    k3.metric("Healthy Debt Ratio",    "< 36%",    "EMI to income")
    k4.metric("Wealth-Building Horizon", "10 + Yrs", "stay invested")

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1.65, 1], gap="large")

    with left:
        st.markdown("### Core Concepts")
        t1, t2, t3 = st.tabs(["50-30-20 Rule", "Power of Compounding", "Safety Net Order"])

        with t1:
            st.markdown("""
**Split your take-home pay into three purposeful buckets:**

| Category | Share | Examples |
|----------|-------|---------|
| 🏠 Needs | **50%** | Rent, groceries, EMIs, utilities, transport |
| 🎯 Wants | **30%** | Dining, OTT, gadgets, leisure travel |
| 💰 Savings | **20%** | SIPs, FD, PPF, emergency fund, NPS |

Adjust for your city and life stage — tracking consistently matters more than hitting the exact split.
""")

        with t2:
            st.markdown("""
Compounding means earning returns on previous returns. Starting early is the only unfair advantage available to everyone.

| Monthly SIP | 10 years | 20 years | 30 years |
|------------|----------|----------|----------|
| ₹3,000 | ₹6.97 L | ₹27.6 L | ₹1.06 Cr |
| ₹5,000 | ₹11.6 L | ₹46 L | ₹1.76 Cr |
| ₹10,000 | ₹23.2 L | ₹91.9 L | ₹3.52 Cr |

*Assumes 12% p.a. (historical long-run equity average). Not guaranteed.*

A 25-year-old investing ₹2,000/month will outpace a 35-year-old investing ₹8,000/month — by the time they retire.
""")

        with t3:
            st.markdown("""
Build in this exact order. Skipping ahead creates fragility.

1. **1-Month Expense Buffer** — cash in savings account, always accessible.
2. **Term + Health Insurance** — protect income and health before investing.
3. **Full Emergency Fund** — grow the buffer to 3–6 months in a liquid fund.
4. **High-Interest Debt Cleared** — credit cards and personal loans at 18%+ gone.
5. **Retirement Contributions** — EPF, PPF, NPS, ELSS with compounding runway.
6. **Goal-Based Investing** — home, education, car — now you can plan these.
""")

    with right:
        st.markdown("### Financial Wellness Principles")

        principles = [
            ("💡", "Spend less than you earn",
             "The foundation of every financial plan. The gap between income and spending is where wealth is built."),
            ("🔄", "Automate your savings",
             "Set a transfer to trigger on salary day. Willpower runs out — automation doesn't."),
            ("🚫", "Avoid lifestyle inflation",
             "As income grows, resist the pull to expand spending proportionally. Invest the difference."),
            ("📋", "Insure before you invest",
             "A single medical emergency or loss of income erases years of savings. Term + health cover first."),
            ("📈", "Stay invested through volatility",
             "Markets drop. The investors who stay put capture the recovery. Timing the market rarely works."),
        ]

        for icon, headline, detail in principles:
            st.markdown(f"""
<div class='principle-row'>
    <span class='principle-icon'>{icon}</span>
    <div class='principle-body'><b>{headline}.</b> {detail}</div>
</div>
""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
<div class='dark-banner'>
<p><strong>Not sure where to start?</strong><br>
Head to <em>Finance Q&A</em> in the sidebar and ask any question — budgeting, investing, debt, insurance, or tax saving.</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  ── BUDGET PLANNER ──────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════
elif page == "Budget Planner":
    st.markdown("""
    <div class='eyebrow'>Calculator</div>
    <div class='page-title'>Budget Planner</div>
    <div class='page-sub'>Customise the 50-30-20 framework to your income and lifestyle.</div>
    """, unsafe_allow_html=True)

    inp_col, chart_col = st.columns([1, 1.15], gap="large")

    with inp_col:
        income = st.number_input(
            "Monthly Take-Home Income (₹)",
            min_value=0.0, value=50000.0, step=1000.0, format="%.0f"
        )

        st.markdown("#### Adjust Allocation")
        needs_p = st.slider("Needs  (%)",   20, 70, 50, 5, help="Rent, EMIs, groceries, utilities, transport")
        wants_p = st.slider("Wants  (%)",   10, 50, 30, 5, help="Dining, entertainment, shopping, travel")
        sav_p   = 100 - needs_p - wants_p

        if sav_p < 0:
            st.error("Needs + Wants exceed 100%. Reduce one of the sliders.")
        else:
            color = SAGE if sav_p >= 20 else (GOLD if sav_p >= 10 else RED)
            st.markdown(f"""
<div style='background:{WHITE};border-left:4px solid {color};
            border-radius:8px;padding:12px 16px;
            font-family:Space Grotesk,sans-serif;font-size:1.05rem;
            font-weight:600;color:{N};box-shadow:0 1px 4px rgba(0,0,0,.05);'>
    Savings = {sav_p}% {"  ✓" if sav_p >= 20 else "  — try to reach 20%"}
</div>
""", unsafe_allow_html=True)

    if income > 0 and sav_p >= 0:
        n_amt = income * needs_p / 100
        w_amt = income * wants_p / 100
        s_amt = income * sav_p   / 100

        with inp_col:
            st.markdown("#### Monthly Breakdown")
            c1, c2, c3 = st.columns(3)
            c1.metric(f"Needs ({needs_p}%)",   f"₹{n_amt:,.0f}")
            c2.metric(f"Wants ({wants_p}%)",   f"₹{w_amt:,.0f}")
            c3.metric(f"Savings ({sav_p}%)",   f"₹{s_amt:,.0f}")

            st.markdown("#### Suggested Expense Breakdown")
            rows = [
                ("🏠 Rent / EMI",       "Need",    income * 0.25),
                ("🛒 Groceries",        "Need",    income * 0.10),
                ("⚡ Utilities",        "Need",    income * 0.05),
                ("🚗 Transport",        "Need",    income * 0.08),
                ("🍽️ Dining Out",       "Want",    income * 0.10),
                ("🎮 Entertainment",    "Want",    income * 0.08),
                ("🛍️ Shopping",         "Want",    income * 0.07),
                ("🚑 Emergency Build",  "Savings", income * 0.05),
                ("📈 SIP / Investment", "Savings", income * 0.15),
            ]
            df = pd.DataFrame(rows, columns=["Category", "Type", "Suggested (₹)"])
            df["Suggested (₹)"] = df["Suggested (₹)"].apply(lambda x: f"₹{x:,.0f}")
            st.dataframe(df, use_container_width=True, hide_index=True)

        with chart_col:
            fig, ax = pie_fig(
                [n_amt, w_amt, s_amt],
                [f"Needs\n₹{n_amt/1000:.1f}K", f"Wants\n₹{w_amt/1000:.1f}K", f"Savings\n₹{s_amt/1000:.1f}K"],
                colors=[N, GOLD, SAGE]
            )
            ax.set_title("Your Budget Distribution", fontsize=13, fontweight="bold", color=N, pad=14)
            st.pyplot(fig)
            plt.close(fig)

            if sav_p < 20:
                msg = f"Your savings rate is {sav_p}%. The benchmark is 20%. Consider reducing wants by ₹{(income*(20-sav_p)/100):,.0f}/month."
                colour = RED
            elif sav_p >= 30:
                msg = f"Excellent — you're saving {sav_p}% of income. At this rate, compounding works strongly in your favour."
                colour = SAGE
            else:
                msg = f"Good start. You're saving {sav_p}%. Nudge this to 25–30% as income grows."
                colour = GOLD
            st.markdown(f"""
<div style='background:{colour}18;border-left:4px solid {colour};
            border-radius:8px;padding:12px 16px;font-size:0.88rem; color:{N};margin-top:8px;'>
    {msg}
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  ── SAVINGS GOAL ────────────────═════════════════════════════════
# ═══════════════════════════════════════════════════════════════════
elif page == "Savings Goal":
    st.markdown("""
    <div class='eyebrow'>Calculator</div>
    <div class='page-title'>Savings Goal Planner</div>
    <div class='page-sub'>Figure out how much to save monthly — with and without investment returns.</div>
    """, unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    with left:
        goal = st.number_input("Target Amount (₹)", min_value=0.0, value=100000.0, step=5000.0, format="%.0f")
        current = st.number_input("Amount Already Saved (₹)", min_value=0.0, value=20000.0, step=1000.0, format="%.0f")
        months = int(st.number_input("Time Frame (months)", min_value=1, value=24, step=1))
        rate = st.slider("Expected Annual Return on Savings (%)", 0.0, 15.0, 7.0, 0.5,
                         help="Liquid MF ~7% · Debt fund ~8% · Equity index ~12%")

        if goal > 0 and months > 0:
            remaining = max(goal - current, 0.0)
            r_m = rate / 100 / 12
            if r_m > 0 and remaining > 0:
                sip = remaining * r_m / ((1 + r_m) ** months - 1)
            else:
                sip = remaining / months if months > 0 else 0
            progress = min(current / goal, 1.0) if goal > 0 else 0

            st.markdown("---")
            st.markdown(f"**Progress toward ₹{goal:,.0f}**")
            st.progress(progress)
            p1, p2 = st.columns(2)
            p1.metric("Completed", f"{progress*100:.1f}%")
            p2.metric("Remaining", f"₹{remaining:,.0f}")
            st.markdown("#### How Much to Save Monthly")
            r1, r2 = st.columns(2)
            r1.metric("Simple (no return)", f"₹{remaining/months:,.0f}")
            r2.metric(f"SIP @ {rate}% p.a.", f"₹{sip:,.0f}", f"saves ₹{(remaining/months - sip):,.0f}/mo" if sip < remaining/months else None)

    with right:
        if goal > 0 and months > 0:
            m_arr = list(range(0, months + 1))
            if r_m > 0:
                growth = [current * (1 + r_m) ** m + (sip * ((1 + r_m) ** m - 1) / r_m if m > 0 else 0) for m in m_arr]
            else:
                growth = [current + sip * m for m in m_arr]
            simple = [current + (remaining / months) * m for m in m_arr]

            fig2, ax2 = new_fig(6, 4.5)
            ax2.plot(m_arr, [v / 1000 for v in growth], color=N, lw=2.5, label=f"SIP @ {rate}% p.a.")
            ax2.plot(m_arr, [v / 1000 for v in simple], color=MUTED, lw=2, ls="--", label="No returns")
            ax2.axhline(goal / 1000, color=GOLD, ls=":", lw=2, label="Target")
            ax2.fill_between(m_arr, [v / 1000 for v in growth], alpha=0.08, color=N)
            ax2.set_xlabel("Month", fontsize=9)
            ax2.set_ylabel("Amount (₹ thousands)", fontsize=9)
            ax2.set_title("Savings Projection", fontsize=12, fontweight="bold", color=N, pad=10)
            ax2.legend(fontsize=8.5)
            ax2.grid(True, alpha=0.2)
            st.pyplot(fig2)
            plt.close(fig2)

            st.markdown("#### Milestone Tracker")
            for pct in (25, 50, 75, 100):
                amt = goal * pct / 100
                done = current >= amt
                if done:
                    st.markdown(f"✅ &nbsp; **{pct}%** — ₹{amt:,.0f} &nbsp; *Achieved*")
                else:
                    m_to = (amt - current) / sip if sip > 0 else float("inf")
                    st.markdown(f"⏳ &nbsp; **{pct}%** — ₹{amt:,.0f} &nbsp; in ~{m_to:.0f} months")

# ═══════════════════════════════════════════════════════════════════
#  ── DEBT MANAGER ────────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════
elif page == "Debt Manager":
    st.markdown("""
    <div class='eyebrow'>Calculator</div>
    <div class='page-title'>Debt Manager</div>
    <div class='page-sub'>Map your debts, understand your risk, and choose a payoff strategy.</div>
    """, unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    with left:
        st.markdown("#### Enter Your Debts")
        n_d = int(st.number_input("Number of debts / loans", min_value=1, max_value=7, value=2))
        debts = []
        for i in range(n_d):
            with st.expander(f"Debt {i+1}", expanded=(i == 0)):
                dc1, dc2, dc3 = st.columns(3)
                with dc1: nm = st.text_input("Name", value=f"Loan {i+1}", key=f"dn{i}")
                with dc2: am = st.number_input("Balance (₹)", min_value=0.0, value=50000.0 if i==0 else 15000.0, step=1000.0, format="%.0f", key=f"da{i}")
                with dc3: rt = st.number_input("Rate (% p.a.)", min_value=0.0, max_value=60.0, value=14.0 if i==0 else 36.0, step=0.5, key=f"dr{i}")
            debts.append({"name": nm, "amount": am, "rate": rt})

        st.markdown("---")
        inc_d = st.number_input("Monthly Income (₹)", min_value=0.0, value=50000.0, step=1000.0, format="%.0f", key="inc_d")
        emi_d = st.number_input("Total Monthly EMI (₹)", min_value=0.0, value=12000.0, step=500.0, format="%.0f", key="emi_d")

    with right:
        active = [d for d in debts if d["amount"] > 0]
        if active:
            total_debt = sum(d["amount"] for d in active)
            st.metric("Total Outstanding Debt", f"₹{total_debt:,.0f}")

            # Debt allocation chart
            fig3, ax3 = pie_fig([d["amount"] for d in active], [f"{d['name']}\n₹{d['amount']/1000:.1f}K" for d in active])
            ax3.set_title("Debt Distribution Matrix", fontsize=12, fontweight="bold")
            st.pyplot(fig3)
            plt.close(fig3)

            # Strategy suggestions
            avalanche = sorted(active, key=lambda x: x["rate"], reverse=True)
            snowball = sorted(active, key=lambda x: x["amount"])
            
            st.markdown("#### Recommended Payment Actions")
            st.info(f"⚡ **Avalanche Priority (Saves Most Money):** Target **{avalanche[0]['name']}** first (highest interest: {avalanche[0]['rate']}%).")
            st.info(f"❄️ **Snowball Priority (Psychological Wins):** Target **{snowball[0]['name']}** first (smallest balance: ₹{snowball[0]['amount']:,.0f}).")

        if inc_d > 0:
            dti = (emi_d / inc_d) * 100
            status = "Healthy" if dti < 36 else ("Warning Zone" if dti <= 50 else "Critical Status")
            color_d = SAGE if dti < 36 else (GOLD if dti <= 50 else RED)
            st.markdown(f"""
            <div class='card' style='border-left: 4px solid {color_d};'>
                <div style='font-size:0.75rem; color:{MUTED}; font-weight:700;'>DEBT-TO-INCOME RATIO</div>
                <div style='font-size:1.6rem; font-weight:700; color:{N};'>{dti:.1f}% <span style='font-size:1rem; color:{color_d};'>({status})</span></div>
                <p style='font-size:0.85rem; margin-top:4px;'>Lenders prefer an EMI ratio below 36%. Your allocation takes up {dti:.1f}% of your monthly take-home salary.</p>
            </div>
            """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  ── EMERGENCY FUND ────────────────═══════════════════════════════
# ═══════════════════════════════════════════════════════════════════
elif page == "Emergency Fund":
    st.markdown("""
    <div class='eyebrow'>Calculator</div>
    <div class='page-title'>Emergency Fund Safety Net</div>
    <div class='page-sub'>Calculate your foundational survival runway and secure baseline buffers.</div>
    """, unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")
    with left:
        rent = st.number_input("Monthly Rent / EMI (₹)", min_value=0.0, value=15000.0, step=500.0)
        food = st.number_input("Groceries & Core Utilities (₹)", min_value=0.0, value=10000.0, step=500.0)
        loans = st.number_input("Minimum Loan / Insurance Payments (₹)", min_value=0.0, value=3000.0, step=500.0)
        months_target = st.slider("Target Buffer Length (Months)", 1, 12, 6)

        essential_total = rent + food + loans
        target_corpus = essential_total * months_target

    with right:
        st.markdown("#### Safety Corpus Required")
        st.metric("Essential Monthly Expenses", f"₹{essential_total:,.0f}")
        st.metric(f"Total Target Buffer ({months_target} Months)", f"₹{target_corpus:,.0f}")

        st.markdown("""
        <div class='card card-gold'>
            <h5>Where to Hold Your Safe Reserves:</h5>
            <ul>
                <li><b>70% Liquid Mutual Funds:</b> Offers instant redemption access with yields typically around 6-7%.</li>
                <li><b>30% Sweep-In Savings Account:</b> Provides immediate access for emergency cash requirements.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  ── HEALTH SCORE ────────────────═════════════════════════════════
# ═══════════════════════════════════════════════════════════════════
elif page == "Health Score":
    st.markdown("""
    <div class='eyebrow'>Assessment</div>
    <div class='page-title'>Financial Health Score</div>
    <div class='page-sub'>Answer 5 rapid checkpoints to evaluate your structural financial resilience.</div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.2], gap="large")
    with c1:
        q1 = st.radio("1. Do you have active Emergency Funds?", ["No reserves", "1-2 months' cover", "3+ months' cover"])
        q2 = st.radio("2. What is your active Debt Status?", ["High credit card debt / defaults", "Manageable structural EMIs", "Completely debt-free"])
        q3 = st.radio("3. Do you possess Personal Insurance covers?", ["No personal insurance", "Only company medical insurance", "Independent Pure Term + Health insurance policies"])
        
        score = 0
        if "3+" in q1: score += 35
        elif "1-2" in q1: score += 15
        
        if "debt-free" in q2: score += 35
        elif "Manageable" in q2: score += 20
        
        if "Independent" in q3: score += 30
        elif "company" in q3: score += 15

    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        h_color = SAGE if score >= 70 else (GOLD if score >= 40 else RED)
        st.markdown(f"""
        <div class='score-circle' style='border-color: {h_color}; color: {N};'>
            {score}
        </div>
        <p style='text-align: center; font-weight: 700; color: {h_color}; font-size:1.15rem;'>Resilience Grade Evaluation</p>
        """, unsafe_allow_html=True)

        if score >= 70:
            st.success("Excellent! Your defensive structures are strong. Focus on expanding goal-based wealth planning.")
        elif score >= 40:
            st.warning("Moderate. Your foundation has tracking gaps. Build out your 3-6 month emergency fund reserves soon.")
        else:
            st.error("Action Required. Prioritize building an emergency buffer and pay down expensive credit cards immediately.")

# ═══════════════════════════════════════════════════════════════════
#  ── FINANCE Q&A ──────────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════
elif page == "Finance Q&A":
    st.markdown("""
    <div class='eyebrow'>AI Consultation Space</div>
    <div class='page-title'>FinanceIQ Intelligence Engine</div>
    <div class='page-sub'>Ask structural queries on budgeting frameworks, debts, mutual fund options, or Indian tax regimes.</div>
    """, unsafe_allow_html=True)

    if not st.session_state.qa_log:
        st.markdown(f"""
        <div class='dark-banner' style='margin-top:4px;'>
        <p>
            Pick a topic from the left, or type any personal finance question.<br><br>
            <strong>Covered areas:</strong> budgeting · savings · debt · investing · emergency funds · insurance · tax saving · retirement
        </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        bubbles = ""
        for msg in st.session_state.qa_log[-10:]:
            content = _html.escape(msg["content"]).replace("\n", "<br>")
            if msg["role"] == "user":
                bubbles += f"<div class='chat-bubble-user'>You<br>{content}</div>"
            else:
                bubbles += f"<div class='chat-bubble-ai'>FinanceIQ<br><br>{content}</div>"

        st.markdown(f"<div class='chat-wrap'>{bubbles}</div>", unsafe_allow_html=True)

    with st.form("chat_form", clear_on_submit=True):
        u_query = st.text_input("Pose your financial planning question below:", placeholder="e.g., What is the 50-30-20 rule or how to handle card debt?")
        submitted = st.form_submit_button("Query Engine")
        
        if submitted and u_query.strip():
            st.session_state.qa_log.append({"role": "user", "content": u_query})
            response_text = rule_based_answer(u_query)
            st.session_state.qa_log.append({"role": "ai", "content": response_text})
            st.rerun()
