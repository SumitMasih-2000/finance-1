import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =====================================================================
# 1. ARCHITECTURE & HIGH-FIDELITY GRADIENT THEME ENGINE
# =====================================================================
st.set_page_config(
    page_title="Money T - Dashboard Plan",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_moneyt_high_fidelity_theme():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700&display=swap');
        
        /* Main Canvas Layout Base */
        .stApp {
            background: linear-gradient(135deg, #F8FAFC 0%, #EEF2F6 100%) !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* --- SIDEBAR WORKSPACE BRANDING & ITEMS --- */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0;
            padding-top: 1.5rem !important;
        }
        
        .sidebar-brand-container {
            padding: 0 1rem 1.5rem 1rem;
        }
        
        .sidebar-nav-item {
            display: flex;
            align-items: center;
            padding: 0.75rem 1rem;
            border-radius: 12px;
            margin-bottom: 0.3rem;
            color: #64748B;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .sidebar-nav-item:hover {
            background-color: #F8FAFC;
            color: #475569;
        }
        .sidebar-nav-item.active {
            background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%);
            color: #FFFFFF !important;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.15);
        }
        
        /* --- DYNAMIC WHITE CARD SURFACES --- */
        .finance-card {
            background-color: #FFFFFF;
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            margin-bottom: 1.25rem;
        }
        
        /* --- STRATEGIC ALLOCATION DATAGRID TABLE --- */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            background-color: #FFFFFF;
        }
        .custom-table th {
            text-align: left;
            padding: 0.75rem 1rem;
            color: #FFFFFF;
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .custom-table td {
            padding: 0.9rem 1rem;
            color: #334155;
            font-size: 0.85rem;
            border-bottom: 1px solid #E2E8F0;
        }
        
        #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

inject_moneyt_high_fidelity_theme()

# =====================================================================
# 2. STATE PERSISTENCE SYSTEM (MONTHLY RELATIONAL MAPPING)
# =====================================================================
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if 'active_month' not in st.session_state:
    st.session_state['active_month'] = "April"

if 'monthly_db' not in st.session_state:
    st.session_state['monthly_db'] = {m: [] for m in months_list}

# Seed realistic reference data if fresh session
if not any(st.session_state['monthly_db'].values()):
    st.session_state['monthly_db']["April"] = [
        {"Merchant": "Corporate Rent Office", "Category": "Essential Needs", "Amount": 32000.0},
        {"Merchant": "Whole Foods Market", "Category": "Essential Needs", "Amount": 4800.0},
        {"Merchant": "Downtown Premium Dining Out", "Category": "Personal Lifestyle & Wants", "Amount": 8500.0},
        {"Merchant": "Vanguard Index Fund Pool", "Category": "Future Savings & Investments", "Amount": 12800.0}
    ]

# =====================================================================
# 3. SIDEBAR NAVIGATION CONTROLS
# =====================================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand-container">
        <h2 style='font-weight:800; color:#1E293B; margin:0; display:flex; align-items:center;'>
            <span style='background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>💜 Money T</span>
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-nav-item active">📋 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">📊 Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">📉 Income</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">🍔 Menu</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">💳 Payments</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">📂 Budget</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">⚙️ Settings</div>', unsafe_allow_html=True)
    
    st.markdown("<br><hr style='border-color:#E2E8F0;'><br>", unsafe_allow_html=True)
    
    # Clean workspace transaction additions
    st.markdown(f"<h4 style='font-weight:700; color:#1E293B; margin-bottom:0.75rem;'>✍️ Log Outlay ({st.session_state['active_month']})</h4>", unsafe_allow_html=True)
    entry_title = st.text_input("Merchant/Recipient", placeholder="e.g., Target, Electric Corp")
    entry_category = st.selectbox("Strategic Allocation Category", ["Essential Needs", "Personal Lifestyle & Wants", "Future Savings & Investments"])
    entry_amount = st.number_input("Amount Paid", min_value=0.0, value=0.0, step=100.0)
    add_btn = st.button("Commit Outlay Trace", use_container_width=True)

    if add_btn and entry_title and entry_amount > 0:
        st.session_state['monthly_db'][st.session_state['active_month']].append({
            "Merchant": entry_title,
            "Category": entry_category,
            "Amount": entry_amount
        })
        st.toast(f"Logged {entry_title} inside {st.session_state['active_month']}!", icon="🚀")

# =====================================================================
# 4. HEADER INTERACTION BANNER (CHANGEABLE MONTH TIMELINE)
# =====================================================================
st.markdown("<h3 style='margin:0 0 0.5rem 0; font-weight:800; color:#1E293B;'>Money T - Dashboard Plan</h3>", unsafe_allow_html=True)

# Generate month tabs layout
month_cols = st.columns(12)
for idx, m_name in enumerate(months_list):
    with month_cols[idx]:
        is_active = (m_name == st.session_state['active_month'])
        # Use native button styled carefully to preserve the timeline aesthetic
        btn_lbl = f"📍 {m_name}" if is_active else m_name
        if st.button(btn_lbl, key=f"month_btn_{m_name}", use_container_width=True):
            st.session_state['active_month'] = m_name
            st.rerun()

st.markdown("<div style='margin-bottom:1.25rem;'></div>", unsafe_allow_html=True)

# =====================================================================
# 5. INTEGRATED COMPACT CONTROLS & ALIGNMENT STRATEGY ENGINE
# =====================================================================
st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
st.markdown("<h5 style='margin:0 0 0.75rem 0; font-weight:700; color:#334155;'>Budget Parameter Configuration</h5>", unsafe_allow_html=True)

# 3 compact configurations side-by-side to eliminate white blocks
config_col1, config_col2, config_col3 = st.columns([1.5, 2.0, 3.5])

with config_col1:
    currency_choice = st.selectbox("Currency Token", options=["USD ($)", "EUR (€)", "GBP (£)", "INR (₹)"])
    symbols = {"USD ($)": "$", "EUR (€)": "€", "GBP (£)": "£", "INR (₹)": "₹"}
    curr_sym = symbols[currency_choice]

with config_col2:
    user_income = st.number_input(f"Monthly Net Income ({curr_sym})", min_value=1.0, value=80000.0, step=1000.0)

with config_col3:
    allocation_strategy = st.selectbox(
        "Matrix Strategy Target Split",
        options=[
            "Balanced Target Rule (50% Needs, 30% Wants, 20% Savings)",
            "Aggressive Growth Rule (40% Needs, 20% Wants, 40% Savings)",
            "Conservative Baseline Rule (60% Needs, 20% Wants, 20% Savings)"
        ]
    )

# Establish strict breakdown parameters
if "Balanced" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.50, 0.30, 0.20
elif "Aggressive" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.40, 0.20, 0.40
else:
    p_needs, p_wants, p_savings = 0.60, 0.20, 0.20

amt_needs_target = user_income * p_needs
amt_wants_target = user_income * p_wants
amt_savings_target = user_income * p_savings

st.markdown(f"""
<div style='margin-top:0.5rem; padding-top:0.5rem; border-top:1px dashed #E2E8F0; color:#64748B; font-size:0.8rem; font-weight:500;'>
    ✨ <strong style='color:#475569;'>Active Plan Profile:</strong> Allocation Balanced rule targets applied automatically across active 2026 data matrices.
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Extract operations data from selected month session arrays
current_month_entries = st.session_state['monthly_db'][st.session_state['active_month']]
df_entries = pd.DataFrame(current_month_entries) if current_month_entries else pd.DataFrame(columns=["Merchant", "Category", "Amount"])

spent_needs = df_entries[df_entries['Category'] == "Essential Needs"]['Amount'].sum()
spent_wants = df_entries[df_entries['Category'] == "Personal Lifestyle & Wants"]['Amount'].sum()
spent_savings = df_entries[df_entries['Category'] == "Future Savings & Investments"]['Amount'].sum()

total_spent = spent_needs + spent_wants + spent_savings
overall_ratio_used = int((total_spent / user_income * 100)) if user_income > 0 else 0

pct_needs_used = int((spent_needs / amt_needs_target * 100)) if amt_needs_target > 0 else 0
pct_wants_used = int((spent_wants / amt_wants_target * 100)) if amt_wants_target > 0 else 0
pct_savings_used = int((spent_savings / amt_savings_target * 100)) if amt_savings_target > 0 else 0

# =====================================================================
# 6. HIGH-FIDELITY CIRCULAR TRACKING GAUGES BANNER (FROM TEMPLATE IMAGE)
# =====================================================================
st.markdown("<div class='finance-card' style='padding:1rem 2rem;'>", unsafe_allow_html=True)
gauge_col1, gauge_col2, gauge_col3, gauge_col4, gauge_col5 = st.columns(5)

def construct_template_radial_gauge(label_text, percentage_val, prime_color):
    fig = go.Figure(go.Pie(
        values=[percentage_val, max(0, 100 - percentage_val)],
        hole=0.80,
        marker=dict(colors=[prime_color, '#F1F5F9']),
        textinfo='none', hoverinfo='none'
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10), showlegend=False, height=140,
        annotations=[dict(text=f"<span style='font-size:1.3rem; font-weight:800; color:#1E293B;'>{percentage_val}%</span><br><span style='font-size:0.68rem; color:#94A3B8; font-weight:700;'>{label_text}</span>", x=0.5, y=0.5, showarrow=False, align="center")]
    )
    return fig

with gauge_col1:
    # Master Total Ratio
    st.plotly_chart(construct_template_radial_gauge("Ratio", overall_ratio_used, "#6366F1"), use_container_width=True, key="g1")
with gauge_col2:
    st.plotly_chart(construct_template_radial_gauge("Income Used", pct_needs_used, "#8B5CF6"), use_container_width=True, key="g2")
with gauge_col3:
    st.plotly_chart(construct_template_radial_gauge("Wants Used", pct_wants_used, "#A855F7"), use_container_width=True, key="g3")
with gauge_col4:
    st.plotly_chart(construct_template_radial_gauge("Savings Used", pct_savings_used, "#EC4899"), use_container_width=True, key="g4")
with gauge_col5:
    # Custom interactive reference tracking index marker
    safety_margin = max(0, 100 - overall_ratio_used)
    st.plotly_chart(construct_template_radial_gauge("Margin Left", safety_margin, "#3B82F6"), use_container_width=True, key="g5")

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 7. CENTRAL DIRECTIVES MATRIX GRID & LIVE MATRIX TRACES
# =====================================================================
row2_left, row2_right = st.columns([1.8, 1.2])

with row2_left:
    st.markdown("<div class='finance-card' style='min-height:390px;'>", unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0 0 1rem 0; font-weight:700; color:#1E293B;'>Exact Strategic Allocation Directives Matrix</h5>", unsafe_allow_html=True)
    
    # Production-ready custom implementation of the template multi-layered matrix table look
    table_html = f"""
    <table class='custom-table'>
        <thead>
            <tr style='background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%);'>
                <th style='border-top-left-radius:8px;'>Where You Spend</th>
                <th>Target Split %</th>
                <th>Target Allocation Bound</th>
                <th>Current Month Spend</th>
                <th style='border-top-right-radius:8px;'>Available Surplus Remainder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style='font-weight:700; color:#4F46E5;'>📁 Essential Needs</td>
                <td><span style='font-weight:600; color:#6366F1;'>{int(p_needs*100)}%</span></td>
                <td style='color:#475569; font-weight:600;'>{curr_sym}{amt_needs_target:,.2f}</td>
                <td style='color:#E11D48; font-weight:600;'>{curr_sym}{spent_needs:,.2f}</td>
                <td style='font-weight:700; color:#16A34A;'>{curr_sym}{(amt_needs_target - spent_needs):,.2f}</td>
            </tr>
            <tr>
                <td style='font-weight:700; color:#9333EA;'>📁 Personal Lifestyle & Wants</td>
                <td><span style='font-weight:600; color:#A855F7;'>{int(p_wants*100)}%</span></td>
                <td style='color:#475569; font-weight:600;'>{curr_sym}{amt_wants_target:,.2f}</td>
                <td style='color:#E11D48; font-weight:600;'>{curr_sym}{spent_wants:,.2f}</td>
                <td style='font-weight:700; color:#16A34A;'>{curr_sym}{(amt_wants_target - spent_wants):,.2f}</td>
            </tr>
            <tr>
                <td style='font-weight:700; color:#DB2777;'>📁 Future Savings & Investments</td>
                <td><span style='font-weight:600; color:#EC4899;'>{int(p_savings*100)}%</span></td>
                <td style='color:#475569; font-weight:600;'>{curr_sym}{amt_savings_target:,.2f}</td>
                <td style='color:#E11D48; font-weight:600;'>{curr_sym}{spent_savings:,.2f}</td>
                <td style='font-weight:700; color:#16A34A;'>{curr_sym}{(amt_savings_target - spent_savings):,.2f}</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(table_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with row2_right:
    st.markdown("<div class='finance-card' style='min-height:390px;'>", unsafe_allow_html=True)
    st.markdown("<h5 style='margin:0 0 1rem 0; font-weight:700; color:#1E293B;'>Live Session Expense Ledger</h5>", unsafe_allow_html=True)
    
    if not df_entries.empty:
        st.dataframe(
            df_entries[["Merchant", "Category", "Amount"]],
            use_container_width=True,
            hide_index=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Reset Month Workspace Ledger"):
            st.session_state['monthly_db'][st.session_state['active_month']] = []
            st.rerun()
    else:
        st.markdown(f"<p style='color:#94A3B8; font-size:0.85rem; padding-top:3rem; text-align:center;'>No expenses recorded yet for the month of {st.session_state['active_month']}.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
