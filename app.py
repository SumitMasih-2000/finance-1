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
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
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
st.markdown("<p style='color:#71717A; margin-top:0.25rem; margin-bottom:1.5
