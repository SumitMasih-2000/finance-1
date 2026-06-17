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

# Initialize state configuration for custom settings
if 'theme_choice' not in st.session_state:
    st.session_state['theme_choice'] = "Light Mode"

def inject_theme_engine(theme):
    """Injects high-fidelity stylesheets to toggle canvas variants layout."""
    if theme == "Dark Mode":
        # Corporate Dark Blueprint Theme System Colors
        bg_canvas = "#0F172A"       # Deep Slate Blue-Gray
        card_surface = "#1E293B"    # Muted Card Surface
        text_primary = "#F8FAFC"    # Crisp White Text
        text_secondary = "#94A3B8"  # Slate Muted Gray
        border_color = "#334155"    # Subtle Dark Border Line
        grid_color = "#334155"
    else:
        # Template Standard Light Mode Palette Clones
        bg_canvas = "#F3F4F6"       # Light Grayish-White
        card_surface = "#FFFFFF"    # Pure White Cards
        text_primary = "#111114"    # Deep Charcoal
        text_secondary = "#71717A"  # Cool Gray
        border_color = "#E4E4E7"    # Thin Border Line
        grid_color = "#E4E4E7"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
        /* Master Main Canvas Settings */
        .stApp {{
            background-color: {bg_canvas} !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            transition: background-color 0.3s ease;
        }}
        
        h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }}
        
        /* --- SIDEBAR CLONE DESIGN BLOCK (#111114 Dark Charcoal) --- */
        [data-testid="stSidebar"] {{
            background-color: #111114 !important;
            border-right: 1px solid #1E1E24;
            padding-top: 1rem !important;
        }}
        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {{
            color: #FFFFFF !important;
        }}
        
        .sidebar-nav-item {{
            display: flex;
            align-items: center;
            padding: 0.75rem 1rem;
            border-radius: 10px;
            margin-bottom: 0.25rem;
            color: #A1A1AA;
            font-weight: 500;
            font-size: 0.95rem;
        }}
        .sidebar-nav-item.active {{
            background-color: #1F1F23;
            color: #FFFFFF;
        }}
        .sidebar-section-lbl {{
            font-size: 0.75rem;
            font-weight: 700;
            color: #52525B;
            letter-spacing: 0.08em;
            margin: 1.5rem 0 0.5rem 1rem;
        }}
        
        /* --- DYNAMIC METRIC SURFACES --- */
        .kpi-wrapper {{
            background-color: {card_surface};
            padding: 1.25rem;
            border-radius: 16px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
            border: 1px solid {border_color};
            min-height: 145px;
            transition: all 0.3s ease;
        }}
        .kpi-title {{
            font-size: 0.85rem;
            color: {text_secondary};
            font-weight: 500;
        }}
        .kpi-value {{
            font-size: 2.1rem;
            font-weight: 700;
            color: {text_primary};
            margin-top: 0.4rem;
            letter-spacing: -0.04em;
        }}
        .kpi-badge {{
            display: inline-flex;
            align-items: center;
            padding: 0.2rem 0.4rem;
            border-radius: 6px;
            font-size: 0.72rem;
            font-weight: 600;
            margin-top: 0.6rem;
        }}
        .badge-inc {{ background-color: #DCFCE7; color: #16A34A; }}
        
        .border-purple {{ border-top: 4px solid #6366F1; }}
        .border-orange {{ border-top: 4px solid #F97316; }}
        .border-teal {{ border-top: 4px solid #06B6D4; }}
        .border-green {{ border-top: 4px solid #10B981; }}

        /* --- CLEAN STREAMLINED TABLE SYSTEMS --- */
        .custom-table {{
            width: 100%;
            border-collapse: collapse;
            background-color: {card_surface};
            border-radius: 12px;
            overflow: hidden;
        }}
        .custom-table th {{
            text-align: left;
            padding: 0.75rem 1rem;
            background-color: {card_surface};
            color: {text_secondary};
            font-weight: 600;
            font-size: 0.8rem;
            border-bottom: 1px solid {border_color};
        }}
        .custom-table td {{
            padding: 0.9rem 1rem;
            color: {text_primary};
            font-size: 0.85rem;
            border-bottom: 1px solid {border_color};
        }}
        .pill-medium {{
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        
        #MainMenu, footer {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)

# =====================================================================
# 2. RUNTIME COMPLETE FINANCIAL DATA ENGINE
# =====================================================================
@st.cache_data
def get_clean_mock_dataset():
    np.random.seed(42)
    today = datetime.date.today()
    date_range = pd.date_range(end=today, periods=30, freq='D')
    
    # Real-time asset progression trends modeling
    income_curve = 550 + 120 * np.sin(np.linspace(0, 2*np.pi, 30)) + np.random.normal(0, 10, 30)
    expense_curve = 380 + 90 * np.cos(np.linspace(0, 2*np.pi, 30)) + np.random.normal(0, 8, 30)
    
    df_trends = pd.DataFrame({'Date': date_range, 'Income': income_curve, 'Expense': expense_curve})
    
    # Granular expense matrix
    ledger_records = [
        {"Titel": "Dana Schultz", "Category": "Entertainment", "Medium": "Visa", "Color": "#EEF2FF", "Txt": "#4F46E5", "Amount": 550.00, "Date": "22 Sep - 10 AM"},
        {"Titel": "Jassie Moen", "Category": "Food & Beverage", "Medium": "Paypal", "Color": "#ECFDF5", "Txt": "#059669", "Amount": 120.00, "Date": "21 Sep - 10 AM"},
        {"Titel": "Carroll Emmerich", "Category": "Housing", "Medium": "Payoner", "Color": "#FFFBEB", "Txt": "#D97706", "Amount": 2200.00, "Date": "20 Sep - 10 AM"},
        {"Titel": "Elaine Dicki", "Category": "Digital Shopping", "Medium": "Visa", "Color": "#EEF2FF", "Txt": "#4F46E5", "Amount": 45.00, "Date": "19 Sep - 10 AM"},
        {"Titel": "Ray Bergnaum", "Category": "Transportation", "Medium": "Payoner", "Color": "#FFFBEB", "Txt": "#D97706", "Amount": 85.00, "Date": "18 Sep - 10 AM"},
        {"Titel": "Rose Dickinson", "Category": "Healthcare", "Medium": "Paypal", "Color": "#ECFDF5", "Txt": "#059669", "Amount": 310.00, "Date": "17 Sep - 10 AM"}
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
# 4. ENGINE CONTROLS, THEME ACCENT PICKER, & EXPENSE CALCULATOR
# =====================================================================
header_col, control_col = st.columns([2, 1])

with header_col:
    st.markdown("<h1 style='font-weight:700; margin-bottom: 0rem;'>Wellcome, Ethan Cole 👋</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:0.25rem; margin-bottom:1.5rem;'>360° Financial Visibility Suite Overview Matrix</p>", unsafe_allow_html=True)

with control_col:
    # Color Layout Dynamic Control Slicer
    theme_choice = st.radio(
        "Canvas Interface Theme",
        options=["Light Mode", "Dark Mode"],
        horizontal=True,
        index=0 if st.session_state['theme_choice'] == "Light Mode" else 1,
        key="theme_radio_input"
    )
    st.session_state['theme_choice'] = theme_choice

# Initialize Master CSS UI Theme Layer Injector
inject_theme_engine(st.session_state['theme_choice'])
is_dark = st.session_state['theme_choice'] == "Dark Mode"
text_color_code = "#F8FAFC" if is_dark else "#111114"
grid_color_code = "#334155" if is_dark else "#E4E4E7"

# --- NEW: INTERACTIVE AMOUNT SPENDING SEARCH ENGINE ---
st.markdown(f"<div style='background-color: {'#1E293B' if is_dark else '#FFFFFF'}; padding:1.25rem; border-radius:14px; border:1px solid {grid_color_code}; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
st.markdown(f"<h4 style='margin:0 0 0.5rem 0; font-weight:700; color:{text_color_code};'>🔍 Dynamic Expense Tracker Slicer</h4>", unsafe_allow_html=True)
target_amount = st.number_input("Enter a threshold amount to review exactly where and how much you spent ($):", min_value=0.0, value=500.0, step=10.0)

# Apply runtime logical threshold calculations
filtered_ledger = master_ledger[master_ledger['Amount'] <= target_amount]
total_filtered_spend = filtered_ledger['Amount'].sum()
st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 5. DYNAMIC DESIGN METRIC CARDS
# =====================================================================
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.markdown(f"""
    <div class="kpi-wrapper border-purple">
        <div class="kpi-title">Total Income</div>
        <div class="kpi-value">$8,500</div>
        <div class="kpi-badge badge-inc">▲ 35% Base Yield</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    st.markdown(f"""
    <div class="kpi-wrapper border-orange">
        <div class="kpi-title">Calculated Spending Target Filter</div>
        <div class="kpi-value">${total_filtered_spend:,.2f}</div>
        <div class="kpi-badge badge-inc" style="background-color:#E0F2FE; color:#0369A1;">⚙️ Under Max Threshold</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    st.markdown(f"""
    <div class="kpi-wrapper border-teal">
        <div class="kpi-title">Spending Goal Limit</div>
        <div class="kpi-value">$9,254</div>
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
        font=dict(color=text_color_code, family="Plus Jakarta Sans"),
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode="x unified"
    )
    if hasattr(fig, 'update_xaxes'):
        fig.update_xaxes(showgrid=True, gridcolor=grid_color_code, tickfont=dict(color=text_color_code))
        fig.update_yaxes(showgrid=True, gridcolor=grid_color_code, tickfont=dict(color=text_color_code))

# =====================================================================
# 6. CENTRAL ANALYTICS GRID METRICS
# =====================================================================
body_col_left, body_col_right = st.columns([2, 1])

with body_col_left:
    # Asset Progress Graph Block
    st.markdown(f"<div style='background-color:{'#1E293B' if is_dark else '#FFFFFF'}; padding:1.5rem; border-radius:16px; border:1px solid {grid_color_code};'>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='margin:0 0 1rem 0; font-weight:700; color:{text_color_code};'>Your Assets Progression</h4>", unsafe_allow_html=True)
    
    asset_fig = go.Figure()
    asset_fig.add_trace(go.Scatter(
        x=chart_data['Date'], y=chart_data['Income'], 
        name='Income Outflows', mode='lines', line=dict(color='#10B981', width=4.5),
        fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.03)'
    ))
    asset_fig.add_trace(go.Scatter(
        x=chart_data['Date'], y=chart_data['Expense'], 
        name='Expense Outflows', mode='lines', line=dict(color='#F97316', width=4),
        fill='tozeroy', fillcolor='rgba(249, 115, 22, 0.03)'
    ))
    
    format_chart_layout(asset_fig)
    asset_fig.update_layout(legend=dict(orientation="h", y=1.1, x=0.6, font=dict(color=text_color_code)))
    st.plotly_chart(asset_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Custom HTML Table Component Clone (Where and how much was spent)
    st.markdown(f"<div style='background-color:{'#1E293B' if is_dark else '#FFFFFF'}; padding:1.5rem; border-radius:16px; border:1px solid {grid_color_code};'>", unsafe_allow_html=True)
    st.markdown(f"<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;'><h4 style='margin:0; font-weight:700; color:{text_color_code};'>Dynamic Expense Breakdown Engine</h4></div>", unsafe_allow_html=True)
    
    if not filtered_ledger.empty:
        table_html = f"<table class='custom-table'><thead><tr style='background-color: {'#334155' if is_dark else '#FAFAFA'};'><th>Recipient</th><th>Category Pool</th><th>Method</th><th>Total Cost</th></tr></thead><tbody>"
        for _, row in filtered_ledger.iterrows():
            table_html += f"""
            <tr>
                <td style='font-weight:600;'>👤 {row['Titel']}</td>
                <td style='font-weight:500;'>📂 {row['Category']}</td>
                <td><span class='pill-medium' style='background-color:{row['Color']}; color:{row['Txt']};'>{row['Medium']}</span></td>
                <td style='font-weight:700; color: #EF4444;'>-${row['Amount']:,.2f}</td>
            </tr>
            """
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#EF4444; font-weight:600;'>No items found costing less than or equal to the filtered selection value.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with body_col_right:
    # Half Donut / Gauge Arc Transaction View Block
    st.markdown(f"<div style='background-color:{'#1E293B' if is_dark else '#FFFFFF'}; padding:1.5rem; border-radius:16px; border:1px solid {grid_color_code}; min-height:430px;'>", unsafe_allow_html=True)
    st.markdown(f"<div style='display:flex; justify-content:space-between;'><span style='font-weight:700; color:{text_color_code};'>Operational Metrics</span></div>", unsafe_allow_html=True)
    
    if not filtered_ledger.empty:
        cat_group = filtered_ledger.groupby('Category')['Amount'].sum().reset_index()
        gauge_fig = go.Figure(go.Pie(
            values=cat_group['Amount'],
            labels=cat_group['Category'],
            hole=0.7,
            rotation=90,
            direction='clockwise',
            textinfo='none'
        ))
        format_chart_layout(gauge_fig)
        gauge_fig.update_layout(
            showlegend=True, 
            legend=dict(orientation="h", y=-0.1, x=-0.1, font=dict(color=text_color_code)),
            annotations=[dict(text=f'${total_filtered_spend:,.0f}<br><span style="font-size:0.75rem; color:#10B981;">Active Volume</span>', x=0.5, y=0.5, font_size=16, font_weight="bold", showarrow=False, font_color=text_color_code)]
        )
        st.plotly_chart(gauge_fig, use_container_width=True)
    else:
        st.markdown("<p style='text-align:center; padding-top:4rem; color:#71717A;'>Waiting for filter values...</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
