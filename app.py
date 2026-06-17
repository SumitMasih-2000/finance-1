import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import io

# =====================================================================
# 1. ARCHITECTURE & EXACT TEMPLATE COLOR MATCHING (UI ENGINE)
# =====================================================================
st.set_page_config(
    page_title="Money T Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_exact_template_theme():
    """Injects precise styling to clone the uploaded UI mockup template."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
        /* Main Canvas Layout Background (Light Grayish-White) */
        .stApp {
            background-color: #F3F4F6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* Headings & Interface Font Overrides */
        h1, h2, h3, h4, h5, h6, p, span, label, div {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* --- SIDEBAR CLONE STYLE (#111114 Dark Charcoal) --- */
        [data-testid="stSidebar"] {
            background-color: #111114 !important;
            border-right: 1px solid #1E1E24;
        }
        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        [data-testid="stSidebar"] .stMarkdown p {
            color: #A1A1AA !important; /* Muted sidebar items */
        }
        
        /* --- FILTER MATRIX DRIVEN HORIZONTALLY --- */
        .streamlit-expanderHeader {
            background-color: #FFFFFF !important;
            border-radius: 12px !important;
            border: 1px solid #E4E4E7 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        .streamlit-expanderContent {
            background-color: #FFFFFF !important;
            border: 1px solid #E4E4E7 !important;
            border-top: none !important;
            border-radius: 0 0 12px 12px !important;
            padding: 1.25rem !important;
        }
        
        /* Multi-Select Tag Adjustments (No More Orange) */
        span[data-baseweb="tag"] {
            background-color: #7C3AED !important; /* Purple Theme Focus Tag */
            color: #FFFFFF !important;
            border-radius: 6px !important;
        }
        
        /* Tab Selection Graphics */
        button[data-baseweb="tab"] {
            color: #71717A !important;
            font-weight: 600 !important;
            background-color: transparent !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #7C3AED !important;
            border-bottom-color: #7C3AED !important;
        }

        /* --- UI METRIC CARD GRID INHERITANCE (Exact Mockup Match) --- */
        .kpi-wrapper {
            background-color: #FFFFFF;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
            border: 1px solid #E4E4E7;
            position: relative;
            overflow: hidden;
            min-height: 140px;
        }
        .kpi-title {
            font-size: 0.85rem;
            color: #71717A;
            font-weight: 500;
        }
        .kpi-value {
            font-size: 2rem;
            font-weight: 700;
            color: #18181B;
            margin-top: 0.5rem;
            letter-spacing: -0.03em;
        }
        .kpi-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.5rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-top: 0.75rem;
        }
        .badge-inc { background-color: #DCFCE7; color: #16A34A; }
        .badge-dec { background-color: #FEE2E2; color: #DC2626; }
        
        /* Specific Top-Border Accents from Image Template */
        .border-purple { border-top: 4px solid #8B5CF6; }
        .border-orange { border-top: 4px solid #F97316; }
        .border-teal { border-top: 4px solid #06B6D4; }
        .border-green { border-top: 4px solid #10B981; }
        .border-gray { border-top: 4px solid #71717A; }

        /* Hide basic Streamlit overhead markers */
        #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

inject_exact_template_theme()

# =====================================================================
# 2. SEED GENERATOR & MULTIDIMENSIONAL LOGS DATA
# =====================================================================
@st.cache_data
def generate_360_financial_ledger():
    np.random.seed(42)
    today = datetime.date.today()
    start_time = today - datetime.timedelta(days=365)
    date_series = pd.date_range(start_time, today, freq='D')
    
    ledger_records = []
    accounts = ['Chase Checking', 'Amex Platinum', 'Fidelity Investment', 'Apple Cash']
    payment_methods = ['Credit Card', 'ACH Transfer', 'Debit Card', 'Digital Wallet']
    priorities = ['High', 'Medium', 'Low']
    statuses = ['Settled', 'Pending', 'Disputed']
    
    expense_universe = {
        'Housing': ['Mortgage Service', 'Grid Utilities', 'Property Management'],
        'Food & Beverage': ['Wholesale Groceries', 'Premium Dining', 'Delivery Apps'],
        'Transportation': ['Auto Insurance', 'Fuel Station', 'Ride Share Platforms'],
        'Entertainment': ['Subscriptions', 'Live Events', 'Gaming Ecosystems'],
        'Digital Shopping': ['Apparel', 'High-Tech Gear', 'Home Aesthetics'],
        'Healthcare': ['Premium Coverage', 'Pharmacy Cleared', 'Clinical Consultation']
    }
    
    for current_date in date_series:
        if current_date.day == 1:
            ledger_records.append([current_date, 'Income', 'Salary', 'Corporate Salary', 8500.00, 'Chase Checking', 'ACH Transfer', 'High', 'Settled', 'Yes'])
        if current_date.day == 15 and np.random.rand() > 0.5:
            ledger_records.append([current_date, 'Income', 'Consulting', 'Consulting Advisory', 2450.00, 'Chase Checking', 'ACH Transfer', 'Medium', 'Settled', 'No'])
        if current_date.day == 28 and current_date.month % 3 == 0:
            ledger_records.append([current_date, 'Income', 'Capital Yields', 'Equity Dividends', 680.00, 'Fidelity Investment', 'ACH Transfer', 'Low', 'Settled', 'No'])
            
        if current_date.day == 2:
            ledger_records.append([current_date, 'Expense', 'Housing', 'Mortgage Service', 2200.00, 'Chase Checking', 'ACH Transfer', 'High', 'Settled', 'Yes'])
            ledger_records.append([current_date, 'Expense', 'Housing', 'Grid Utilities', 240.00, 'Amex Platinum', 'Credit Card', 'High', 'Settled', 'Yes'])
            
        if np.random.rand() > 0.2:
            selected_cat = np.random.choice(list(expense_universe.keys()))
            selected_sub = np.random.choice(expense_universe[selected_cat])
            processed_amount = np.round(np.random.exponential(scale=45.0) + 5.00, 2)
            assigned_acct = np.random.choice(accounts)
            assigned_pay = 'Credit Card' if 'Amex' in assigned_acct else np.random.choice(payment_methods)
            assigned_prior = np.random.choice(priorities)
            assigned_status = np.random.choice(statuses, p=[0.92, 0.06, 0.02])
            is_recurring = 'Yes' if np.random.rand() > 0.85 else 'No'
            
            ledger_records.append([current_date, 'Expense', selected_cat, selected_sub, processed_amount, assigned_acct, assigned_pay, assigned_prior, assigned_status, is_recurring])

    output_frame = pd.DataFrame(ledger_records, columns=['Date', 'Transaction Type', 'Category', 'Sub Category', 'Amount', 'Account', 'Payment Method', 'Priority', 'Status', 'Recurring'])
    output_frame['Date'] = pd.to_datetime(output_frame['Date'])
    
    budget_allocations = {'Housing': 2600.00, 'Food & Beverage': 800.00, 'Transportation': 400.00, 'Entertainment': 350.00, 'Digital Shopping': 600.00, 'Healthcare': 300.00}
    output_frame['Assigned Budget'] = output_frame['Category'].map(budget_allocations).fillna(0.0)
    return output_frame

if 'fin_ledger' not in st.session_state:
    st.session_state['fin_ledger'] = generate_360_financial_ledger()

# =====================================================================
# 3. DARK SIDEBAR LAYOUT CLONE (#111114)
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='color:#FFFFFF; font-weight:700; margin-bottom:0rem;'>💰 Money T</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#71717A; font-size:0.8rem; margin-bottom:2rem;'>Personal Edition v2.6</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:0.75rem; font-weight:700; color:#52525B; letter-spacing:0.05em; margin-bottom:0.5rem;'>MENU</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#FFFFFF; font-weight:500; cursor:pointer;'>🎛️ Dashboard</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#A1A1AA; cursor:pointer;'>💳 Cards</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#A1A1AA; cursor:pointer;'>📈 Analytics</p>", unsafe_allow_html=True)
    
    st.divider()
    
    # Internal text lookup search field setup
    st.markdown("<p style='font-size:0.75rem; font-weight:700; color:#52525B; letter-spacing:0.05em; margin-bottom:0.5rem;'>FILTER BY SEARCH</p>", unsafe_allow_html=True)
    sidebar_search = st.text_input("Search description...", label_visibility="collapsed", placeholder="🔍 Search transaction...")

# =====================================================================
# 4. HORIZONTAL FILTER SLICERS (MATCHING THE IMAGE MATRIX LAYOUT)
# =====================================================================
raw_ledger = st.session_state['fin_ledger'].copy()

st.markdown("<h1 style='color:#18181B; font-weight:700; margin-bottom:0.2rem;'>Welcome, Ethan Cole 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#71717A; margin-top:0rem; margin-bottom:1.5rem;'>Here is your 360° financial visibility overview tracking matrix.</p>", unsafe_allow_html=True)

with st.expander("🎛️ SYSTEM CONTROLS & DASHBOARD SLICERS", expanded=True):
    col_date, col_cat, col_acct, col_pay = st.columns(4)
    
    with col_date:
        abs_min = raw_ledger['Date'].min().to_pydatetime()
        abs_max = raw_ledger['Date'].max().to_pydatetime()
        selected_window = st.date_input("Time Period Window", [abs_min, abs_max], min_value=abs_min, max_value=abs_max)
        runtime_ledger = raw_ledger[(raw_ledger['Date'] >= pd.to_datetime(selected_window[0])) & (raw_ledger['Date'] <= pd.to_datetime(selected_window[1]))] if len(selected_window) == 2 else raw_ledger
            
    with col_cat:
        cat_choices = list(runtime_ledger['Category'].unique())
        selected_cats = st.multiselect("Category Slicer", options=cat_choices, default=cat_choices)
        if selected_cats: runtime_ledger = runtime_ledger[runtime_ledger['Category'].isin(selected_cats)]
            
    with col_acct:
        acct_choices = list(runtime_ledger['Account'].unique())
        selected_accts = st.multiselect("Account Slicer", options=acct_choices, default=acct_choices)
        if selected_accts: runtime_ledger = runtime_ledger[runtime_ledger['Account'].isin(selected_accts)]
            
    with col_pay:
        pay_choices = list(runtime_ledger['Payment Method'].unique())
        selected_pays = st.multiselect("Payment Method Slicer", options=pay_choices, default=pay_choices)
        if selected_pays: runtime_ledger = runtime_ledger[runtime_ledger['Payment Method'].isin(selected_pays)]

if sidebar_search:
    runtime_ledger = runtime_ledger[runtime_ledger['Category'].str.contains(sidebar_search, case=False) | runtime_ledger['Sub Category'].str.contains(sidebar_search, case=False)]

# =====================================================================
# 5. DYNAMIC KPI CARDS MATCHING TEMPLATE BORDERS EXACTLY
# =====================================================================
val_income = runtime_ledger[runtime_ledger['Transaction Type'] == 'Income']['Amount'].sum()
val_expense = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']['Amount'].sum()
val_net_flow = val_income - val_expense
val_total_records = len(runtime_ledger)

def generate_html_card(title, cash_string, accent_class, badge_val, is_up=True):
    badge_class = "badge-inc" if is_up else "badge-dec"
    arrow = "▲" if is_up else "▼"
    return f"""
    <div class="kpi-wrapper {accent_class}">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{cash_string}</div>
        <div class="kpi-badge {badge_class}">{arrow} {badge_val} last month</div>
    </div>
    """

kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)
with kpi_col1: st.markdown(generate_html_card("Total Income", f"${val_income:,.0f}", "border-purple", "35%", True), unsafe_allow_html=True)
with kpi_col2: st.markdown(generate_html_card("Total Spending", f"${val_expense:,.0f}", "border-orange", "75%", False), unsafe_allow_html=True)
with kpi_col3: st.markdown(generate_html_card("Net Cash Flow", f"${val_net_flow:,.0f}", "border-teal", "15%", val_net_flow >= 0), unsafe_allow_html=True)
with kpi_col4: st.markdown(generate_html_card("Total Savings Pool", f"${(val_net_flow if val_net_flow > 0 else 0):,.0f}", "border-green", "12%", True), unsafe_allow_html=True)
with kpi_col5: st.markdown(generate_html_card("Total Records Logs", f"{val_total_records:,}", "border-gray", "85%", True), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Shared Styling Overrides for Plotly Charts to Match Light Layout
def style_plotly_to_match_template(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#18181B", family="Plus Jakarta Sans"),
        title_font=dict(color="#18181B", size=15, weight="bold"),
        legend=dict(font=dict(color="#18181B", size=11), orientation="h", y=1.12),
        margin=dict(l=30, r=20, t=50, b=20),
        hovermode="x unified"
    )
    if hasattr(fig, 'update_xaxes'):
        fig.update_xaxes(showgrid=True, gridcolor="#E4E4E7", tickfont=dict(color="#71717A"))
        fig.update_yaxes(showgrid=True, gridcolor="#E4E4E7", tickfont=dict(color="#71717A"))

# =====================================================================
# 6. GRAPHICS DEPLOYMENT VIA THE 5 NAVIGATION VIEWS
# =====================================================================
page_overview, page_spending, page_income, page_budget, page_status = st.tabs([
    "📊 Overview Suite", "💸 Spending Analysis", "📈 Income Tracking", "🛡️ Budget Review", "🎯 Transaction Status"
])

# --- TAB 1: OVERVIEW SUITE ---
with page_overview:
    chart_col, details_col = st.columns([2, 1])
    
    with chart_col:
        st.markdown("<div style='background:white; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
        st.markdown("#### Your Assets Progression")
        monthly_trend = runtime_ledger.groupby([pd.Grouper(key='Date', freq='ME'), 'Transaction Type'])['Amount'].sum().unstack().fillna(0)
        
        assets_fig = go.Figure()
        if 'Income' in monthly_trend.columns:
            assets_fig.add_trace(go.Scatter(x=monthly_trend.index, y=monthly_trend['Income'], name='Income', line=dict(color='#10B981', width=4), mode='lines'))
        if 'Expense' in monthly_trend.columns:
            assets_fig.add_trace(go.Scatter(x=monthly_trend.index, y=monthly_trend['Expense'], name='Expense', line=dict(color='#F97316', width=4), mode='lines'))
        
        style_plotly_to_match_template(assets_fig)
        st.plotly_chart(assets_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with details_col:
        st.markdown("<div style='background:white; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7; min-height:435px;'>", unsafe_allow_html=True)
        st.markdown("#### Transaction View Breakdown")
        
        pie_data = runtime_ledger.groupby('Account')['Amount'].sum().reset_index()
        donut_fig = px.pie(pie_data, values='Amount', names='Account', hole=0.6,
                           color_discrete_sequence=['#8B5CF6', '#10B981', '#F97316', '#71717A'])
        style_plotly_to_match_template(donut_fig)
        st.plotly_chart(donut_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: SPENDING ANALYSIS ---
with page_spending:
    exp_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']
    if not exp_set.empty:
        s1, s2, s3 = st.columns(3)
        with s1:
            st.markdown("#### Payments Method Density")
            f = px.pie(exp_set, values='Amount', names='Payment Method', color_discrete_sequence=['#8B5CF6','#F97316','#06B6D4','#10B981'])
            style_plotly_to_match_template(f)
            st.plotly_chart(f, use_container_width=True)
        with s2:
            st.markdown("#### Operational Priorities")
            f = px.bar(exp_set.groupby('Priority')['Amount'].sum().reset_index(), x='Priority', y='Amount', color_discrete_sequence=['#8B5CF6'])
            style_plotly_to_match_template(f)
            st.plotly_chart(f, use_container_width=True)
        with s3:
            st.markdown("#### Structural Category Split")
            f = px.pie(exp_set, values='Amount', names='Category', hole=0.3)
            style_plotly_to_match_template(f)
            st.plotly_chart(f, use_container_width=True)
    else:
        st.info("No expenditures tracked inside parameters.")

# --- TAB 3: INCOME TRACKING ---
with page_income:
    inc_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Income']
    i1, i2 = st.columns(2)
    with i1:
        st.markdown("#### Income Vector Flows")
        if not inc_set.empty:
            f = px.bar(inc_set.groupby([pd.Grouper(key='Date', freq='ME'), 'Category'])['Amount'].sum().unstack().fillna(0), barmode='stack')
            style_plotly_to_match_template(f)
            st.plotly_chart(f, use_container_width=True)
    with i2:
        st.markdown("#### Realized Accounts Multi-Comparison")
        comp = runtime_ledger.groupby(['Account', 'Transaction Type'])['Amount'].sum().unstack().fillna(0).reset_index()
        f = go.Figure()
        if 'Income' in comp.columns: f.add_trace(go.Bar(name='Inflows', x=comp['Account'], y=comp['Income'], marker_color='#10B981'))
        if 'Expense' in comp.columns: f.add_trace(go.Bar(name='Outflows', x=comp['Account'], y=comp['Expense'], marker_color='#F97316'))
        style_plotly_to_match_template(f)
        st.plotly_chart(f, use_container_width=True)

# --- TAB 4: BUDGET REVIEW ---
with page_budget:
    exp_b_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']
    if not exp_b_set.empty:
        b_matrix = exp_b_set.groupby('Category').agg({'Amount': 'sum', 'Assigned Budget': 'first', 'Priority': 'first', 'Recurring': 'first'}).reset_index()
        b_matrix['Utilization %'] = (b_matrix['Amount'] / b_matrix['Assigned Budget']) * 100
        
        b1, b2 = st.columns([2, 1])
        with b1:
            st.markdown("#### Category Limit Target Allocations")
            f = go.Figure()
            f.add_trace(go.Bar(name='Budget Limit', x=b_matrix['Category'], y=b_matrix['Assigned Budget'], marker_color='#E4E4E7'))
            f.add_trace(go.Bar(name='Real Spend Outflow', x=b_matrix['Category'], y=b_matrix['Amount'], marker_color='#8B5CF6'))
            style_plotly_to_match_template(f)
            st.plotly_chart(f, use_container_width=True)
        with b2:
            st.markdown("#### Recurrence Breakdown")
            f = px.bar(b_matrix.groupby('Recurring')['Amount'].sum().reset_index(), x='Recurring', y='Amount', marker_color='#06B6D4')
            style_plotly_to_match_template(f)
            st.plotly_chart(f, use_container_width=True)
            
        st.dataframe(b_matrix.style.format({'Amount':'${:,.2f}','Assigned Budget':'${:,.2f}','Utilization %':'{:.1f}%'}), use_container_width=True)

# --- TAB 5: TRANSACTION STATUS ---
with page_status:
    st.markdown("### Transaction Execution Status Controls")
    st.divider()
    
    st.markdown("#### Granular Ledger Data Records")
    # Presenting data cleanly in custom stylized frames matching the visual aesthetics
    st.dataframe(runtime_ledger[['Date', 'Transaction Type', 'Category', 'Sub Category', 'Amount', 'Account', 'Payment Method', 'Status']], use_container_width=True)
    
    # Bottom Export Setup Panel
    io_buf = io.StringIO()
    runtime_ledger.to_csv(io_buf, index=False)
    st.download_button(label="📥 Download Extracted Settlement CSV Report Ledger", data=io_buf.getvalue().encode('utf-8'), file_name="Money_T_Extract.csv", mime="text/csv")
