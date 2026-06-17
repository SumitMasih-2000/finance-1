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
        
        div[data-testid="stSidebarUserContent"] {
            padding-top: 2rem;
        }
        
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.2s;
        }
        
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
            ledger_records.append(
