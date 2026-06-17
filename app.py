import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime

# =====================================================================
# 1. APPLICATION ARCHITECTURE & TOTAL DESIGN CLONE STYLESHEET
# =====================================================================
st.set_page_config(
    page_title="Money T - Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_moneyt_template_theme():
    """Injects precise design elements to match the exact template layout."""
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
        
        /* --- SIDEBAR CLONE DESIGN BLOCK (#111114 Dark Charcoal) --- */
        [data-testid="stSidebar"] {
            background-color: #111114 !important;
            border-right: 1px solid #1E1E24;
            padding-top: 1rem !important;
        }
        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        
        /* Sidebar Navigation Items Mockup */
        .sidebar-nav-item {
            display: flex;
            align-items: center;
            padding: 0.75rem 1rem;
            border-radius: 10px;
            margin-bottom: 0.25rem;
            color: #A1A1AA;
            font-weight: 500;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }
        .sidebar-nav-item.active {
            background-color: #1F1F23;
            color: #FFFFFF;
        }
        .sidebar-nav-item:hover {
            color: #FFFFFF;
            background-color: #1A1A1E;
        }
        .sidebar-section-lbl {
            font-size: 0.75rem;
            font-weight: 700;
            color: #52525B;
            letter-spacing: 0.08em;
            margin: 1.5rem 0 0.5rem 1rem;
        }
        
        /* --- HORIZONTAL CONTROLS EXPANDER PANEL --- */
        .streamlit-expanderHeader {
            background-color: #FFFFFF !important;
            border-radius: 12px !important;
            border: 1px solid #E4E4E7 !important;
        }
        .streamlit-expanderContent {
            background-color: #FFFFFF !important;
            border: 1px solid #E4E4E7 !important;
            border-top: none !important;
            border-radius: 0 0 12px 12px !important;
            padding: 1rem !important;
        }
        
        /* Multi-Select Pills Override styling */
        span[data-baseweb="tag"] {
            background-color: #6366F1 !important; 
            color: #FFFFFF !important;
            border-radius: 6px !important;
        }

        /* --- UI METRIC CARD GRID INHERITANCE --- */
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
            color: #18181B;
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
        .badge-dec { background-color: #FEE2E2; color: #DC2626; }
        
        /* Match Explicit Borders from Screenshot Layout Template */
        .border-purple { border-top: 4px solid #6366F1; }
        .border-orange { border-top: 4px solid #F97316; }
        .border-teal { border-top: 4px solid #06B6D4; }
        .border-green { border-top: 4px solid #10B981; }

        /* --- CLEAN INTEGRATED TABLE DESIGN MATRIX --- */
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
            border-bottom: 1px solid #F4F4F5;
        }
        .custom-table td {
            padding: 0.9rem 1rem;
            color: #27272A;
            font-size: 0.85rem;
            border-bottom: 1px solid #F4F4F5;
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
# 2. RUNTIME REPLICA LIVE FINANCIAL LEDGER SIMULATOR
# =====================================================================
@st.cache_data
def get_clean_mock_dataset():
    """Generates precise seed metrics corresponding to dashboard graphical values."""
    np.random.seed(101)
    today = datetime.date.today()
    date_range = pd.date_range(end=today, periods=30, freq='D')
    
    income_curve = 400 + 150 * np.sin(np.linspace(0, 2*np.pi, 30)) + np.random.normal(0, 15, 30)
    expense_curve = 300 + 120 * np.cos(np.linspace(0, 2*np.pi, 30)) + np.random.normal(0, 10, 30)
    
    df_trends = pd.DataFrame({
        'Date': date_range,
        'Income': income_curve,
        'Expense': expense_curve
    })
    
    table_records = [
        {"Titel": "Dana Schultz", "Date": "22 Sep - 10 AM", "Medium": "Visa", "Color": "#EEF2FF", "Txt": "#4F46E5", "Amount": "$55,022"},
        {"Titel": "Jassie Moen", "Date": "21 Sep - 10 AM", "Medium": "Paypal", "Color": "#ECFDF5", "Txt": "#059669", "Amount": "$55,022"},
        {"Titel": "Carroll Emmerich", "Date": "20 Sep - 10 AM", "Medium": "Payoner", "Color": "#FFFBEB", "Txt": "#D97706", "Amount": "$55,022"},
        {"Titel": "Elaine Dicki", "Date": "19 Sep - 10 AM", "Medium": "Visa", "Color": "#EEF2FF", "Txt": "#4F46E5", "Amount": "$55,022"},
        {"Titel": "Ray Bergnaum", "Date": "18 Sep - 10 AM", "Medium": "Payoner", "Color": "#FFFBEB", "Txt": "#D97706", "Amount": "$55,022"},
        {"Titel": "Rose Dickinson", "Date": "17 Sep - 10 AM", "Medium": "Paypal", "Color": "#ECFDF5", "Txt": "#059669", "Amount": "$55,022"}
    ]
    
    return df_trends, table_records

chart_data, raw_table = get_clean_mock_dataset()

# =====================================================================
# 3. SIDEBAR HTML EMBED CLONE LAYER (REMOVED SWITCH TO PRO & GENERAL)
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0rem; font-weight:700;'>💳 Money T</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-lbl">MENU</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item active">🏠 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">🔄 Transactions</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">💳 Card</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">📊 Analytics</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">⏱️ History</div>', unsafe_allow_html=True)

# =====================================================================
# 4. TOP MANAGEMENT FILTER EXPANDER SECTION
# =====================================================================
st.markdown("<h1 style='color:#111114; font-weight:700; margin-bottom: 0rem;'>Wellcome, Ethan Cole 👋</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#71717A; margin-top:0.25rem; margin-bottom:1.5rem;'>360° Financial Visibility Suite Overview Matrix</p>", unsafe_allow_html=True)

with st.expander("🎛️ DRILL DOWN SELECTIONS / INTERACTIVE SLICERS", expanded=True):
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        date_sel = st.date_input("Timeframe Window Filter", [datetime.date.today() - datetime.timedelta(days=30), datetime.date.today()])
    with f_col2:
        cat_choices = ["Housing", "Food & Beverage", "Transportation", "Entertainment", "Digital Shopping"]
        cat_sel = st.multiselect("Category Select Slicer", options=cat_choices, default=cat_choices)
    with f_col3:
        acct_choices = ["Chase Checking", "Amex Platinum", "Fidelity Investment"]
        acct_sel = st.multiselect("Active Account Filter", options=acct_choices, default=acct_choices)

# =====================================================================
# 5. DYNAMIC DESIGN METRIC CARDS (MATCHES TOP ACCENT BORDERS)
# =====================================================================
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.markdown(f"""
    <div class="kpi-wrapper border-purple">
        <div class="kpi-title">Total Income</div>
        <div class="kpi-value">$8,500</div>
        <div class="kpi-badge badge-inc">▲ 35% Increased form last month</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    st.markdown(f"""
    <div class="kpi-wrapper border-orange">
        <div class="kpi-title">Total Spending</div>
        <div class="kpi-value">$3,500</div>
        <div class="kpi-badge badge-inc">▲ 75% Increased form last month</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    st.markdown(f"""
    <div class="kpi-wrapper border-teal">
        <div class="kpi-title">Spending Goal</div>
        <div class="kpi-value">$9,254</div>
        <div class="kpi-badge badge-inc">▲ 15% Increased form last month</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col4:
    st.markdown(f"""
    <div class="kpi-wrapper border-green">
        <div class="kpi-title">Total Transactions</div>
        <div class="kpi-value">$17,000</div>
        <div class="kpi-badge badge-inc">▲ 85% Increased form last month</div>
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
    if hasattr(fig, 'update_xaxes'):
        fig.update_xaxes(showgrid=True, gridcolor="#E4E4E7", tickfont=dict(color="#71717A"))
        fig.update_yaxes(showgrid=True, gridcolor="#E4E4E7", tickfont=dict(color="#71717A"))

# =====================================================================
# 6. CENTRAL ANALYTICS GRID METRICS (ASSETS CURVE & GAUGES)
# =====================================================================
body_col_left, body_col_right = st.columns([2, 1])

with body_col_left:
    # Asset Progress Graph Block
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#111114;'>Your Assets</h4>", unsafe_allow_html=True)
    
    asset_fig = go.Figure()
    asset_fig.add_trace(go.Scatter(
        x=chart_data['Date'], y=chart_data['Income'], 
        name='Income', mode='lines', line=dict(color='#10B981', width=4.5),
        fill='tozeroy', fillcolor='rgba(16, 185, 129, 0.03)'
    ))
    asset_fig.add_trace(go.Scatter(
        x=chart_data['Date'], y=chart_data['Expense'], 
        name='Expense', mode='lines', line=dict(color='#F97316', width=4),
        fill='tozeroy', fillcolor='rgba(249, 115, 22, 0.03)'
    ))
    
    format_chart_layout(asset_fig)
    asset_fig.update_layout(legend=dict(orientation="h", y=1.1, x=0.7))
    st.plotly_chart(asset_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Custom HTML Table Component Clone (Latest Transactions)
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:between; align-items:center; margin-bottom:1rem;'><h4 style='margin:0; font-weight:700; color:#111114;'>Latest Transaction</h4><span style='color:#6366F1; font-size:0.85rem; font-weight:600; cursor:pointer;'>See All</span></div>", unsafe_allow_html=True)
    
    table_html = "<table class='custom-table'><thead><tr><th>Titel</th><th>Date</th><th>Medium</th><th>Amount</th></tr></thead><tbody>"
    for row in raw_table:
        table_html += f"""
        <tr>
            <td style='font-weight:600;'>👤 {row['Titel']}</td>
            <td style='color:#71717A;'>{row['Date']}</td>
            <td><span class='pill-medium' style='background-color:{row['Color']}; color:{row['Txt']};'>{row['Medium']}</span></td>
            <td style='font-weight:700; color:#111114;'>🪙 {row['Amount']}</td>
        </tr>
        """
    table_html += "</tbody></table>"
    st.markdown(table_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with body_col_right:
    # Credit Card Render Mockup Block
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#111114;'>My Cards</h4>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #6366F1 0%, #4338CA 100%); padding: 1.5rem; border-radius: 14px; color: white; position: relative; min-height:160px; box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.3);">
        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8;">Debit Card</div>
        <div style="font-size: 1.4rem; font-weight: 700; margin-top: 1.5rem; letter-spacing: 0.05em;">•••• •••• •••• 0124</div>
        <div style="display: flex; justify-content: space-between; margin-top: 1.5rem; font-size: 0.8rem;">
            <div>
                <div style="opacity: 0.6; font-size: 0.65rem; text-transform: uppercase;">Holder</div>
                <div style="font-weight: 600;">Ethan Cole</div>
            </div>
            <div>
                <div style="opacity: 0.6; font-size: 0.65rem; text-transform: uppercase;">Expires</div>
                <div style="font-weight: 600;">12/28</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><button style='width:100%; padding:0.6rem; border-radius:10px; border:1px dashed #CBD5E1; background:transparent; color:#71717A; font-weight:600; cursor:pointer;'>+ Add new card</button>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Half Donut/Gauge Arc Transaction View Block
    st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
    st.markdown("<div style='display:flex; justify-content:between;'><span style='font-weight:700; color:#111114;'>Transaction View</span><span style='font-weight:700; color:#111114;'>$55,501</span></div>", unsafe_allow_html=True)
    
    gauge_fig = go.Figure(go.Pie(
        values=[45, 35, 20],
        labels=['Transaction View', 'Sales', 'Payment'],
        hole=0.7,
        rotation=90,
        direction='clockwise',
        marker=dict(colors=['#6366F1', '#10B981', '#D97706']),
        textinfo='none'
    ))
    format_chart_layout(gauge_fig)
    gauge_fig.update_layout(
        showlegend=True, 
        legend=dict(orientation="h", y=-0.1, x=-0.1),
        annotations=[dict(text='$55,501<br><span style="font-size:0.75rem; color:#10B981;">▲ 20% Growth</span>', x=0.5, y=0.5, font_size=20, font_weight="bold", showarrow=False)]
    )
    st.plotly_chart(gauge_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
