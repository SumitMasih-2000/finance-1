import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =====================================================================
# 1. APPLICATION ARCHITECTURE & UI TEMPLATE THEME CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Money T - Budgeting Suite",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_moneyt_template_theme():
    """Injects high-fidelity stylesheets matching your template layout style."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700&display=swap');
        
        .stApp {
            background-color: #F3F4F6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* --- SIDEBAR DESIGN BLOCK (#111114 Dark Charcoal) --- */
        [data-testid="stSidebar"] {
            background-color: #111114 !important;
            border-right: 1px solid #1E1E24;
            padding-top: 1rem !important;
        }
        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        
        .sidebar-nav-item {
            display: flex;
            align-items: center;
            padding: 0.75rem 1rem;
            border-radius: 10px;
            margin-bottom: 0.25rem;
            color: #A1A1AA;
            font-weight: 500;
            font-size: 0.95rem;
        }
        .sidebar-nav-item.active {
            background-color: #1F1F23;
            color: #FFFFFF;
        }
        .sidebar-section-lbl {
            font-size: 0.75rem;
            font-weight: 700;
            color: #52525B;
            letter-spacing: 0.08em;
            margin: 1.5rem 0 0.5rem 1rem;
        }
        
        /* --- DYNAMIC METRIC SURFACES --- */
        .kpi-wrapper {
            background-color: #FFFFFF;
            padding: 1.25rem;
            border-radius: 16px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
            border: 1px solid #E4E4E7;
            min-height: 125px;
        }
        .kpi-title {
            font-size: 0.85rem;
            color: #71717A;
            font-weight: 500;
        }
        .kpi-value {
            font-size: 2.1rem;
            font-weight: 700;
            color: #111114;
            margin-top: 0.4rem;
            letter-spacing: -0.04em;
        }
        
        .border-purple { border-top: 4px solid #6366F1; }
        .border-orange { border-top: 4px solid #F97316; }
        .border-green { border-top: 4px solid #10B981; }

        /* --- CLEAN STREAMLINED TABLE SYSTEMS --- */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            background-color: #FFFFFF;
            border-radius: 12px;
            overflow: hidden;
        }
        .custom-table th {
            text-align: left;
            padding: 0.75rem 1rem;
            background-color: #FAFAFA;
            color: #71717A;
            font-weight: 600;
            font-size: 0.8rem;
            border-bottom: 1px solid #E4E4E7;
        }
        .custom-table td {
            padding: 0.9rem 1rem;
            color: #111114;
            font-size: 0.85rem;
            border-bottom: 1px solid #E4E4E7;
        }
        .pill-medium {
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        
        #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

inject_moneyt_template_theme()

# =====================================================================
# 2. RUNTIME ACTIVE LEDGER STATE ENGINE (USER ENTRY ONLY)
# =====================================================================
if 'user_expenses' not in st.session_state:
    st.session_state['user_expenses'] = []

# =====================================================================
# 3. SIDEBAR NAVIGATION LAYOUT
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0rem; font-weight:700;'>💳 Money T</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-lbl">MENU</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item active">🏠 Dashboard Plan</div>', unsafe_allow_html=True)

# =====================================================================
# 4. INTERACTIVE HEADER & ENGINE CONTROL CONTROLS
# =====================================================================
st.markdown("<h1 style='color:#111114; font-weight:700; margin-bottom: 0rem;'>Personalized Allocation Strategy Matrix</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#71717A; margin-top:0.25rem; margin-bottom:1.5rem;'>Zero Pre-loaded Dummy Data. Driven entirely by your income and live spending entries.</p>", unsafe_allow_html=True)

# --- FINANCIAL INPUT SYSTEM ---
st.markdown("<div style='background-color: #FFFFFF; padding:1.25rem; border-radius:14px; border:1px solid #E4E4E7; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
st.markdown("<h4 style='margin:0 0 0.75rem 0; font-weight:700; color:#111114;'>⚙️ Live Budget Planner Inputs</h4>", unsafe_allow_html=True)

config_col1, config_col2, config_col3 = st.columns([1.5, 1.5, 2])

with config_col1:
    currency_choice = st.selectbox(
        "Select Local Currency Token",
        options=["USD ($)", "EUR (€)", "GBP (£)", "JPY (¥)", "INR (₹)"]
    )
    symbols = {"USD ($)": "$", "EUR (€)": "€", "GBP (£)": "£", "JPY (¥)": "¥", "INR (₹)": "₹"}
    curr_sym = symbols[currency_choice]

with config_col2:
    user_income = st.number_input(
        f"Enter Your Real Monthly Net Income ({curr_sym}):", 
        min_value=0.0, 
        value=80000.0,
        step=500.0
    )

with config_col3:
    allocation_strategy = st.selectbox(
        "Select Budget Strategy Rule",
        options=[
            "Balanced Strategy (50% Needs, 30% Wants, 20% Savings)",
            "Aggressive Investment Strategy (40% Needs, 20% Wants, 40% Savings)",
            "Conservative Minimum Strategy (60% Needs, 20% Wants, 20% Savings)"
        ]
    )

# Deconstruct Strategy Splitting Rules
if "Balanced Strategy" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.50, 0.30, 0.20
elif "Aggressive Investment" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.40, 0.20, 0.40
else:
    p_needs, p_wants, p_savings = 0.60, 0.20, 0.20

# Absolute Dynamic Allocations Calculation
amt_needs = user_income * p_needs
amt_wants = user_income * p_wants
amt_savings = user_income * p_savings

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 5. ENTER REAL EXPENSES INTERACTIVE MANIFEST SYSTEM
# =====================================================================
st.markdown("<div style='background-color: #FFFFFF; padding:1.25rem; border-radius:14px; border:1px solid #E4E4E7; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
st.markdown("<h4 style='margin:0 0 0.75rem 0; font-weight:700; color:#111114;'>✍️ Record Where and How Much You Spent</h4>", unsafe_allow_html=True)

exp_col1, exp_col2, exp_col3, exp_col4 = st.columns([2, 2, 1.5, 1])

with exp_col1:
    entry_title = st.text_input("Where did you spend this? (e.g., Landlord, Walmart, Gas Station, Vanguard)", placeholder="Enter recipient or store")
with exp_col2:
    entry_category = st.selectbox("Which core allocation pool does this belong to?", ["Essential Needs", "Personal Lifestyle & Wants", "Future Savings & Investments"])
with exp_col3:
    entry_amount = st.number_input(f"Amount Spent ({curr_sym})", min_value=0.0, value=0.0, step=10.0)
with exp_col4:
    st.markdown("<div style='padding-top:1.7rem;'></div>", unsafe_allow_html=True)
    add_btn = st.button("Log Expense", use_container_width=True)

if add_btn and entry_title and entry_amount > 0:
    st.session_state['user_expenses'].append({
        "Title": entry_title,
        "Category": entry_category,
        "Amount": entry_amount
    })
    st.success(f"Successfully logged entry for '{entry_title}'!")

st.markdown("</div>", unsafe_allow_html=True)

# Calculate active balances based on live user entries
df_entries = pd.DataFrame(st.session_state['user_expenses']) if st.session_state['user_expenses'] else pd.DataFrame(columns=["Title", "Category", "Amount"])

spent_needs = df_entries[df_entries['Category'] == "Essential Needs"]['Amount'].sum()
spent_wants = df_entries[df_entries['Category'] == "Personal Lifestyle & Wants"]['Amount'].sum()
spent_savings = df_entries[df_entries['Category'] == "Future Savings & Investments"]['Amount'].sum()

# Check to block layout rendering if income isn't set yet
if user_income <= 0:
    st.info("👋 Please set an income value greater than 0 above to generate your live dashboard analytics.")
else:
    # =====================================================================
    # 6. DYNAMIC CALCULATED HIGHLIGHT BUDGET REMAINING KPI CARDS
    # =====================================================================
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

    with kpi_col1:
        st.markdown(f"""
        <div class="kpi-wrapper border-purple">
            <div class="kpi-title">Essential Needs Left ({int(p_needs*100)}%)</div>
            <div class="kpi-value" style="color: #4F46E5;">{curr_sym}{(amt_needs - spent_needs):,.2f}</div>
            <div style="font-size:0.75rem; color:#71717A; margin-top:0.4rem;">Total Budgeted: {curr_sym}{amt_needs:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi_col2:
        st.markdown(f"""
        <div class="kpi-wrapper border-orange">
            <div class="kpi-title">Lifestyle & Wants Left ({int(p_wants*100)}%)</div>
            <div class="kpi-value" style="color: #F97316;">{curr_sym}{(amt_wants - spent_wants):,.2f}</div>
            <div style="font-size:0.75rem; color:#71717A; margin-top:0.4rem;">Total Budgeted: {curr_sym}{amt_wants:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi_col3:
        st.markdown(f"""
        <div class="kpi-wrapper border-green">
            <div class="kpi-title">Savings Strategy Target ({int(p_savings*100)}%)</div>
            <div class="kpi-value" style="color: #10B981;">{curr_sym}{(amt_savings - spent_savings):,.2f}</div>
            <div style="font-size:0.75rem; color:#71717A; margin-top:0.4rem;">Total Budgeted: {curr_sym}{amt_savings:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================================
    # 7. CENTRAL LAYOUT DATA TABLES & VISUAL PROGRESS
    # =====================================================================
    body_col_left, body_col_right = st.columns([1.8, 1.2])

    with body_col_left:
        # Dynamic Recommendation Details Action Grid (Your Exact Table Layout)
        st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#111114;'>Exact Allocation Directives Matrix</h4>", unsafe_allow_html=True)
        
        table_html = f"""
        <table class='custom-table'>
            <thead>
                <tr style='background-color: #FAFAFA;'>
                    <th>Where You Should Spend</th>
                    <th>Examples / Real Items Logged Below</th>
                    <th>Budget Target Split</th>
                    <th>Remaining Spending Budget Available</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style='font-weight:600;'>📁 Essential Needs</td>
                    <td style='color:#71717A; font-size:0.8rem;'>Rent/Mortgage, Utilities, Groceries, Insurance, Minimum Debt Payments</td>
                    <td><span class='pill-medium' style='background-color:#EEF2FF; color:#4F46E5;'>{int(p_needs*100)}%</span></td>
                    <td style='font-weight:700;'>{curr_sym}{(amt_needs - spent_needs):,.2f}</td>
                </tr>
                <tr>
                    <td style='font-weight:600;'>📁 Personal Lifestyle & Wants</td>
                    <td style='color:#71717A; font-size:0.8rem;'>Dining Out, Entertainment, Hobbies, Travel, Shopping, Subscriptions</td>
                    <td><span class='pill-medium' style='background-color:#FFFBEB; color:#D97706;'>{int(p_wants*100)}%</span></td>
                    <td style='font-weight:700;'>{curr_sym}{(amt_wants - spent_wants):,.2f}</td>
                </tr>
                <tr>
                    <td style='font-weight:600;'>📁 Future Savings & Investments</td>
                    <td style='color:#71717A; font-size:0.8rem;'>Emergency Fund, Retirement accounts (401k/IRA), Stocks, Cash Reserves</td>
                    <td><span class='pill-medium' style='background-color:#ECFDF5; color:#059669;'>{int(p_savings*100)}%</span></td>
                    <td style='font-weight:700;'>{curr_sym}{(amt_savings - spent_savings):,.2f}</td>
                </tr>
            </tbody>
        </table>
        """
        st.markdown(table_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Live Ledger List Table
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#111114;'>Your Live Spending Ledger</h4>", unsafe_allow_html=True)
        if not df_entries.empty:
            st.dataframe(df_entries, use_container_width=True, hide_index=True)
            if st.button("Clear All Logged Expenses"):
                st.session_state['user_expenses'] = []
                st.rerun()
        else:
            st.markdown("<p style='color:#71717A; font-size:0.85rem;'>No expenses logged yet. Use the form above to record items.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with body_col_right:
        # High Fidelity Visual Donut Matrix Tracking Real-Time Used vs Available Funds
        st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7; min-height:360px;'>", unsafe_allow_html=True)
        st.markdown("<span style='font-weight:700; color:#111114;'>Active Resource Spending Distribution</span>", unsafe_allow_html=True)
        
        labels = ['Spent - Needs', 'Spent - Wants', 'Spent - Savings', 'Remaining Available']
        values = [spent_needs, spent_wants, spent_savings, max(0.0, user_income - (spent_needs + spent_wants + spent_savings))]
        colors = ['#818CF8', '#FDBA74', '#34D399', '#E4E4E7']
        
        gauge_fig = go.Figure(go.Pie(
            values=values,
            labels=labels,
            hole=0.7,
            marker=dict(colors=colors),
            textinfo='none',
            hoverinfo='label+value'
        ))
        
        gauge_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#111114", family="Plus Jakarta Sans"),
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=True,
            legend=dict(orientation="h", y=-0.1, x=-0.05)
        )
        
        st.plotly_chart(gauge_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
