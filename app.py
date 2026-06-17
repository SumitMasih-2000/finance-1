import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import io

# =====================================================================
# 1. APPLICATION ARCHITECTURE & NAVY / BLUE HIGH-CONTRAST SYSTEM
# =====================================================================
st.set_page_config(
    page_title="Personal Finance",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Theme Design System
COLOR_NAVY = "#0F172A"       # Deep Dark Navy Blue (For main containers/cards)
COLOR_BLUE = "#1E40AF"       # Premium Royal Blue (For highlights/accent layers)
COLOR_TEXT_LIGHT = "#FFFFFF" # White text for high visibility
COLOR_BG_WHITE = "#FFFFFF"   # Pure White main canvas background

def inject_high_contrast_theme():
    """Injects high-contrast stylesheets: White canvas background with 
    Navy/Blue layout panels and clear white text strings."""
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Main Application Background Set to White */
        .stApp {{
            background-color: {COLOR_BG_WHITE} !important;
            font-family: 'Inter', sans-serif;
        }}
        
        /* Titles & Baseline Text */
        h1, h2, h3, h4, p, span, label {{
            color: {COLOR_NAVY} !important;
        }}
        
        /* Slicer Container Expanders Built with Navy Background & White Text */
        .streamlit-expanderHeader {{
            background-color: {COLOR_NAVY} !important;
            color: {COLOR_TEXT_LIGHT} !important;
            border-radius: 8px;
        }}
        .streamlit-expanderHeader p {{
            color: {COLOR_TEXT_LIGHT} !important;
        }}
        .streamlit-expanderContent {{
            background-color: {COLOR_BLUE} !important;
            border-radius: 0 0 8px 8px;
            padding: 1.5rem !important;
        }}
        .streamlit-expanderContent label, .streamlit-expanderContent p {{
            color: {COLOR_TEXT_LIGHT} !important;
        }}
        
        /* Override Select/Multi-select Pills (No More Orange) */
        span[data-baseweb="tag"] {{
            background-color: {COLOR_NAVY} !important;
            color: {COLOR_TEXT_LIGHT} !important;
            border: 1px solid #3B82F6 !important;
        }}
        
        /* Custom Premium KPI UI Cards - Navy Base, White Typography */
        .kpi-container {{
            background: {COLOR_NAVY} !important;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.15);
            border-left: 5px solid {COLOR_BLUE};
            margin-bottom: 1rem;
        }}
        .kpi-label {{
            font-size: 0.8rem;
            color: #94A3B8 !important; /* Muted soft grey-white for readability */
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .kpi-val {{
            font-size: 1.8rem;
            font-weight: 700;
            color: {COLOR_TEXT_LIGHT} !important;
            margin-top: 0.25rem;
        }}
        .kpi-subtext {{
            font-size: 0.8rem;
            margin-top: 0.5rem;
            font-weight: 500;
            color: #34D399 !important; /* Clean emerald green for visibility */
        }}
        .kpi-subtext-down {{
            font-size: 0.8rem;
            margin-top: 0.5rem;
            font-weight: 500;
            color: #F87171 !important; /* Pastel red alert */
        }}

        /* Navigation Tab Controllers */
        button[data-baseweb="tab"] {{
            color: {COLOR_NAVY} !important;
            font-weight: 600 !important;
        }}
        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {COLOR_BLUE} !important;
            border-bottom-color: {COLOR_BLUE} !important;
        }}

        /* Clean utilities */
        #MainMenu, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

inject_high_contrast_theme()

# =====================================================================
# 2. DATA SOURCE CONFIGURATIONS & LEDGER GENERATOR
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
            ledger_records.append([current_date, 'Income', 'Salary', 'Corporate Salary', 7500.00, 'Chase Checking', 'ACH Transfer', 'High', 'Settled', 'Yes'])
        if current_date.day == 15 and np.random.rand() > 0.5:
            ledger_records.append([current_date, 'Income', 'Consulting', 'Consulting Advisory', np.random.uniform(1500, 3000), 'Chase Checking', 'ACH Transfer', 'Medium', 'Settled', 'No'])
        if current_date.day == 28 and current_date.month % 3 == 0:
            ledger_records.append([current_date, 'Income', 'Capital Yields', 'Equity Dividends', np.random.uniform(400, 900), 'Fidelity Investment', 'ACH Transfer', 'Low', 'Settled', 'No'])
            
        if current_date.day == 2:
            ledger_records.append([current_date, 'Expense', 'Housing', 'Mortgage Service', 2200.00, 'Chase Checking', 'ACH Transfer', 'High', 'Settled', 'Yes'])
            ledger_records.append([current_date, 'Expense', 'Housing', 'Grid Utilities', np.random.uniform(180, 290), 'Amex Platinum', 'Credit Card', 'High', 'Settled', 'Yes'])
            
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
# 3. INTERACTIVE SLICERS ENGINE (NAVY BANNER BAR)
# =====================================================================
raw_ledger = st.session_state['fin_ledger'].copy()

st.markdown("<h1 style='color:#0F172A; font-weight:800; margin-bottom:0rem;'>360° Financial Visibility Suite</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#1E40AF; font-weight:500; margin-top:0rem; margin-bottom:1.5rem;'>Premium Personal Finance Analytics Control Center</p>", unsafe_allow_html=True)

with st.expander("🎛️ SYSTEM CONTROLS & MULTIPLE SLICERS", expanded=True):
    col_date, col_cat, col_acct, col_pay = st.columns(4)
    
    with col_date:
        abs_min = raw_ledger['Date'].min().to_pydatetime()
        abs_max = raw_ledger['Date'].max().to_pydatetime()
        selected_window = st.date_input("Time Period Window", [abs_min, abs_max], min_value=abs_min, max_value=abs_max)
        runtime_ledger = raw_ledger[(raw_ledger['Date'] >= pd.to_datetime(selected_window[0])) & (raw_ledger['Date'] <= pd.to_datetime(selected_window[1]))] if len(selected_window) == 2 else raw_ledger
            
    with col_cat:
        cat_choices = list(runtime_ledger['Category'].unique())
        selected_cats = st.multiselect("Drilldown Category", options=cat_choices, default=cat_choices)
        if selected_cats: runtime_ledger = runtime_ledger[runtime_ledger['Category'].isin(selected_cats)]
            
    with col_acct:
        acct_choices = list(runtime_ledger['Account'].unique())
        selected_accts = st.multiselect("Drilldown Account", options=acct_choices, default=acct_choices)
        if selected_accts: runtime_ledger = runtime_ledger[runtime_ledger['Account'].isin(selected_accts)]
            
    with col_pay:
        pay_choices = list(runtime_ledger['Payment Method'].unique())
        selected_pays = st.multiselect("Drilldown Payment Method", options=pay_choices, default=pay_choices)
        if selected_pays: runtime_ledger = runtime_ledger[runtime_ledger['Payment Method'].isin(selected_pays)]

# =====================================================================
# 4. RUNTIME SYSTEM CALCULATIONS & DYNAMIC KPI CARDS
# =====================================================================
val_income = runtime_ledger[runtime_ledger['Transaction Type'] == 'Income']['Amount'].sum()
val_expense = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']['Amount'].sum()
val_net_flow = val_income - val_expense
val_savings = val_net_flow if val_net_flow > 0 else 0.0
val_total_records = len(runtime_ledger)

def render_kpi(label, formatted_val, dynamic_subtext="", is_positive=True):
    subtext_class = "kpi-subtext" if is_positive else "kpi-subtext-down"
    indicator = "▲" if is_positive else "▼"
    subtext_markup = f'<div class="{subtext_class}">{indicator} {dynamic_subtext}</div>' if dynamic_subtext else ''
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-label">{label}</div>
        <div class="kpi-val">{formatted_val}</div>
        {subtext_markup}
    </div>
    """, unsafe_allow_html=True)

# 5 Dynamic KPI Cards displayed instantly at a single glance
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)
with kpi_col1: render_kpi("Total Income", f"${val_income:,.2f}", "Verified Inflows", True)
with kpi_col2: render_kpi("Total Expenses", f"${val_expense:,.2f}", "System Outflows", False)
with kpi_col3: render_kpi("Net Cash Flow", f"${val_net_flow:,.2f}", "Operating Margin", val_net_flow >= 0)
with kpi_col4: render_kpi("Total Savings", f"${val_savings:,.2f}", "Capital Preserved", True)
with kpi_col5: render_kpi("Total Records", f"{val_total_records:,}", "Logs Aggregated", True)

st.divider()

# Shared Chart Dark Theme Layout Configurator
def apply_chart_theme(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#0F172A", family="Inter"),
        title_font=dict(color="#0F172A", size=14, weight="bold"),
        legend=dict(font=dict(color="#0F172A")),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    if hasattr(fig, 'update_xaxes'):
        fig.update_xaxes(showgrid=True, gridcolor="#E2E8F0", title_font=dict(color="#0F172A"), tickfont=dict(color="#0F172A"))
        fig.update_yaxes(showgrid=True, gridcolor="#E2E8F0", title_font=dict(color="#0F172A"), tickfont=dict(color="#0F172A"))

# =====================================================================
# 5. THE 5 INTERACTIVE DASHBOARD PAGES
# =====================================================================
page_overview, page_spending, page_income, page_budget, page_status = st.tabs([
    "📊 Overview", "💸 Spending Analysis", "📈 Income Tracking", "🛡️ Budget Review", "🎯 Transaction Status"
])

# --- PAGE 1: OVERVIEW ---
with page_overview:
    st.markdown("<h3 style='color:#0F172A;'>360° Financial Visibility Overview Suite</h3>", unsafe_allow_html=True)
    ov_col_left, ov_col_right = st.columns([2, 1])
    
    with ov_col_left:
        st.markdown("#### Chronological Inflow vs Expense Trends")
        monthly_trend = runtime_ledger.groupby([pd.Grouper(key='Date', freq='ME'), 'Transaction Type'])['Amount'].sum().unstack().fillna(0)
        trend_fig = go.Figure()
        if 'Income' in monthly_trend.columns:
            trend_fig.add_trace(go.Scatter(x=monthly_trend.index, y=monthly_trend['Income'], name='Gross Income', line=dict(color=COLOR_BLUE, width=4), mode='lines+markers'))
        if 'Expense' in monthly_trend.columns:
            trend_fig.add_trace(go.Scatter(x=monthly_trend.index, y=monthly_trend['Expense'], name='Total Expenditures', line=dict(color="#EF4444", width=3), mode='lines'))
        apply_chart_theme(trend_fig)
        st.plotly_chart(trend_fig, use_container_width=True)
        
    with ov_col_right:
        st.markdown("#### Capital Assets Share by Account")
        acct_dist = runtime_ledger.groupby('Account')['Amount'].sum().reset_index()
        acct_fig = px.pie(acct_dist, values='Amount', names='Account', hole=0.5, color_discrete_sequence=[COLOR_NAVY, COLOR_BLUE, "#3B82F6", "#94A3B8"])
        apply_chart_theme(acct_fig)
        st.plotly_chart(acct_fig, use_container_width=True)

# --- PAGE 2: SPENDING ANALYSIS ---
with page_spending:
    st.markdown("<h3 style='color:#0F172A;'>Spending Breakdown Matrix</h3>", unsafe_allow_html=True)
    exp_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']
    
    if not exp_set.empty:
        sp_col1, sp_col2, sp_col3 = st.columns(3)
        with sp_col1:
            st.markdown("#### Expenses by Payment Method")
            pay_fig = px.pie(exp_set, values='Amount', names='Payment Method', color_discrete_sequence=["#0F172A", "#1E40AF", "#3B82F6", "#60A5FA"])
            apply_chart_theme(pay_fig)
            st.plotly_chart(pay_fig, use_container_width=True)
            
        with sp_col2:
            st.markdown("#### Expenses by Allocation Priority")
            prio_fig = px.bar(exp_set.groupby('Priority')['Amount'].sum().reset_index(), x='Priority', y='Amount', color_discrete_sequence=[COLOR_BLUE])
            apply_chart_theme(prio_fig)
            st.plotly_chart(prio_fig, use_container_width=True)
            
        with sp_col3:
            st.markdown("#### Outflows by Category Matrix")
            cat_fig = px.pie(exp_set, values='Amount', names='Category', hole=0.4, color_discrete_sequence=px.colors.qualitative.Prism)
            apply_chart_theme(cat_fig)
            st.plotly_chart(cat_fig, use_container_width=True)
    else:
        st.info("No expense data vectors found.")

# --- PAGE 3: INCOME TRACKING ---
with page_income:
    st.markdown("<h3 style='color:#0F172A;'>Income streams vs. Operational Expenses</h3>", unsafe_allow_html=True)
    inc_col_left, inc_col_right = st.columns(2)
    
    with inc_col_left:
        st.markdown("#### Income Category Stack Trends")
        inc_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Income']
        if not inc_set.empty:
            inc_matrix = inc_set.groupby([pd.Grouper(key='Date', freq='ME'), 'Category'])['Amount'].sum().unstack().fillna(0)
            inc_stack = px.bar(inc_matrix, x=inc_matrix.index, y=inc_matrix.columns, color_discrete_sequence=["#0F172A", "#1E40AF", "#60A5FA"])
            apply_chart_theme(inc_stack)
            st.plotly_chart(inc_stack, use_container_width=True)
            
    with inc_col_right:
        st.markdown("#### Comparative Tracking by Account Profile")
        comp_matrix = runtime_ledger.groupby(['Account', 'Transaction Type'])['Amount'].sum().unstack().fillna(0).reset_index()
        comp_bar = go.Figure()
        if 'Income' in comp_matrix.columns: comp_bar.add_trace(go.Bar(name='Income Inflows', x=comp_matrix['Account'], y=comp_matrix['Income'], marker_color=COLOR_BLUE))
        if 'Expense' in comp_matrix.columns: comp_bar.add_trace(go.Bar(name='Expense Outflows', x=comp_matrix['Account'], y=comp_matrix['Expense'], marker_color=COLOR_NAVY))
        apply_chart_theme(comp_bar)
        comp_bar.update_layout(barmode='group')
        st.plotly_chart(comp_bar, use_container_width=True)

# --- PAGE 4: BUDGET REVIEW ---
with page_budget:
    st.markdown("<h3 style='color:#0F172A;'>Budget Utilization Analysis</h3>", unsafe_allow_html=True)
    exp_b_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']
    
    if not exp_b_set.empty:
        b_matrix = exp_b_set.groupby('Category').agg({'Amount': 'sum', 'Assigned Budget': 'first', 'Priority': 'first', 'Recurring': 'first'}).reset_index()
        b_matrix['Utilization %'] = (b_matrix['Amount'] / b_matrix['Assigned Budget']) * 100
        b_matrix['Remaining Target'] = b_matrix['Assigned Budget'] - b_matrix['Amount']
        
        b_tab_cat, b_tab_prio, b_tab_recur = st.tabs(["📂 Allocation by Category", "🚨 Allocation by Priority", "🔄 Allocation by Recurring Status"])
        
        with b_tab_cat:
            cat_b_fig = go.Figure()
            cat_b_fig.add_trace(go.Bar(name='Assigned Target Budget', x=b_matrix['Category'], y=b_matrix['Assigned Budget'], marker_color="#CBD5E1"))
            cat_b_fig.add_trace(go.Bar(name='Incurred Active Spend', x=b_matrix['Category'], y=b_matrix['Amount'], marker_color=COLOR_BLUE))
            apply_chart_theme(cat_b_fig)
            cat_b_fig.update_layout(barmode='group')
            st.plotly_chart(cat_b_fig, use_container_width=True)
            
        with b_tab_prio:
            prio_mat = b_matrix.groupby('Priority').agg({'Amount': 'sum', 'Assigned Budget': 'sum'}).reset_index()
            prio_b_fig = px.bar(prio_mat, x='Priority', y=['Assigned Budget', 'Amount'], barmode='group', color_discrete_sequence=["#CBD5E1", COLOR_NAVY])
            apply_chart_theme(prio_b_fig)
            st.plotly_chart(prio_b_fig, use_container_width=True)
            
        with b_tab_recur:
            recur_mat = b_matrix.groupby('Recurring').agg({'Amount': 'sum', 'Assigned Budget': 'sum'}).reset_index()
            recur_b_fig = px.bar(recur_mat, x='Recurring', y=['Assigned Budget', 'Amount'], barmode='group', color_discrete_sequence=["#CBD5E1", COLOR_BLUE])
            apply_chart_theme(recur_b_fig)
            st.plotly_chart(recur_b_fig, use_container_width=True)
            
        st.dataframe(b_matrix.style.format({'Amount': '${:,.2f}', 'Assigned Budget': '${:,.2f}', 'Utilization %': '{:.1f}%', 'Remaining Target': '${:,.2f}'}), use_container_width=True)

# --- PAGE 5: TRANSACTION STATUS ---
with page_status:
    st.markdown("<h3 style='color:#0F172A;'>Transaction Status Monitoring Engine</h3>", unsafe_allow_html=True)
    status_col_l, status_col_r = st.columns(2)
    
    with status_col_l:
        st.markdown("#### Records Volumes by Status")
        status_shares = runtime_ledger.groupby('Status')['Amount'].count().reset_index().rename(columns={'Amount': 'Count'})
        status_cnt_fig = px.bar(status_shares, x='Status', y='Count', color_discrete_sequence=[COLOR_BLUE])
        apply_chart_theme(status_cnt_fig)
        st.plotly_chart(status_cnt_fig, use_container_width=True)
        
    with status_col_r:
        st.markdown("#### Volume Value Across Status Category Channels")
        status_vol_matrix = runtime_ledger.groupby(['Category', 'Status'])['Amount'].sum().unstack().fillna(0)
        status_vol_fig = px.bar(status_vol_matrix, x=status_vol_matrix.index, y=status_vol_matrix.columns, color_discrete_sequence=["#0F172A", "#1E40AF", "#93C5FD"])
        apply_chart_theme(status_vol_fig)
        st.plotly_chart(status_vol_fig, use_container_width=True)
        
    st.divider()
    st.markdown("#### Monthly Transaction Value Averages Matrix")
    runtime_ledger['Month_Label'] = runtime_ledger['Date'].dt.strftime('%B %Y')
    monthly_averages = runtime_ledger.groupby(['Month_Label', 'Status'])['Amount'].mean().unstack().fillna(0)
    st.dataframe(monthly_averages.style.format("${:,.2f}"), use_container_width=True)

# =====================================================================
# 6. CENTRAL EXPORT CONTROLS
# =====================================================================
st.sidebar.markdown(f"<h3 style='color:{COLOR_NAVY};'>⚙️ CORE CONTROLS</h3>", unsafe_allow_html=True)
io_buf = io.StringIO()
runtime_ledger.to_csv(io_buf, index=False)
st.sidebar.download_button(
    label="📥 Download Data Extract (CSV)", 
    data=io_buf.getvalue().encode('utf-8'), 
    file_name="360_Financial_Report.csv", 
    mime="text/csv"
)
