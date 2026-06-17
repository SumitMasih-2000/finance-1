import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime

# =====================================================================
# 1. APPLICATION ARCHITECTURE & THEME ENGINE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Money T - Dashboard Suite",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_moneyt_template_theme():
    """Injects high-fidelity stylesheets matching the template light mode."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
        /* Master Main Canvas Settings (Clean Gray-White Canvas) */
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
            min-height: 145px;
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
        .kpi-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.2rem 0.4rem;
            border-radius: 6px;
            font-size: 0.72rem;
            font-weight: 600;
            margin-top: 0.6rem;
        }
        .badge-inc { background-color: #DCFCE7; color: #16A34A; }
        
        .border-purple { border-top: 4px solid #6366F1; }
        .border-orange { border-top: 4px solid #F97316; }
        .border-teal { border-top: 4px solid #06B6D4; }
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
# 2. RUNTIME COMPLETE FINANCIAL DATA ENGINE
# =====================================================================
@st.cache_data
def get_clean_mock_dataset():
    np.random.seed(42)
    today = datetime.date.today()
    date_range = pd.date_range(end=today, periods=30, freq='D')
    
    income_curve = 550 + 120 * np.sin(np.linspace(0, 2*np.pi, 30)) + np.random.normal(0, 10, 30)
    expense_curve = 380 + 90 * np.cos(np.linspace(0, 2*np.pi, 30)) + np.random.normal(0, 8, 30)
    
    df_trends = pd.DataFrame({'Date': date_range, 'Income': income_curve, 'Expense': expense_curve})
    
    ledger_records = [
        {"Titel": "Dana Schultz", "Category": "Entertainment", "Medium": "Visa", "Color": "#EEF2FF", "Txt": "#4F46E5", "BaseAmount": 550.00, "Date": "22 Sep - 10 AM"},
        {"Titel": "Jassie Moen", "Category": "Food & Beverage", "Medium": "Paypal", "Color": "#ECFDF5", "Txt": "#059669", "BaseAmount": 120.00, "Date": "21 Sep - 10 AM"},
        {"Titel": "Carroll Emmerich", "Category": "Housing", "Medium": "Payoner", "Color": "#FFFBEB", "Txt": "#D97706", "BaseAmount": 2200.00, "Date": "20 Sep - 10 AM"},
        {"Titel": "Elaine Dicki", "Category": "Digital Shopping", "Medium": "Visa", "Color": "#EEF2FF", "Txt": "#4F46E5", "BaseAmount": 45.00, "Date": "19 Sep - 10 AM"},
        {"Titel": "Ray Bergnaum", "Category": "Transportation", "Medium": "Payoner", "Color": "#FFFBEB", "Txt": "#D97706", "BaseAmount": 85.00, "Date": "18 Sep - 10 AM"},
        {"Titel": "Rose Dickinson", "Category": "Healthcare", "Medium": "Paypal", "Color": "#ECFDF5", "Txt": "#059669", "BaseAmount": 310.00, "Date": "17 Sep - 10 AM"}
    ]
    df_ledger = pd.DataFrame(ledger_records)
    return df_trends, df_ledger

chart_data, master_ledger = get_clean_mock_dataset()

# =====================================================================
# 3. SIDEBAR LAYOUT LAYER
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0rem; font-weight:700;'>💳 Money T</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-lbl">MENU</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item active">🏠 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">🔄 Transactions</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">📊 Analytics</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">⏱️ History</div>', unsafe_allow_html=True)

# =====================================================================
# 4. ENGINE HEADER SUTTE
# =====================================================================
st.markdown("<h1 style='color:#111114; font-weight:700; margin-bottom: 0rem;'>Wellcome, Ethan Cole 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#71717A; margin-top:0.25rem; margin-bottom:1.5rem;'>360° Financial Visibility Suite Overview Matrix</p>", unsafe_allow_html=True)

# =====================================================================
# 5. DYNAMIC CURRENCY & EXPENSE INTERACTION MATRIX
# =====================================================================
st.markdown("<div style='background-color: #FFFFFF; padding:1.25rem; border-radius:14px; border:1px solid #E4E4E7; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
st.markdown("<h4 style='margin:0 0 0.75rem 0; font-weight:700; color:#111114;'>⚙️ Live Financial Control Board</h4>", unsafe_allow_html=True)

config_col1, config_col2, config_col3 = st.columns(3)

with config_col1:
    currency_choice = st.selectbox(
        "Select Reporting Currency",
        options=["USD ($)", "EUR (€)", "GBP (£)", "JPY (¥)", "INR (₹)"]
    )
    
    # Currency symbol mapping
    symbols = {"USD ($)": "$", "EUR (€)": "€", "GBP (£)": "£", "JPY (¥)": "¥", "INR (₹)": "₹"}
    curr_sym = symbols[currency_choice]
    
    # Cross conversion calculation rates relative to baseline USD values
    rates = {"USD ($)": 1.0, "EUR (€)": 0.92, "GBP (£)": 0.79, "JPY (¥)": 156.0, "INR (₹)": 83.5}
    curr_rate = rates[currency_choice]

with config_col2:
    # Custom interactive base income input system
    user_income_input = st.number_input(
        f"Enter Base Monthly Income ({curr_sym}):", 
        min_value=0.0, 
        value=8500.0 * curr_rate,
        step=50.0
    )

with config_col3:
    target_amount = st.number_input(
        f"Max Expense Threshold Search ({curr_sym}):", 
        min_value=0.0, 
        value=500.0 * curr_rate, 
        step=10.0
    )

# Normalize currencies back to standard operational data bounds
target_amount_usd = target_amount / curr_rate
filtered_ledger = master_ledger[master_ledger['BaseAmount'] <= target_amount_usd]
total_filtered_spend_converted = (filtered_ledger['BaseAmount'].sum()) * curr_rate

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 6. DYNAMIC DESIGN METRIC CARDS (AUTOMATICALLY CONVERTED)
# =====================================================================
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.markdown(f"""
    <div class="kpi-wrapper border-purple">
        <div class="kpi-title">Calculated Total Income</div>
        <div class="kpi-value">{curr_sym}{user_income_input:,.2f}</div>
        <div class="kpi-badge badge-inc">▲ Active Base Settings</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    st.markdown(f"""
    <div class="kpi-wrapper border-orange">
        <div class="kpi-title">Calculated Spending Filter</div>
        <div class="kpi-value">{curr_sym}{total_filtered_spend_converted:,.2f}</div>
        <div class="kpi-badge badge-inc" style="background-color:#E0F2FE; color:#0369A1;">⚙️ Under Threshold Max</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    st.markdown(f"""
    <div class="kpi-wrapper border-teal">
        <div class="kpi-title">Spending Goal Limit</div>
        <div class="kpi-value">{curr_sym}{(9254.0 * curr_rate):,.2f}</div>
        <div class="kpi-badge badge-inc">▲ 15% Cap Buffer</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col4:
    st.markdown(f"""
    <div class="kpi-wrapper border-green">
        <div class="kpi-title">Active Logged Items</div>
        <div class="kpi-value">{len(filtered_ledger)} / {len(master_ledger)}</div>
        <div class="kpi-badge badge-inc">🎯 Records Matched</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Shared Chart Configuration Layers
def format_chart_layout(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#111114", family="Plus Jakarta Sans"),
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode="x unified"
    )
    fig.update_xaxes(showgrid=True, gridcolor="#E4E4E7", tickfont=dict(color="#71717A"))
    fig.update_yaxes(showgrid=True, gridcolor="#E4E4E7", tickfont=dict(color="#71717A"))

# =====================================================================
# 7. CENTRAL ANALYTICS GRID METRICS (ASSETS CURVE & GAUGES)
# =====================================================================
body_col_left, body_col_right = st.columns([2, 1])

with body_col_left:
    # Asset Progress Graph Block
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#111114;'>Your Assets Progression Matrix</h4>", unsafe_allow_html=True)
    
    asset_fig = go.Figure()
    asset_fig.add_trace(go.Scatter(
        x=chart_data['Date'], y=chart_data['Income'] * curr_rate, 
        name='Income Outflows', mode='lines', line=dict(color='#10B981', width=4.5),
        fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.03)'
    ))
    asset_fig.add_trace(go.Scatter(
        x=chart_data['Date'], y=chart_data['Expense'] * curr_rate, 
        name='Expense Outflows', mode='lines', line=dict(color='#F97316', width=4),
        fill='tozeroy', fillcolor='rgba(249, 115, 22, 0.03)'
    ))
    
    format_chart_layout(asset_fig)
    asset_fig.update_layout(legend=dict(orientation="h", y=1.1, x=0.6))
    st.plotly_chart(asset_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Custom HTML Table Component Clone (Where and how much was spent)
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;'><h4 style='margin:0; font-weight:700; color:#111114;'>Dynamic Expense Breakdown Engine</h4></div>", unsafe_allow_html=True)
    
    if not filtered_ledger.empty:
        table_html = "<table class='custom-table'><thead><tr style='background-color: #FAFAFA;'><th>Recipient</th><th>Category Pool</th><th>Method</th><th>Total Cost</th></tr></thead><tbody>"
        for _, row in filtered_ledger.iterrows():
            converted_amount = row['BaseAmount'] * curr_rate
            table_html += f"""
            <tr>
                <td style='font-weight:600;'>👤 {row['Titel']}</td>
                <td style='font-weight:500;'>📂 {row['Category']}</td>
                <td><span class='pill-medium' style='background-color:{row['Color']}; color:{row['Txt']};'>{row['Medium']}</span></td>
                <td style='font-weight:700; color: #EF4444;'>-{curr_sym}{converted_amount:,.2f}</td>
            </tr>
            """
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#EF4444; font-weight:600;'>No items found costing less than or equal to the filtered selection value.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with body_col_right:
    # Half Donut / Gauge Arc Transaction View Block
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7; min-height:430px;'>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:space-between;'><span style='font-weight:700; color:#111114;'>Operational Metrics</span></div>", unsafe_allow_html=True)
    
    if not filtered_ledger.empty:
        cat_group = filtered_ledger.groupby('Category')['BaseAmount'].sum().reset_index()
        gauge_fig = go.Figure(go.Pie(
            values=cat_group['BaseAmount'] * curr_rate,
            labels=cat_group['Category'],
            hole=0.7,
            rotation=90,
            direction='clockwise',
            textinfo='none'
        ))
        format_chart_layout(gauge_fig)
        gauge_fig.update_layout(
            showlegend=True, 
            legend=dict(orientation="h", y=-0.1, x=-0.1),
            annotations=[dict(text=f'{curr_sym}{total_filtered_spend_converted:,.0f}<br><span style="font-size:0.75rem; color:#10B981;">Active Volume</span>', x=0.5, y=0.5, font_size=16, font_weight="bold", showarrow=False)]
        )
        st.plotly_chart(gauge_fig, use_container_width=True)
    else:
        st.markdown("<p style='text-align:center; padding-top:4rem; color:#71717A;'>Waiting for filter values...</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
