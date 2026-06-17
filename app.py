import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import io

# =====================================================================
# 1. APPLICATION ARCHITECTURE & PREMIUM ENHANCED CSS OVERRIDES
# =====================================================================
st.set_page_config(
    page_title="Aura Core",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enterprise Color Engine Design Guidelines
COLOR_PRIMARY = "#1E40AF"    # Slate Blue
COLOR_SECONDARY = "#0D9488"  # Teal
COLOR_ACCENT = "#F59E0B"     # Amber
COLOR_DANGER = "#DC2626"     # Crimson
COLOR_MUTED = "#64748B"      # Muted Slate Grey

def inject_enterprise_theme():
    """Forces structural DOM updates to override Streamlit default orange 
    with a premium enterprise design layout."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #F8FAFC;
        }
        
        /* ZERO-CONFIG THEME SYSTEM OVERRIDE (Goodbye Orange) */
        span[data-baseweb="tag"] {
            background-color: #1E40AF !important;
            color: #FFFFFF !important;
            border-radius: 6px !important;
        }
        div[data-baseweb="select"] div {
            border-color: #E2E8F0 !important;
        }
        button[data-baseweb="tab"] {
            color: #64748B !important;
            font-weight: 500 !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #1E40AF !important;
            border-bottom-color: #1E40AF !important;
            font-weight: 600 !important;
        }
        
        /* Premium Card UI Engineering */
        .kpi-container {
            background: #FFFFFF;
            padding: 1.25rem 1.5rem;
            border-radius: 12px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.03);
            border: 1px solid #E2E8F0;
            margin-bottom: 1rem;
            transition: all 0.2s ease-in-out;
        }
        .kpi-container:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
            border-color: #CBD5E1;
        }
        .kpi-label {
            font-size: 0.75rem;
            color: #64748B;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.25rem;
        }
        .kpi-val {
            font-size: 1.75rem;
            font-weight: 700;
            color: #0F172A;
            letter-spacing: -0.02em;
        }
        .kpi-subtext {
            font-size: 0.8rem;
            margin-top: 0.4rem;
            font-weight: 500;
        }
        .status-up { color: #0D9488; }
        .status-down { color: #DC2626; }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

inject_enterprise_theme()

# =====================================================================
# 2. SEED ENGINES & COMPREHENSIVE MULTIDIMENSIONAL DATA GENERATOR
# =====================================================================
@st.cache_data
def generate_360_financial_ledger():
    """Generates an enhanced multi-dimensional transactional ledger mirroring enterprise logging metrics."""
    np.random.seed(42)
    today = datetime.date.today()
    start_time = today - datetime.timedelta(days=365)
    date_series = pd.date_range(start_time, today, freq='D')
    
    ledger_records = []
    
    accounts = ['Chase Checking', 'Amex Platinum', 'Fidelity Investment', 'Apple Cash']
    payment_methods = ['Credit Card', 'ACH Transfer', 'Debit Card', 'Digital Wallet']
    priorities = ['High', 'Medium', 'Low']
    statuses = ['Settled', 'Pending', 'Disputed']
    
    income_map = {
        'Corporate Salary': ['Chase Checking', 'High', 'Settled'],
        'Consulting Advisory': ['Chase Checking', 'Medium', 'Settled'],
        'Equity Dividends': ['Fidelity Investment', 'Low', 'Settled']
    }
    
    expense_universe = {
        'Housing': ['Mortgage Service', 'Grid Utilities', 'Property Management'],
        'Food & Beverage': ['Wholesale Groceries', 'Premium Dining', 'Delivery Apps'],
        'Transportation': ['Auto Insurance', 'Fuel Station', 'Ride Share Platforms'],
        'Entertainment': ['Subscriptions', 'Live Events', 'Gaming Ecosystems'],
        'Digital Shopping': ['Apparel', 'High-Tech Gear', 'Home Aesthetics'],
        'Healthcare': ['Premium Coverage', 'Pharmacy Cleared', 'Clinical Consultation']
    }
    
    for idx, current_date in enumerate(date_series):
        # Monthly Recurring Income Execution
        if current_date.day == 1:
            ledger_records.append([
                current_date, 'Income', 'Salary', 'Corporate Salary', 7500.00,
                'Chase Checking', 'ACH Transfer', 'High', 'Settled', 'Yes'
            ])
        if current_date.day == 15 and np.random.rand() > 0.5:
            ledger_records.append([
                current_date, 'Income', 'Consulting', 'Consulting Advisory', np.random.uniform(1500, 3000),
                'Chase Checking', 'ACH Transfer', 'Medium', 'Settled', 'No'
            ])
        if current_date.day == 28 and current_date.month % 3 == 0:
            ledger_records.append([
                current_date, 'Income', 'Capital Yields', 'Equity Dividends', np.random.uniform(400, 900),
                'Fidelity Investment', 'ACH Transfer', 'Low', 'Settled', 'No'
            ])
            
        # Standard Operating Structural Expenditures
        if current_date.day == 2:
            ledger_records.append([
                current_date, 'Expense', 'Housing', 'Mortgage Service', 2200.00,
                'Chase Checking', 'ACH Transfer', 'High', 'Settled', 'Yes'
            ])
            ledger_records.append([
                current_date, 'Expense', 'Housing', 'Grid Utilities', np.random.uniform(180, 290),
                'Amex Platinum', 'Credit Card', 'High', 'Settled', 'Yes'
            ])
            
        # Daily Dynamic Lifestyle Fluctuations
        if np.random.rand() > 0.2:
            selected_cat = np.random.choice(list(expense_universe.keys()))
            selected_sub = np.random.choice(expense_universe[selected_cat])
            processed_amount = np.round(np.random.exponential(scale=45.0) + 5.00, 2)
            
            # Contextual Assignment Matrix logic
            assigned_acct = np.random.choice(accounts)
            assigned_pay = 'Credit Card' if 'Amex' in assigned_acct else np.random.choice(payment_methods)
            assigned_prior = np.random.choice(priorities)
            assigned_status = np.random.choice(statuses, p=[0.92, 0.06, 0.02])
            is_recurring = 'Yes' if np.random.rand() > 0.85 else 'No'
            
            ledger_records.append([
                current_date, 'Expense', selected_cat, selected_sub, processed_amount,
                assigned_acct, assigned_pay, assigned_prior, assigned_status, is_recurring
            ])

    output_frame = pd.DataFrame(ledger_records, columns=[
        'Date', 'Transaction Type', 'Category', 'Sub Category', 'Amount',
        'Account', 'Payment Method', 'Priority', 'Status', 'Recurring'
    ])
    output_frame['Date'] = pd.to_datetime(output_frame['Date'])
    # Setup baseline assigned target budgets inside mapping
    budget_allocations = {
        'Housing': 2600.00, 'Food & Beverage': 800.00, 'Transportation': 400.00,
        'Entertainment': 350.00, 'Digital Shopping': 600.00, 'Healthcare': 300.00,
        'Salary': 0.0, 'Consulting': 0.0, 'Capital Yields': 0.0
    }
    output_frame['Assigned Budget'] = output_frame['Category'].map(budget_allocations)
    return output_frame

if 'fin_ledger' not in st.session_state:
    st.session_state['fin_ledger'] = generate_360_financial_ledger()

# =====================================================================
# 3. INTERACTIVE MULTIPLE SLICERS ENGINE (QUICK FILTER BAR)
# =====================================================================
raw_ledger = st.session_state['fin_ledger'].copy()

with st.expander("🎛️ GLOBAL CONTROL SLICERS - ANALYTIC PARAMETERS", expanded=True):
    col_date, col_cat, col_acct, col_pay = st.columns(4)
    
    with col_date:
        abs_min = raw_ledger['Date'].min().to_pydatetime()
        abs_max = raw_ledger['Date'].max().to_pydatetime()
        selected_window = st.date_input("Time Period Window", [abs_min, abs_max], min_value=abs_min, max_value=abs_max)
        if len(selected_window) == 2:
            runtime_ledger = raw_ledger[(raw_ledger['Date'] >= pd.to_datetime(selected_window[0])) & (raw_ledger['Date'] <= pd.to_datetime(selected_window[1]))]
        else:
            runtime_ledger = raw_ledger
            
    with col_cat:
        cat_choices = list(runtime_ledger['Category'].unique())
        selected_cats = st.multiselect("Drilldown Categories", options=cat_choices, default=cat_choices)
        if selected_cats:
            runtime_ledger = runtime_ledger[runtime_ledger['Category'].isin(selected_cats)]
            
    with col_acct:
        acct_choices = list(runtime_ledger['Account'].unique())
        selected_accts = st.multiselect("Isolate Accounts", options=acct_choices, default=acct_choices)
        if selected_accts:
            runtime_ledger = runtime_ledger[runtime_ledger['Account'].isin(selected_accts)]
            
    with col_pay:
        pay_choices = list(runtime_ledger['Payment Method'].unique())
        selected_pays = st.multiselect("Payment Methods", options=pay_choices, default=pay_choices)
        if selected_pays:
            runtime_ledger = runtime_ledger[runtime_ledger['Payment Method'].isin(selected_pays)]

# =====================================================================
# 4. RUNTIME SYSTEM CALCULATIONS & CORE KPI DATA AGGREGATIONS
# =====================================================================
val_income = runtime_ledger[runtime_ledger['Transaction Type'] == 'Income']['Amount'].sum()
val_expense = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']['Amount'].sum()
val_net_flow = val_income - val_expense
val_savings = val_net_flow if val_net_flow > 0 else 0.0  # Surplus baseline logic
val_total_records = len(runtime_ledger)

def render_kpi(label, formatted_val, dynamic_subtext="", is_positive=True):
    subtext_color = "status-up" if is_positive else "status-down"
    indicator = "▲" if is_positive else "▼"
    subtext_markup = f'<div class="kpi-subtext {subtext_color}">{indicator} {dynamic_subtext}</div>' if dynamic_subtext else ''
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-label">{label}</div>
        <div class="kpi-val">{formatted_val}</div>
        {subtext_markup}
    </div>
    """, unsafe_allow_html=True)

# Top Bar Metric Viewport
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)
with kpi_col1: render_kpi("Total Income", f"${val_income:,.2f}", "Verified Ecosystem Inflows", True)
with kpi_col2: render_kpi("Total Expenses", f"${val_expense:,.2f}", "Structural Balance Sheet Debits", False)
with kpi_col3: render_kpi("Net Cash Flow", f"${val_net_flow:,.2f}", "Operating Margin Delta", val_net_flow >= 0)
with kpi_col4: render_kpi("Total Savings Pool", f"${val_savings:,.2f}", "Capital Escrow Preservation", True)
with kpi_col5: render_kpi("Total Records", f"{val_total_records:,}", "Line Transactions Parsed", True)

st.divider()

# =====================================================================
# 5. THE 5 INTERACTIVE DASHBOARD PAGES ARCHITECTURE
# =====================================================================
page_overview, page_spending, page_income, page_budget, page_status = st.tabs([
    "📊 1. Overview Suite",
    "💸 2. Spending Analysis",
    "📈 3. Income Tracking",
    "🛡️ 4. Budget Review",
    "🎯 5. Transaction Status"
])

# --- PAGE 1: OVERVIEW SUITE ---
with page_overview:
    st.markdown("### 360° Financial Visibility Overview")
    ov_col_left, ov_col_right = st.columns([2, 1])
    
    with ov_col_left:
        st.markdown("#### Chronological Capital Velocity Trends")
        monthly_trend = runtime_ledger.groupby([pd.Grouper(key='Date', freq='ME'), 'Transaction Type'])['Amount'].sum().unstack().fillna(0)
        trend_fig = go.Figure()
        if 'Income' in monthly_trend.columns:
            trend_fig.add_trace(go.Scatter(x=monthly_trend.index, y=monthly_trend['Income'], name='Gross Inflows', line=dict(color=COLOR_SECONDARY, width=3), mode='lines+markers'))
        if 'Expense' in monthly_trend.columns:
            trend_fig.add_trace(go.Scatter(x=monthly_trend.index, y=monthly_trend['Expense'], name='Burn Deficits', line=dict(color=COLOR_DANGER, width=3), mode='lines'))
        trend_fig.update_layout(template='plotly_white', margin=dict(l=10, r=10, t=10, b=10), height=320, legend=dict(orientation="h", y=1.1))
        st.plotly_chart(trend_fig, use_container_width=True)
        
    with ov_col_right:
        st.markdown("#### Core Account Capital Share")
        acct_distribution = runtime_ledger.groupby('Account')['Amount'].sum().reset_index()
        acct_fig = px.pie(acct_distribution, values='Amount', names='Account', hole=0.5, color_discrete_sequence=[COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_MUTED])
        acct_fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320, legend=dict(orientation="h", y=-0.1))
        st.plotly_chart(acct_fig, use_container_width=True)

# --- PAGE 2: SPENDING ANALYSIS ---
with page_spending:
    st.markdown("### Spending Breakdown Matrix")
    exp_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']
    
    if not exp_set.empty:
        sp_col1, sp_col2, sp_col3 = st.columns(3)
        
        with sp_col1:
            st.markdown("#### Distribution by Payment Method")
            pay_fig = px.pie(exp_set, values='Amount', names='Payment Method', color_discrete_sequence=px.colors.sequential.YlGnBu_r)
            st.plotly_chart(pay_fig, use_container_width=True)
            
        with sp_col2:
            st.markdown("#### Outflows by Allocation Priority")
            prio_fig = px.bar(exp_set.groupby('Priority')['Amount'].sum().reset_index(), x='Priority', y='Amount', color='Priority', color_discrete_map={'High': COLOR_DANGER, 'Medium': COLOR_ACCENT, 'Low': COLOR_SECONDARY})
            prio_fig.update_layout(template='plotly_white', showlegend=False)
            st.plotly_chart(prio_fig, use_container_width=True)
            
        with sp_col3:
            st.markdown("#### Structural Category Density")
            cat_fig = px.pie(exp_set, values='Amount', names='Category', hole=0.4, color_discrete_sequence=px.colors.qualitative.G10)
            st.plotly_chart(cat_fig, use_container_width=True)
    else:
        st.info("No expenditure traces recorded inside parameters.")

# --- PAGE 3: INCOME TRACKING ---
with page_income:
    st.markdown("### Income Streams vs. Operational Debits")
    inc_col_left, inc_col_right = st.columns(2)
    
    with inc_col_left:
        st.markdown("#### Inflow Channels Stack Analysis")
        inc_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Income']
        if not inc_set.empty:
            inc_matrix = inc_set.groupby([pd.Grouper(key='Date', freq='ME'), 'Category'])['Amount'].sum().unstack().fillna(0)
            inc_stack = px.bar(inc_matrix, x=inc_matrix.index, y=inc_matrix.columns, color_discrete_sequence=px.colors.sequential.Mint_r)
            inc_stack.update_layout(template='plotly_white', barmode='stack')
            st.plotly_chart(inc_stack, use_container_width=True)
        else:
            st.info("No inflow metrics found.")
            
    with inc_col_right:
        st.markdown("#### Account Cross-Comparison Interface")
        comparison_matrix = runtime_ledger.groupby(['Account', 'Transaction Type'])['Amount'].sum().unstack().fillna(0).reset_index()
        comp_bar = go.Figure()
        if 'Income' in comparison_matrix.columns:
            comp_bar.add_trace(go.Bar(name='Inflows', x=comparison_matrix['Account'], y=comparison_matrix['Income'], marker_color=COLOR_SECONDARY))
        if 'Expense' in comparison_matrix.columns:
            comp_bar.add_trace(go.Bar(name='Outflows', x=comparison_matrix['Account'], y=comparison_matrix['Expense'], marker_color=COLOR_DANGER))
        comp_bar.update_layout(barmode='group', template='plotly_white')
        st.plotly_chart(comp_bar, use_container_width=True)

# --- PAGE 4: BUDGET REVIEW ---
with page_budget:
    st.markdown("### Budget Utilization Analysis Framework")
    exp_b_set = runtime_ledger[runtime_ledger['Transaction Type'] == 'Expense']
    
    if not exp_b_set.empty:
        b_matrix = exp_b_set.groupby('Category').agg({'Amount': 'sum', 'Assigned Budget': 'first', 'Priority': 'first', 'Recurring': 'first'}).reset_index()
        b_matrix['Utilization %'] = (b_matrix['Amount'] / b_matrix['Assigned Budget']) * 100
        b_matrix['Remaining Capital'] = b_matrix['Assigned Budget'] - b_matrix['Amount']
        
        # Multi-Variate Layout Breakdowns
        b_tab_cat, b_tab_prio, b_tab_recur = st.tabs(["📂 Category Constraints", "🚨 Priority Limits", "🔄 Recurring Status Overviews"])
        
        with b_tab_cat:
            cat_b_fig = go.Figure()
            cat_b_fig.add_trace(go.Bar(name='Assigned Limit Threshold', x=b_matrix['Category'], y=b_matrix['Assigned Budget'], marker_color='#E2E8F0'))
            cat_b_fig.add_trace(go.Bar(name='Incurred Spend Outflow', x=b_matrix['Category'], y=b_matrix['Amount'], marker_color=COLOR_PRIMARY))
            cat_b_fig.update_layout(barmode='group', template='plotly_white')
            st.plotly_chart(cat_b_fig, use_container_width=True)
            
        with b_tab_prio:
            prio_b_matrix = b_matrix.groupby('Priority').agg({'Amount': 'sum', 'Assigned Budget': 'sum'}).reset_index()
            prio_b_fig = px.bar(prio_b_matrix, x='Priority', y=['Assigned Budget', 'Amount'], barmode='group', color_discrete_sequence=['#CBD5E1', COLOR_ACCENT])
            prio_b_fig.update_layout(template='plotly_white')
            st.plotly_chart(prio_b_fig, use_container_width=True)
            
        with b_tab_recur:
            recur_b_matrix = b_matrix.groupby('Recurring').agg({'Amount': 'sum', 'Assigned Budget': 'sum'}).reset_index()
            recur_b_fig = px.bar(recur_b_matrix, x='Recurring', y=['Assigned Budget', 'Amount'], barmode='group', color_discrete_sequence=['#CBD5E1', COLOR_PRIMARY])
            recur_b_fig.update_layout(template='plotly_white')
            st.plotly_chart(recur_b_fig, use_container_width=True)
            
        st.markdown("#### Structured Budget Matrix Logs")
        st.dataframe(b_matrix.style.format({
            'Amount': '${:,.2f}', 'Assigned Budget': '${:,.2f}', 
            'Utilization %': '{:.1f}%', 'Remaining Capital': '${:,.2f}'
        }), use_container_width=True)
    else:
        st.info("Provide dataset tracking fields to render utilization insights.")

# --- PAGE 5: TRANSACTION STATUS ---
with page_status:
    st.markdown("### Transaction Status Auditing & Controls")
    
    status_col_l, status_col_r = st.columns(2)
    with status_col_l:
        st.markdown("#### Log Count Quantities by Status")
        status_shares = runtime_ledger.groupby('Status')['Amount'].count().reset_index().rename(columns={'Amount': 'Count'})
        status_cnt_fig = px.bar(status_shares, x='Status', y='Count', color='Status', color_discrete_sequence=px.colors.qualitative.Pastel)
        status_cnt_fig.update_layout(template='plotly_white', showlegend=False)
        st.plotly_chart(status_cnt_fig, use_container_width=True)
        
    with status_col_r:
        st.markdown("#### Financial Volume Distribution by Category Profile")
        status_vol_matrix = runtime_ledger.groupby(['Category', 'Status'])['Amount'].sum().unstack().fillna(0)
        status_vol_fig = px.bar(status_vol_matrix, x=status_vol_matrix.index, y=status_vol_matrix.columns, color_discrete_sequence=[COLOR_SECONDARY, COLOR_ACCENT, COLOR_DANGER])
        status_vol_fig.update_layout(template='plotly_white')
        st.plotly_chart(status_vol_fig, use_container_width=True)
        
    st.divider()
    st.markdown("#### Monthly Average Flow Values")
    runtime_ledger['Month_Label'] = runtime_ledger['Date'].dt.strftime('%B %Y')
    monthly_averages = runtime_ledger.groupby(['Month_Label', 'Status'])['Amount'].mean().unstack().fillna(0)
    st.dataframe(monthly_averages.style.format("${:,.2f}"), use_container_width=True)

# =====================================================================
# 6. CENTRAL EXPORT INFRASTRUCTURE
# =====================================================================
st.sidebar.divider()
st.sidebar.markdown("### 💾 Export Engine")
io_buf = io.StringIO()
runtime_ledger.to_csv(io_buf, index=False)
st.sidebar.download_button(
    label="Download 360° Report Ledger", 
    data=io_buf.getvalue().encode('utf-8'), 
    file_name="Aura_Core_Financials.csv", 
    mime="text/csv"
)
