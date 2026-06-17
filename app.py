import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import io

# =====================================================================
# 1. CORE THEME CONFIGURATION & PREMIUM GRAPHIC DESIGN OVERRIDES
# =====================================================================
st.set_page_config(
    page_title="Aura",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional FinTech Palette Configuration
COLOR_PRIMARY = "#2563EB"    # Blue
COLOR_SECONDARY = "#10B981"  # Green
COLOR_ACCENT = "#F59E0B"     # Gold
COLOR_DANGER = "#EF4444"     # Red
COLOR_MUTED = "#64748B"      # Gray

def inject_premium_css():
    """Injects commercial grade structural layout styling mimicking premium platforms."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #F8FAFC;
        }
        
        /* OVERRIDE THE ORANGE WIDGET HIGHLIGHTS */
        span[data-baseweb="tag"] {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
        }
        div[data-baseweb="select"] div {
            border-color: #CBD5E1;
        }
        
        /* Premium Card UI Engineering */
        .kpi-container {
            background: #FFFFFF;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 15px -3px rgba(15, 23, 42, 0.04), 0 4px 6px -2px rgba(15, 23, 42, 0.02);
            border: 1px solid #E2E8F0;
            margin-bottom: 1rem;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .kpi-container:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.08), 0 10px 10px -5px rgba(15, 23, 42, 0.04);
            border-color: #CBD5E1;
        }
        
        .kpi-label {
            font-size: 0.8rem;
            color: #64748B;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            margin-bottom: 0.5rem;
        }
        
        .kpi-val {
            font-size: 1.85rem;
            font-weight: 700;
            color: #0F172A;
            letter-spacing: -0.02em;
        }
        
        .kpi-subtext {
            font-size: 0.85rem;
            margin-top: 0.6rem;
            font-weight: 500;
            display: flex;
            align-items: center;
        }
        
        .status-up { color: #10B981; }
        .status-down { color: #EF4444; }
        
        /* AI Panel Styling */
        .ai-insight-panel {
            background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
            border-left: 6px solid #10B981;
            padding: 1.5rem;
            border-radius: 14px;
            margin-bottom: 1.25rem;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.06);
        }
        
        /* Clean Interface Utilities */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Custom Styling for the Filter Section Header */
        .filter-banner {
            background-color: #FFFFFF;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
# =====================================================================
# 2. SEED ENGINES & REALISTIC SYNTHETIC LEDGER GENERATOR
# =====================================================================
@st.cache_data
def generate_synthetic_ledger():
    np.random.seed(101)
    today = datetime.date.today()
    start_time = today - datetime.timedelta(days=365)
    date_series = pd.date_range(start_time, today, freq='D')
    
    ledger_records = []
    income_streams = ['Corporate Salary', 'Consulting Advisory', 'Equity Dividends']
    expense_universe = {
        'Housing': ['Mortgage Service', 'Grid Utilities', 'Property Management'],
        'Food & Beverage': ['Wholesale Groceries', 'Premium Dining', 'Delivery Apps'],
        'Transportation': ['Auto Insurance', 'Fuel Station', 'Ride Share Platforms'],
        'Entertainment': ['Streaming Subscriptions', 'Live Events', 'Gaming Ecosystems'],
        'Digital Shopping': ['Apparel', 'High-Tech Gear', 'Home Aesthetics'],
        'Healthcare': ['Premium Coverage', 'Pharmacy Cleared', 'Clinical Consultation']
    }
    investment_vehicles = ['Global Indices Equities', 'Crypto Assets Portfolio', 'Real Estate Trusts', 'Treasury Instruments']
    saving_milestones = ['Emergency Cash Reserves', 'Tax Capital Escrow', 'Venture Deployment Pool']
    
    for current_date in date_series:
        if current_date.day == 1:
            ledger_records.append([current_date, 'Income', 'Salary', 'Corporate Salary', 'Primary Institutional Allocation', 7200.00, 'Corporate Salary', 0, 'None', 'None'])
        if current_date.day == 15 and np.random.rand() > 0.4:
            ledger_records.append([current_date, 'Income', 'Consulting', 'Consulting Advisory', 'Strategic Milestone Advisory Payment', np.random.uniform(1200, 2600), 'Consulting Advisory', 0, 'None', 'None'])
        if current_date.day == 26 and current_date.month % 3 == 0:
            ledger_records.append([current_date, 'Income', 'Capital Yields', 'Equity Dividends', 'Quarterly Portfolio Dividend Matrix payout', np.random.uniform(350, 750), 'Equity Dividends', 0, 'None', 'None'])
            
        if current_date.day == 2:
            ledger_records.append([current_date, 'Expense', 'Housing', 'Mortgage Service', 'Primary Residential Mortgage Debt Settlement', 2100.00, 'None', 2100.00, 'None', 'None'])
            ledger_records.append([current_date, 'Expense', 'Housing', 'Grid Utilities', 'Municipal Power, Water, Fiber Optic Network Matrix', 240.00, 'None', 250.00, 'None', 'None'])
            
        if np.random.rand() > 0.25:
            selected_cat = np.random.choice(list(expense_universe.keys()))
            selected_sub = np.random.choice(expense_universe[selected_cat])
            processed_amount = np.round(np.random.exponential(scale=42.0) + 6.50, 2)
            target_budget = 650.00 if selected_cat in ['Food & Beverage', 'Digital Shopping'] else 350.00
            ledger_records.append([current_date, 'Expense', selected_cat, selected_sub, f"Settlement transaction descriptor to {selected_sub}", processed_amount, 'None', target_budget, 'None', 'None'])
            
        if current_date.day == 5:
            asset_target = np.random.choice(investment_vehicles)
            capital_volume = np.random.uniform(600, 1500)
            ledger_records.append([current_date, 'Investment', 'Asset Allocation', asset_target, f"Capital Conversion -> {asset_target}", capital_volume, 'None', 0, asset_target, 'None'])
            
        if current_date.day == 10:
            milestone_target = np.random.choice(saving_milestones)
            saving_volume = np.random.uniform(300, 800)
            ledger_records.append([current_date, 'Savings', 'Capital Preservation', milestone_target, f"Vault Escrow Transfer -> {milestone_target}", saving_volume, 'None', 0, 'None', milestone_target])

    output_frame = pd.DataFrame(ledger_records, columns=[
        'Date', 'Transaction Type', 'Category', 'Sub Category', 
        'Description', 'Amount', 'Income Source', 'Budget', 'Investment Type', 'Goal Name'
    ])
    output_frame['Date'] = pd.to_datetime(output_frame['Date'])
    return output_frame

if 'fin_data' not in st.session_state:
    st.session_state['fin_data'] = generate_synthetic_ledger()

def execute_pure_linear_forecast(x_data, y_data, steps_forward=6):
    n = len(x_data)
    if n < 2: return np.array([]), np.array([])
    x, y = np.array(x_data, dtype=float), np.array(y_data, dtype=float)
    x_mean, y_mean = np.mean(x), np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    slope = 0 if denominator == 0 else numerator / denominator
    intercept = y_mean - (slope * x_mean)
    future_x = np.array([x[-1] + (i * 30.4) for i in range(1, steps_forward + 1)])
    return future_x, intercept + (slope * future_x)

# =====================================================================
# 3. SIDEBAR STRUCTURE (CLEAN, MINIMALIST UTILITIES ONLY)
# =====================================================================
st.sidebar.markdown("<h2 style='color:#2563EB; font-weight:700;'>💎 Aura</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:0.85rem; color:#64748B; margin-top:-10px;'>System Version: 2026.1</p>", unsafe_allow_html=True)
st.sidebar.divider()

st.sidebar.markdown("### 📥 Document Sync Engine")
uploaded_document = st.sidebar.file_uploader("Upload External Ledger", type=['csv', 'xlsx'])
if uploaded_document is not None:
    try:
        imported_df = pd.read_csv(uploaded_document) if uploaded_document.name.endswith('.csv') else pd.read_excel(uploaded_document)
        imported_df['Date'] = pd.to_datetime(imported_df['Date'])
        st.session_state['fin_data'] = imported_df
        st.sidebar.success("Database engine synchronized.")
    except Exception as e:
        st.sidebar.error(f"Sync Fault: {str(e)}")

search_term = st.sidebar.text_input("📝 Search Line-Item Descriptors", "")

# =====================================================================
# 4. MAIN PAGE ENGINE & PROFESSIONAL HORIZONTAL FILTER BAR
# =====================================================================
st.markdown("<h1 style='color:#0F172A; font-weight:700; margin-bottom: 0.2rem;'>Aura | Financial Command</h1>", unsafe_allow_html=True)

# THE NEW WAY: Horizontal Enterprise Filtering Toolbar
with st.expander("🎛️  Database Filters & Analysis Parameters", expanded=True):
    # Setup 4 distinct tracking columns side-by-side
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    
    active_ledger = st.session_state['fin_data'].copy()
    
    with f_col1:
        absolute_min = active_ledger['Date'].min().to_pydatetime()
        absolute_max = active_ledger['Date'].max().to_pydatetime()
        selected_bounds = st.date_input("Analysis Window", [absolute_min, absolute_max], min_value=absolute_min, max_value=absolute_max)
        if len(selected_bounds) == 2:
            filtered_ledger = active_ledger[(active_ledger['Date'] >= pd.to_datetime(selected_bounds[0])) & (active_ledger['Date'] <= pd.to_datetime(selected_bounds[1]))]
        else:
            filtered_ledger = active_ledger

    with f_col2:
        all_types = list(filtered_ledger['Transaction Type'].unique())
        selected_types = st.multiselect("Transaction Types", options=all_types, default=all_types)
        if selected_types:
            filtered_ledger = filtered_ledger[filtered_ledger['Transaction Type'].isin(selected_types)]

    with f_col3:
        all_categories = list(filtered_ledger['Category'].unique())
        selected_categories = st.multiselect("Isolate Categories", options=all_categories, default=all_categories)
        if selected_categories:
            filtered_ledger = filtered_ledger[filtered_ledger['Category'].isin(selected_categories)]

    with f_col4:
        all_goals = list(filtered_ledger['Goal Name'].unique())
        selected_goals = st.multiselect("Target Milestones", options=all_goals, default=all_goals)
        if selected_goals:
            filtered_ledger = filtered_ledger[filtered_ledger['Goal Name'].isin(selected_goals)]

if search_term:
    filtered_ledger = filtered_ledger[
        filtered_ledger['Description'].str.contains(search_term, case=False, na=False) |
        filtered_ledger['Category'].str.contains(search_term, case=False, na=False)
    ]

def render_kpi_card(title, cash_value, delta_string="", positive_vector=True):
    trend_class = "status-up" if positive_vector else "status-down"
    vector_symbol = "▲" if positive_vector else "▼"
    delta_markup = f'<div class="kpi-subtext {trend_class}">{vector_symbol} {delta_string}</div>' if delta_string else ''
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-label">{title}</div>
        <div class="kpi-val">{cash_value}</div>
        {delta_markup}
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# 5. TAB-BASED ANALYTICS VIEWPORTS
# =====================================================================
tab_exec, tab_expense, tab_income, tab_budget, tab_savings, tab_asset, tab_milestones, tab_predictive, tab_export = st.tabs([
    "📊 Executive Summary", "💸 Expense Analytics", "📈 Inflow Channels", "🛡️ Budget Constraints", 
    "🏦 Savings Vaults", "💼 Asset Allocation", "🎯 Goal Tracks", "🧠 Predictive AI Engine", "💾 Data Export"
])

# --- TAB 1: EXECUTIVE SUMMARY ---
with tab_exec:
    gross_income = filtered_ledger[filtered_ledger['Transaction Type'] == 'Income']['Amount'].sum()
    gross_expenses = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense']['Amount'].sum()
    gross_investments = filtered_ledger[filtered_ledger['Transaction Type'] == 'Investment']['Amount'].sum()
    net_savings = gross_income - gross_expenses
    savings_ratio = (net_savings / gross_income * 100) if gross_income > 0 else 0.0
    calculated_net_worth = gross_income + gross_investments - gross_expenses
    financial_health_index = int(max(10, min(100, (savings_ratio * 1.3) + (65 if gross_expenses < gross_income else 15))))
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    with kpi_col1: render_kpi_card("Total Verified Income", f"${gross_income:,.2f}", "4.8% upward velocity", True)
    with kpi_col2: render_kpi_card("System Structural Burn", f"${gross_expenses:,.2f}", "0.9% optimized baseline", True)
    with kpi_col3: render_kpi_card("Net Capital Retained", f"${net_savings:,.2f}", f"Savings Rate: {savings_ratio:.1f}%", savings_ratio >= 20.0)
    with kpi_col4: render_kpi_card("Estimated Net Worth", f"${calculated_net_worth:,.2f}", f"Health Index: {financial_health_index}/100", financial_health_index > 75)
        
    st.divider()
    
    chart_col_left, chart_col_right = st.columns([2, 1])
    with chart_col_left:
        st.markdown("### Liquidity Flow Dynamics & Cash Intercepts")
        m_dist = filtered_ledger[filtered_ledger['Transaction Type'].isin(['Income', 'Expense'])].groupby([pd.Grouper(key='Date', freq='ME'), 'Transaction Type'])['Amount'].sum().unstack().fillna(0)
        flow_graphic = go.Figure()
        if 'Income' in m_dist.columns:
            flow_graphic.add_trace(go.Scatter(x=m_dist.index, y=m_dist['Income'], name='Total Capital Influx', line=dict(color=COLOR_SECONDARY, width=3.5), stackgroup='one'))
        if 'Expense' in m_dist.columns:
            flow_graphic.add_trace(go.Scatter(x=m_dist.index, y=m_dist['Expense'], name='System Burn Rate', line=dict(color=COLOR_DANGER, width=3)))
        flow_graphic.update_layout(template='plotly_white', margin=dict(l=10, r=10, t=15, b=15), height=360, legend=dict(orientation="h", y=1.1))
        st.plotly_chart(flow_graphic, use_container_width=True)
        
    with chart_col_right:
        st.markdown("### System Health Optimization")
        gauge_graphic = go.Figure(go.Indicator(
            mode="gauge+number", value=financial_health_index, domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': COLOR_MUTED},
                'bar': {'color': COLOR_PRIMARY, 'thickness': 0.25}, 'bgcolor': "white", 'borderwidth': 1, 'bordercolor': "#E2E8F0",
                'steps': [{'range': [0, 45], 'color': '#FFE4E6'}, {'range': [45, 75], 'color': '#FEF3C7'}, {'range': [75, 100], 'color': '#D1FAE5'}]
            }
        ))
        gauge_graphic.update_layout(margin=dict(l=20, r=20, t=30, b=10), height=310)
        st.plotly_chart(gauge_graphic, use_container_width=True)

# --- TAB 2: EXPENSE ANALYTICS ---
with tab_expense:
    expense_superset = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense']
    if not expense_superset.empty:
        view_col_left, view_col_right = st.columns(2)
        with view_col_left:
            st.markdown("### Structural Distribution Density")
            donut_graphic = px.pie(expense_superset, values='Amount', names='Category', hole=0.55, color_discrete_sequence=px.colors.qualitative.G10)
            st.plotly_chart(donut_graphic, use_container_width=True)
        with view_col_right:
            st.markdown("### Granular Spending Hierarchy")
            treemap_graphic = px.treemap(expense_superset, path=['Category', 'Sub Category'], values='Amount', color='Amount', color_continuous_scale='Purples')
            st.plotly_chart(treemap_graphic, use_container_width=True)
    else:
        st.info("No expense tracking data falls within active filter states.")

# --- TAB 3: INFLOW CHANNELS ---
with tab_income:
    income_superset = filtered_ledger[filtered_ledger['Transaction Type'] == 'Income']
    if not income_superset.empty:
        col_inc_left, col_inc_right = st.columns([1, 2])
        with col_inc_left:
            st.markdown("### Input Vector Contributions")
            income_share_graphic = px.pie(income_superset, values='Amount', names='Income Source', hole=0.4)
            st.plotly_chart(income_share_graphic, use_container_width=True)
        with col_inc_right:
            st.markdown("### Inflow Channels Stack Velocity")
            m_inc_streams = income_superset.groupby([pd.Grouper(key='Date', freq='ME'), 'Income Source'])['Amount'].sum().unstack().fillna(0)
            income_bar_graphic = px.bar(m_inc_streams, x=m_inc_streams.index, y=m_inc_streams.columns, color_discrete_sequence=px.colors.sequential.Agsunset)
            income_bar_graphic.update_layout(template='plotly_white', barmode='stack')
            st.plotly_chart(income_bar_graphic, use_container_width=True)
    else:
        st.info("No verified income records found in isolated sub-matrices.")

# --- TAB 4: BUDGET CONSTRAINTS ---
with tab_budget:
    exp_data = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense']
    if not exp_data.empty:
        budget_matrix = exp_data.groupby('Category').agg({'Amount':'sum', 'Budget':'first'}).reset_index()
        budget_matrix['Budget'] = budget_matrix['Budget'].apply(lambda val: val if val > 0 else 1350.00)
        budget_matrix['Utilization %'] = (budget_matrix['Amount'] / budget_matrix['Budget']) * 100
        budget_matrix['Net Variance'] = budget_matrix['Budget'] - budget_matrix['Amount']
        
        comparison_bar = go.Figure()
        comparison_bar.add_trace(go.Bar(name='Assigned Guardrail', x=budget_matrix['Category'], y=budget_matrix['Budget'], marker_color='#E2E8F0'))
        comparison_bar.add_trace(go.Bar(name='Realized Incurred Capital', x=budget_matrix['Category'], y=budget_matrix['Amount'], marker_color=COLOR_PRIMARY))
        comparison_bar.update_layout(barmode='group', template='plotly_white')
        st.plotly_chart(comparison_bar, use_container_width=True)
        st.dataframe(budget_matrix.style.format({'Amount': '${:,.2f}', 'Budget': '${:,.2f}', 'Utilization %': '{:.1f}%', 'Net Variance': '${:,.2f}'}), use_container_width=True)
    else:
        st.info("No historical budget vectors found in standard scope constraints.")

# --- TAB 5: SAVINGS VAULTS ---
with tab_savings:
    sav_data = filtered_ledger[filtered_ledger['Transaction Type'] == 'Savings']
    if not sav_data.empty:
        m_sav_accum = sav_data.groupby(pd.Grouper(key='Date', freq='ME'))['Amount'].sum().reset_index()
        m_sav_accum['Compound Growth Curve'] = m_sav_accum['Amount'].cumsum()
        v_col_l, v_col_r = st.columns([2, 1])
        with v_col_l:
            growth_area_chart = px.area(m_sav_accum, x='Date', y='Compound Growth Curve', color_discrete_sequence=[COLOR_SECONDARY])
            st.plotly_chart(growth_area_chart, use_container_width=True)
        with v_col_r:
            tot_liquid = m_sav_accum['Amount'].sum()
            st.metric("Consolidated Escrow Cash Balance", f"${tot_liquid:,.2f}")
            st.progress(min(1.0, tot_liquid / 30000.0))
    else:
        st.info("No transaction traces linked to capital preservation vaults.")

# --- TAB 6: ASSET ALLOCATION ---
with tab_asset:
    inv_data = filtered_ledger[filtered_ledger['Transaction Type'] == 'Investment']
    if not inv_data.empty:
        inv_summary = inv_data.groupby('Investment Type')['Amount'].sum().reset_index()
        a_col_l, a_col_r = st.columns(2)
        with a_col_l:
            risk_pie_chart = px.pie(inv_summary, values='Amount', names='Investment Type', color_discrete_sequence=px.colors.sequential.Darkmint)
            st.plotly_chart(risk_pie_chart, use_container_width=True)
        with a_col_r:
            cum_inv = inv_data.groupby([pd.Grouper(key='Date', freq='ME'), 'Investment Type'])['Amount'].sum().unstack().fillna(0).cumsum()
            asset_line_chart = px.line(cum_inv, x=cum_inv.index, y=cum_inv.columns)
            st.plotly_chart(asset_line_chart, use_container_width=True)
    else:
        st.info("No active capital deployments identified in portfolio tracks.")

# --- TAB 7: GOAL TRACKS ---
with tab_milestones:
    milestone_aggregates = filtered_ledger[filtered_ledger['Transaction Type'] == 'Savings'].groupby('Goal Name')['Amount'].sum().reset_index()
    milestone_aggregates = milestone_aggregates[milestone_aggregates['Goal Name'] != 'None']
    if not milestone_aggregates.empty:
        capital_target_index = {'Emergency Cash Reserves': 25000, 'Tax Capital Escrow': 15000, 'Venture Deployment Pool': 60000}
        milestone_aggregates['Target Benchmark'] = milestone_aggregates['Goal Name'].map(capital_target_index).fillna(40000)
        milestone_aggregates['Completion Index Ratio'] = (milestone_aggregates['Amount'] / milestone_aggregates['Target Benchmark']) * 100
        for _, milestone_row in milestone_aggregates.iterrows():
            st.markdown(f"#### 🎯 Target: {milestone_row['Goal Name']}")
            st.progress(min(1.0, milestone_row['Completion Index Ratio'] / 100.0))
            st.markdown(f"Secured Allocation: **${milestone_row['Amount']:,.2f}** / Goal Benchmark: **${milestone_row['Target Benchmark']:,.2f}** ({milestone_row['Completion Index Ratio']:.1f}% Fulfilled)")
            st.divider()
    else:
        st.info("No active investment milestone definitions found.")

# --- TAB 8: PREDICTIVE AI ENGINE ---
with tab_predictive:
    st.markdown("### 📈 Closed-Form Trend Regression Projections")
    m_burn_series = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense'].groupby(pd.Grouper(key='Date', freq='ME'))['Amount'].sum().reset_index()
    if len(m_burn_series) >= 3:
        m_burn_series['Ordinal_Time_Vector'] = m_burn_series['Date'].map(datetime.date.toordinal)
        future_ordinals, projected_burns = execute_pure_linear_forecast(m_burn_series['Ordinal_Time_Vector'].values, m_burn_series['Amount'].values, steps_forward=6)
        extrapolated_timeline = [datetime.date.fromordinal(int(val)) for val in future_ordinals]
        forecast_graphic = go.Figure()
        forecast_graphic.add_trace(go.Scatter(x=m_burn_series['Date'], y=m_burn_series['Amount'].values, name='Incurred Burn', line=dict(color=COLOR_PRIMARY, width=3.5)))
        forecast_graphic.add_trace(go.Scatter(x=extrapolated_timeline, y=projected_burns, name='Trend Forecast', line=dict(color=COLOR_ACCENT, dash='dash', width=3)))
        st.plotly_chart(forecast_graphic, use_container_width=True)
    else:
        st.info("Provide at least 3 months of historical data entries to execute structural line forecasts.")

# --- TAB 9: DATA EXPORT ---
with tab_export:
    st.dataframe(filtered_ledger, use_container_width=True)
    io_buf = io.StringIO()
    filtered_ledger.to_csv(io_buf, index=False)
    st.download_button(label="📥 Download Extracted Settlement CSV Ledger", data=io_buf.getvalue().encode('utf-8'), file_name="Aura_Extract.csv", mime="text/csv")
