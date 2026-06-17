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
    page_title="AuraFinance | Intelligence Suite",
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
COLOR_BG_CARD = "#FFFFFF"

def inject_premium_css():
    """Injects commercial grade structural layout styling mimicking premium platforms."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #F8FAFC;
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
        
        /* Structural Layout Utility */
        div[data-testid="stSidebarUserContent"] {
            padding-top: 2rem;
        }
        
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.2s;
        }
        
        /* Clean Interface Utilities */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

inject_premium_css()

# =====================================================================
# 2. SEED ENGINES & REALISTIC SYNTHETIC LEDGER GENERATOR
# =====================================================================
@st.cache_data
def generate_synthetic_ledger():
    """Generates a perfectly correlated, multi-variate continuous financial ledger covering 365 days."""
    np.random.seed(101)
    today = datetime.date.today()
    start_time = today - datetime.timedelta(days=365)
    date_series = pd.date_range(start_time, today, freq='D')
    
    ledger_records = []
    
    # Structural Mapping Arrays
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
        # Core Regular Cash Inflows
        if current_date.day == 1:
            ledger_records.append([current_date, 'Income', 'Salary', 'Corporate Salary', 'Primary Institutional Allocation', 7200.00, 'Corporate Salary', 0, 'None', 'None'])
        if current_date.day == 15 and np.random.rand() > 0.4:
            ledger_records.append([current_date, 'Income', 'Consulting', 'Consulting Advisory', 'Strategic Milestone Advisory Payment', np.random.uniform(1200, 2600), 'Consulting Advisory', 0, 'None', 'None'])
        if current_date.day == 26 and current_date.month % 3 == 0:
            ledger_records.append([current_date, 'Income', 'Capital Yields', 'Equity Dividends', 'Quarterly Portfolio Dividend Matrix payout', np.random.uniform(350, 750), 'Equity Dividends', 0, 'None', 'None'])
            
        # Core Regular Structural Burns
        if current_date.day == 2:
            ledger_records.append([current_date, 'Expense', 'Housing', 'Mortgage Service', 'Primary Residential Mortgage Debt Settlement', 2100.00, 'None', 2100.00, 'None', 'None'])
            ledger_records.append([current_date, 'Expense', 'Housing', 'Grid Utilities', 'Municipal Power, Water, Fiber Optic Network Matrix', 240.00, 'None', 250.00, 'None', 'None'])
            
        # Variable Discrete Consumer Burns
        if np.random.rand() > 0.25:  # 75% transactional velocity saturation
            selected_cat = np.random.choice(list(expense_universe.keys()))
            selected_sub = np.random.choice(expense_universe[selected_cat])
            processed_amount = np.round(np.random.exponential(scale=42.0) + 6.50, 2)
            
            # Allocation matrices for dynamic targeting budgets
            target_budget = 650.00 if selected_cat in ['Food & Beverage', 'Digital Shopping'] else 350.00
            ledger_records.append([current_date, 'Expense', selected_cat, selected_sub, f"Settlement transaction descriptor to {selected_sub}", processed_amount, 'None', target_budget, 'None', 'None'])
            
        # Programmatic Asset Layer Swaps
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

# =====================================================================
# 3. ROBUST PURE MATHEMATICAL CLOSED-FORM REGRESSION ENGINE (No Sklearn)
# =====================================================================
def execute_pure_linear_forecast(x_data, y_data, steps_forward=6):
    """Executes a pure algebraic Ordinary Least Squares projection using closed-form matrix math."""
    n = len(x_data)
    if n < 2:
        return np.array([]), np.array([])
    
    x = np.array(x_data, dtype=float)
    y = np.array(y_data, dtype=float)
    
    # Calculate slopes and intercepts algebraically: beta = Cov(X,Y)/Var(X)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    
    if denominator == 0:
        slope = 0
        intercept = y_mean
    else:
        slope = numerator / denominator
        intercept = y_mean - (slope * x_mean)
        
    # Extrapolate values linearly
    last_x = x[-1]
    # Build forward steps assuming monthly average index spacing (~30.4 days ordinal)
    future_x = np.array([last_x + (i * 30.4) for i in range(1, steps_forward + 1)])
    projected_y = intercept + (slope * future_x)
    
    return future_x, projected_y

# =====================================================================
# 4. GLOBAL FILTER CONTROL RUNTIME
# =====================================================================
st.sidebar.markdown("<h2 style='color:#2563EB; font-weight:700;'>💎 AuraFinance</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:0.85rem; color:#64748B; margin-top:-10px;'>System Version: 2026.1</p>", unsafe_allow_html=True)
st.sidebar.divider() #  THIS FIXES IT CLEANLY
# Navigation Controller Matrix
dashboard_view = st.sidebar.radio(
    "Control Panels",
    [
        "Executive Summary", 
        "Expense Intelligence", 
        "Inflow Channels", 
        "Budget Limits", 
        "Savings Vaults", 
        "Asset Allocation", 
        "Target Milestones", 
        "Predictive AI Matrix", 
        "Clearing & Exports"
    ]
)

st.sidebar.hr()
st.sidebar.markdown("### 📥 Transaction Document Sync")
uploaded_document = st.sidebar.file_uploader("Upload External Transaction Ledger", type=['csv', 'xlsx'])

# Session Persistence Architecture
if uploaded_document is not None:
    try:
        if uploaded_document.name.endswith('.csv'):
            imported_df = pd.read_csv(uploaded_document)
        else:
            imported_df = pd.read_excel(uploaded_document)
            
        required_schema = ['Date', 'Transaction Type', 'Category', 'Amount']
        if all(col in imported_df.columns for col in required_schema):
            imported_df['Date'] = pd.to_datetime(imported_df['Date'])
            st.session_state['fin_data'] = imported_df
            st.sidebar.success("Database engine synchronized cleanly.")
        else:
            st.sidebar.error("Schema Mismatch. Critical tracking vector dropped.")
    except Exception as error_msg:
        st.sidebar.error(f"Sync Fault: {str(error_msg)}")

active_ledger = st.session_state['fin_data'].copy()

# Date Windowing Selection Pipelines
st.sidebar.markdown("### 🗓️ Macro Date Bounds")
absolute_min = active_ledger['Date'].min().to_pydatetime()
absolute_max = active_ledger['Date'].max().to_pydatetime()
selected_bounds = st.sidebar.date_input("Analysis Window", [absolute_min, absolute_max], min_value=absolute_min, max_value=absolute_max)

if len(selected_bounds) == 2:
    start_window, end_window = pd.to_datetime(selected_bounds[0]), pd.to_datetime(selected_bounds[1])
    filtered_ledger = active_ledger[(active_ledger['Date'] >= start_window) & (active_ledger['Date'] <= end_window)]
else:
    filtered_ledger = active_ledger

# Global Omni-Search Integration
search_term = st.sidebar.text_input("🔍 Search Line-Item Descriptors", "")
if search_term:
    filtered_ledger = filtered_ledger[
        filtered_ledger['Description'].str.contains(search_term, case=False, na=False) |
        filtered_ledger['Category'].str.contains(search_term, case=False, na=False)
    ]

# Component UI Blueprint Generator
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
# 5. DASHBOARD VIEW CONTROLLERS & ENGINE GRAPHICS
# =====================================================================

# --- SECTION 1: EXECUTIVE SUMMARY ---
if dashboard_view == "Executive Summary":
    st.markdown('<div class="main-header">Executive Financial Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Real-time enterprise balance optimization tracking cross-system operations.</div>', unsafe_allow_html=True)
    
    # Mathematical aggregation processing
    gross_income = filtered_ledger[filtered_ledger['Transaction Type'] == 'Income']['Amount'].sum()
    gross_expenses = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense']['Amount'].sum()
    gross_investments = filtered_ledger[filtered_ledger['Transaction Type'] == 'Investment']['Amount'].sum()
    net_savings = gross_income - gross_expenses
    savings_ratio = (net_savings / gross_income * 100) if gross_income > 0 else 0.0
    calculated_net_worth = gross_income + gross_investments - gross_expenses
    financial_health_index = int(max(10, min(100, (savings_ratio * 1.3) + (65 if gross_expenses < gross_income else 15))))
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    with kpi_col1:
        render_kpi_card("Total Verified Income", f"${gross_income:,.2f}", "4.8% upward drift vector", True)
    with kpi_col2:
        render_kpi_card("System Structural Burn", f"${gross_expenses:,.2f}", "0.9% system optimization save", True)
    with kpi_col3:
        render_kpi_card("Net Capital Retained", f"${net_savings:,.2f}", f"Savings Rate: {savings_ratio:.1f}%", savings_ratio >= 20.0)
    with kpi_col4:
        render_kpi_card("Estimated Capital Net Worth", f"${calculated_net_worth:,.2f}", f"Health Index Score: {financial_health_index}/100", financial_health_index > 75)
        
    st.markdown("---")
    
    chart_col_left, chart_col_right = st.columns([2, 1])
    with chart_col_left:
        st.markdown("### Liquidity Flow Dynamics & Cash Intercepts")
        monthly_distribution = filtered_ledger[filtered_ledger['Transaction Type'].isin(['Income', 'Expense'])].groupby([pd.Grouper(key='Date', freq='ME'), 'Transaction Type'])['Amount'].sum().unstack().fillna(0)
        
        flow_graphic = go.Figure()
        flow_graphic.add_trace(go.Scatter(x=monthly_distribution.index, y=monthly_distribution['Income'], name='Total Capital Influx', line=dict(color=COLOR_SECONDARY, width=3.5), stackgroup='one'))
        flow_graphic.add_trace(go.Scatter(x=monthly_distribution.index, y=monthly_distribution['Expense'], name='System Burn Rate', line=dict(color=COLOR_DANGER, width=3)))
        flow_graphic.update_layout(template='plotly_white', margin=dict(l=10, r=10, t=15, b=15), height=360, legend=dict(orientation="h", y=1.1))
        st.plotly_chart(flow_graphic, use_container_width=True)
        
    with chart_col_right:
        st.markdown("### System Health Optimization Gauge")
        gauge_graphic = go.Figure(go.Indicator(
            mode="gauge+number",
            value=financial_health_index,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': COLOR_MUTED},
                'bar': {'color': COLOR_PRIMARY, 'thickness': 0.25},
                'bgcolor': "white",
                'borderwidth': 1,
                'bordercolor': "#E2E8F0",
                'steps': [
                    {'range': [0, 45], 'color': '#FFE4E6'},
                    {'range': [45, 75], 'color': '#FEF3C7'},
                    {'range': [75, 100], 'color': '#D1FAE5'}
                ]
            }
        ))
        gauge_graphic.update_layout(margin=dict(l=20, r=20, t=30, b=10), height=310)
        st.plotly_chart(gauge_graphic, use_container_width=True)
        
    st.markdown("### Operational Capital Flow Topography (Sankey Matrix Diagram)")
    expense_aggregates = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense'].groupby('Category')['Amount'].sum().reset_index()
    income_aggregates = filtered_ledger[filtered_ledger['Transaction Type'] == 'Income'].groupby('Category')['Amount'].sum().reset_index()
    
    nodes_list = ["Total Pipeline Allocation"] + list(income_aggregates['Category']) + ["Central Treasury Wallet"] + list(expense_aggregates['Category']) + ["Preserved Wealth Vault"]
    sankey_links = []
    
    for _, row in income_aggregates.iterrows():
        sankey_links.append({'source': nodes_list.index(row['Category']), 'target': nodes_list.index("Central Treasury Wallet"), 'value': row['Amount']})
    for _, row in expense_aggregates.iterrows():
        sankey_links.append({'source': nodes_list.index("Central Treasury Wallet"), 'target': nodes_list.index(row['Category']), 'value': row['Amount']})
    if net_savings > 0:
        sankey_links.append({'source': nodes_list.index("Central Treasury Wallet"), 'target': nodes_list.index("Preserved Wealth Vault"), 'value': net_savings})
        
    sankey_graphic = go.Figure(data=[go.Sankey(
        node=dict(pad=20, thickness=18, line=dict(color="#0F172A", width=0.3), label=nodes_list, color=COLOR_PRIMARY),
        link=dict(source=[link['source'] for link in sankey_links], target=[link['target'] for link in sankey_links], value=[link['value'] for link in sankey_links], color="rgba(226, 232, 240, 0.75)")
    )])
    sankey_graphic.update_layout(margin=dict(l=10, r=10, t=15, b=15), height=380)
    st.plotly_chart(sankey_graphic, use_container_width=True)

# --- SECTION 2: EXPENSE INTELLIGENCE ---
elif dashboard_view == "Expense Intelligence":
    st.markdown('<div class="main-header">Expense System Diagnostics</div>', unsafe_allow_html=True)
    expense_superset = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense']
    
    chosen_categories = st.multiselect("Isolate Category Analysis Vectors", options=list(expense_superset['Category'].unique()), default=list(expense_superset['Category'].unique())[:4])
    if chosen_categories:
        expense_superset = expense_superset[expense_superset['Category'].isin(chosen_categories)]
        
    view_col_left, view_col_right = st.columns(2)
    with view_col_left:
        st.markdown("### Structural Distribution Density")
        donut_graphic = px.pie(expense_superset, values='Amount', names='Category', hole=0.55, color_discrete_sequence=px.colors.qualitative.G10)
        donut_graphic.update_layout(margin=dict(l=10, r=10, t=15, b=15))
        st.plotly_chart(donut_graphic, use_container_width=True)
        
    with view_col_right:
        st.markdown("### Granular Spending Hierarchy (Hierarchical Treemap)")
        treemap_graphic = px.treemap(expense_superset, path=['Category', 'Sub Category'], values='Amount', color='Amount', color_continuous_scale='Purples')
        treemap_graphic.update_layout(margin=dict(l=10, r=10, t=15, b=15))
        st.plotly_chart(treemap_graphic, use_container_width=True)
        
    st.markdown("---")
    st.markdown("### Temporal System Outflow Density Matrix (Heatmap Grid)")
    expense_superset = expense_superset.copy()
    expense_superset['Day of Week'] = expense_superset['Date'].dt.day_name()
    expense_superset['Calendar Month'] = expense_superset['Date'].dt.strftime('%b %Y')
    heatmap_matrix = expense_superset.groupby(['Day of Week', 'Calendar Month'])['Amount'].sum().unstack().fillna(0)
    
    day_sorting_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_matrix = heatmap_matrix.reindex(intersection := [d for d in day_sorting_order if d in heatmap_matrix.index])
    
    heatmap_graphic = px.imshow(heatmap_matrix, labels=dict(x="Chronological Axis", y="Weekly Footprint Matrix", color="Burn Intensity ($)"), color_continuous_scale='YlOrRd')
    heatmap_graphic.update_layout(margin=dict(l=10, r=10, t=20, b=20), height=380)
    st.plotly_chart(heatmap_graphic, use_container_width=True)

# --- SECTION 3: INFLOW CHANNELS ---
elif dashboard_view == "Inflow Channels":
    st.markdown('<div class="main-header">Income Analytics & Expansion Engines</div>', unsafe_allow_html=True)
    income_superset = filtered_ledger[filtered_ledger['Transaction Type'] == 'Income']
    
    col_inc_left, col_inc_right = st.columns([1, 2])
    with col_inc_left:
        st.markdown("### Input Vector Contributions")
        income_share_graphic = px.pie(income_superset, values='Amount', names='Income Source', hole=0.4, color_discrete_sequence=[COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT])
        st.plotly_chart(income_share_graphic, use_container_width=True)
        
    with col_inc_right:
        st.markdown("### Inflow Channels Stack Velocity")
        monthly_income_streams = income_superset.groupby([pd.Grouper(key='Date', freq='ME'), 'Income Source'])['Amount'].sum().unstack().fillna(0)
        income_bar_graphic = px.bar(monthly_income_streams, x=monthly_income_streams.index, y=monthly_income_streams.columns, color_discrete_sequence=px.colors.sequential.Agsunset)
        income_bar_graphic.update_layout(template='plotly_white', barmode='stack', margin=dict(l=10, r=10, t=15, b=15))
        st.plotly_chart(income_bar_graphic, use_container_width=True)

# --- SECTION 4: BUDGET LIMITS ---
elif dashboard_view == "Budget Limits":
    st.markdown('<div class="main-header">Operational Threshold Engine Matrix</div>', unsafe_allow_html=True)
    
    budget_matrix = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense'].groupby('Category').agg({'Amount':'sum', 'Budget':'first'}).reset_index()
    budget_matrix['Budget'] = budget_matrix['Budget'].apply(lambda val: val if val > 0 else 1350.00)
    budget_matrix['Utilization %'] = (budget_matrix['Amount'] / budget_matrix['Budget']) * 100
    budget_matrix['Net Variance'] = budget_matrix['Budget'] - budget_matrix['Amount']
    
    st.markdown("### Realized Consumer Spending vs Risk Threshold Constraints")
    comparison_bar = go.Figure()
    comparison_bar.add_trace(go.Bar(name='Assigned Threshold Guardrail', x=budget_matrix['Category'], y=budget_matrix['Budget'], marker_color='#E2E8F0'))
    comparison_bar.add_trace(go.Bar(name='Realized Incurred Capital', x=budget_matrix['Category'], y=budget_matrix['Amount'], marker_color=COLOR_PRIMARY))
    comparison_bar.update_layout(barmode='group', template='plotly_white', margin=dict(l=10, r=10, t=15, b=15))
    st.plotly_chart(comparison_bar, use_container_width=True)
    
    st.markdown("### 🚨 System Exceptions & Leakage Indicators")
    for _, budget_row in budget_matrix.iterrows():
        if budget_row['Utilization %'] > 100.0:
            st.error(f"**Critical Capital Overrun**: The sector tracking **{budget_row['Category']}** crossed threshold tolerances by **{budget_row['Utilization %']-100:.1f}%** (Deficit Framework: -${abs(budget_row['Net Variance']):,.2f})")
        elif budget_row['Utilization %'] > 85.0:
            st.warning(f"**Approaching Allocation Boundary**: Sector **{budget_row['Category']}** is reporting high saturation at **{budget_row['Utilization %']:.1f}%** (Safe Space: ${budget_row['Net Variance']:,.2f})")
            
    st.dataframe(budget_matrix.style.format({'Amount': '${:,.2f}', 'Budget': '${:,.2f}', 'Utilization %': '{:.1f}%', 'Net Variance': '${:,.2f}'}), use_container_width=True)

# --- SECTION 5: SAVINGS VAULTS ---
elif dashboard_view == "Savings Vaults":
    st.markdown('<div class="main-header">Liquid Preservation Vaults & Runways</div>', unsafe_allow_html=True)
    
    savings_superset = filtered_ledger[filtered_ledger['Transaction Type'] == 'Savings']
    monthly_vault_accumulation = savings_superset.groupby(pd.Grouper(key='Date', freq='ME'))['Amount'].sum().reset_index()
    
    vault_col_left, vault_col_right = st.columns([2, 1])
    with vault_col_left:
        st.markdown("### Cumulative Capital Runways Scaling")
        monthly_vault_accumulation['Compound Growth Curve'] = monthly_vault_accumulation['Amount'].cumsum()
        growth_area_chart = px.area(monthly_vault_accumulation, x='Date', y='Compound Growth Curve', color_discrete_sequence=[COLOR_SECONDARY])
        growth_area_chart.update_layout(template='plotly_white', margin=dict(l=10, r=10, t=15, b=15))
        st.plotly_chart(growth_area_chart, use_container_width=True)
        
    with vault_col_right:
        st.markdown("### Operational Resiliency Indexes")
        total_liquid_escrow = monthly_vault_accumulation['Amount'].sum()
        safety_reserve_ceiling = 30000.00
        saturation_percentage = min(100.0, (total_liquid_escrow / safety_reserve_ceiling) * 100)
        
        st.metric("Consolidated Escrow Cash Balance", f"${total_liquid_escrow:,.2f}")
        st.metric("Resiliency Threshold Ceiling Target", f"${safety_reserve_ceiling:,.2f}")
        st.progress(saturation_percentage / 100.0)
        st.markdown(f"Vault infrastructure retains **{saturation_percentage:.1f}%** of targeted security baseline.")

# --- SECTION 6: ASSET ALLOCATION ---
elif dashboard_view == "Asset Allocation":
    st.markdown('<div class="main-header">Portfolio Capitalization Engine</div>', unsafe_allow_html=True)
    investment_superset = filtered_ledger[filtered_ledger['Transaction Type'] == 'Investment']
    investment_summary_matrix = investment_superset.groupby('Investment Type')['Amount'].sum().reset_index()
    
    asset_col_l, asset_col_r = st.columns(2)
    with asset_col_l:
        st.markdown("### Dynamic Structural Risk Stratification")
        risk_pie_chart = px.pie(investment_summary_matrix, values='Amount', names='Investment Type', color_discrete_sequence=px.colors.sequential.Darkmint)
        st.plotly_chart(risk_pie_chart, use_container_width=True)
        
    with asset_col_r:
        st.markdown("### Cumulative Conversion Velocities")
        cumulative_investment_timelines = investment_superset.groupby([pd.Grouper(key='Date', freq='ME'), 'Investment Type'])['Amount'].sum().unstack().fillna(0).cumsum()
        asset_line_chart = px.line(cumulative_investment_timelines, x=cumulative_investment_timelines.index, y=cumulative_investment_timelines.columns, color_discrete_sequence=px.colors.qualitative.Dark2)
        asset_line_chart.update_layout(template='plotly_white', margin=dict(l=10, r=10, t=15, b=15))
        st.plotly_chart(asset_line_chart, use_container_width=True)

# --- SECTION 7: TARGET MILESTONES ---
elif dashboard_view == "Target Milestones":
    st.markdown('<div class="main-header">Strategic Objective Trackers</div>', unsafe_allow_html=True)
    milestone_aggregates = filtered_ledger[filtered_ledger['Transaction Type'] == 'Savings'].groupby('Goal Name')['Amount'].sum().reset_index()
    milestone_aggregates = milestone_aggregates[milestone_aggregates['Goal Name'] != 'None']
    
    capital_target_index = {'Emergency Cash Reserves': 25000, 'Tax Capital Escrow': 15000, 'Venture Deployment Pool': 60000}
    milestone_aggregates['Target Benchmark'] = milestone_aggregates['Goal Name'].map(capital_target_index).fillna(40000)
    milestone_aggregates['Completion Index Ratio'] = (milestone_aggregates['Amount'] / milestone_aggregates['Target Benchmark']) * 100
    
    for _, milestone_row in milestone_aggregates.iterrows():
        st.markdown(f"#### 🎯 Target: {milestone_row['Goal Name']}")
        normalized_ratio = min(1.0, milestone_row['Completion Index Ratio'] / 100.0)
        st.progress(normalized_ratio)
        st.markdown(f"Secured Vault Allocation: **${milestone_row['Amount']:,.2f}** / Absolute Goal Benchmark: **${milestone_row['Target Benchmark']:,.2f}** ({milestone_row['Completion Index Ratio']:.1f}% Fulfilled)")
        st.markdown("---")

# --- SECTION 8: PREDICTIVE AI MATRIX ---
elif dashboard_view == "Predictive AI Matrix":
    st.markdown('<div class="main-header">Predictive Mathematical Modelling & AI Analytics</div>', unsafe_allow_html=True)
    
    st.markdown("### 📈 Closed-Form Trend Regression Projections (180-Day Structural Runways)")
    monthly_burn_series = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense'].groupby(pd.Grouper(key='Date', freq='ME'))['Amount'].sum().reset_index()
    
    if len(monthly_burn_series) >= 3:
        # Construct sequential ordinal data tracking for our pure algebraic equation matrix
        monthly_burn_series['Ordinal_Time_Vector'] = monthly_burn_series['Date'].map(datetime.date.toordinal)
        raw_x = monthly_burn_series['Ordinal_Time_Vector'].values
        raw_y = monthly_burn_series['Amount'].values
        
        future_ordinals, projected_burns = execute_pure_linear_forecast(raw_x, raw_y, steps_forward=6)
        
        # Format dates back out of ordinal frameworks cleanly
        extrapolated_timeline = [datetime.date.fromordinal(int(val)) for val in future_ordinals]
        
        forecast_graphic = go.Figure()
        forecast_graphic.add_trace(go.Scatter(x=monthly_burn_series['Date'], y=raw_y, name='Verified Historical Incurred Burn', line=dict(color=COLOR_PRIMARY, width=3.5)))
        forecast_graphic.add_trace(go.Scatter(x=extrapolated_timeline, y=projected_burns, name='Algorithmic Trend Forecast', line=dict(color=COLOR_ACCENT, dash='dash', width=3)))
        forecast_graphic.update_layout(template='plotly_white', margin=dict(l=10, r=10, t=15, b=15))
        st.plotly_chart(forecast_graphic, use_container_width=True)
    else:
        st.info("Insufficient system historical iterations to construct high-confidence predictive algorithms. Extend the date boundaries.")
        
    st.markdown("### 🤖 Continuous Automated System Audit Logs")
    total_inflows_computed = filtered_ledger[filtered_ledger['Transaction Type'] == 'Income']['Amount'].sum()
    total_outflows_computed = filtered_ledger[filtered_ledger['Transaction Type'] == 'Expense']['Amount'].sum()
    lifestyle_dining_burn = filtered_ledger[(filtered_ledger['Category'] == 'Food & Beverage') & (filtered_ledger['Transaction Type'] == 'Expense')]['Amount'].sum()
    
    st.markdown("""
    <div class="ai-insight-panel">
        <h4 style="color:#0F172A; margin-top:0;">💡 Autonomous Heuristic Optimization Insights</h4>
        <p style="color:#334155; font-size:0.95rem;">System metrics matched structural models against default capital efficiency ratios:</p>
    </div>
    """, unsafe_allow_html=True)
    
    if lifestyle_dining_burn > (0.15 * total_inflows_computed):
        st.markdown(f"* 🛑 **Warning: Discretionary Consumption Outliers Found**: Food & Dining channels consume **{(lifestyle_dining_burn/total_inflows_computed)*100:.1f}%** of total system velocity. Instituting a targeted scaling profile could redirect an estimated **${lifestyle_dining_burn * 0.25:,.2f}** per quarter into active investments.")
    if total_outflows_computed > (total_inflows_computed * 0.78):
        st.markdown("* ⚠️ **High System Saturation Notice**: Current system operational costs cross 78% of structural revenue capacity. Recommend immediate validation of optional non-core subscription tiers.")
    else:
        st.markdown("* 💎 **Optimal Efficiency Score Verified**: Capital retention velocities match high-performance profiles. Surplus liquid cash buffers can safely absorb higher venture or public index exposure vectors.")

# --- SECTION 9: CLEARING & EXPORTS ---
elif dashboard_view == "Clearing & Exports":
    st.markdown('<div class="main-header">System Extraction Engine</div>', unsafe_allow_html=True)
    st.markdown("Isolate, filter, verify, and export internal database ledgers into standards-compliant formats.")
    
    st.markdown("### Live Operational Database Frame View")
    st.dataframe(filtered_ledger, use_container_width=True)
    
    # In-memory serialization pipeline mechanics
    io_string_buffer = io.StringIO()
    filtered_ledger.to_csv(io_string_buffer, index=False)
    processed_csv_payload = io_string_buffer.getvalue().encode('utf-8')
    
    st.download_button(
        label="📥 Download Verified CSV Settlement Ledger",
        data=processed_csv_payload,
        file_name="AuraFinance_Settlement_Ledger.csv",
        mime="text/csv"
    )
