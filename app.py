import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =====================================================================
# 1. APPLICATION ARCHITECTURE & UI TEMPLATE THEME CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Money T - Personalized Planner Suite",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_moneyt_template_theme():
    """Injects high-fidelity stylesheets matching the template light mode style."""
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
# 2. SIDEBAR NAVIGATION LAYOUT
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0rem; font-weight:700;'>💳 Money T</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-lbl">MENU</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item active">🏠 Dashboard Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav-item">📊 Allocation Engine</div>', unsafe_allow_html=True)

# =====================================================================
# 3. INTERACTIVE HEADER & ENGINE CONTROL CONTROLS
# =====================================================================
st.markdown("<h1 style='color:#111114; font-weight:700; margin-bottom: 0rem;'>Personalized Allocation Strategy Matrix</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#71717A; margin-top:0.25rem; margin-bottom:1.5rem;'>Zero Dummy Data. Powered entirely by your financial profile inputs.</p>", unsafe_allow_html=True)

# --- USER ENTERED REAL-TIME INPUT ENGINE ---
st.markdown("<div style='background-color: #FFFFFF; padding:1.25rem; border-radius:14px; border:1px solid #E4E4E7; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
st.markdown("<h4 style='margin:0 0 0.75rem 0; font-weight:700; color:#111114;'>⚙️ Live Budget Planner Inputs</h4>", unsafe_allow_html=True)

config_col1, config_col2, config_col3 = st.columns([1.5, 1.5, 2])

with config_col1:
    currency_choice = st.selectbox(
        "Select Local Currency Token",
        options=["USD ($)", "EUR (€)", "GBP (£)", "JPY (¥)", "INR (₹)"]
    )
    symbols = {"USD ($)": "$", "EUR (€)": "€", "GBP (£)": "£", "JPY (¥)": "¥", "INR (₹)": "₹"}
    curr_sym = symbols[currency_choice]

with config_col2:
    user_income = st.number_input(
        f"Enter Your Real Monthly Net Income ({curr_sym}):", 
        min_value=0.0, 
        value=0.0,
        step=100.0
    )

with config_col3:
    allocation_strategy = st.selectbox(
        "Select Budget Strategy Rule",
        options=[
            "Balanced Strategy (50% Needs, 30% Wants, 20% Savings)",
            "Aggressive Investment Strategy (40% Needs, 20% Wants, 40% Savings)",
            "Conservative Minimum Strategy (60% Needs, 20% Wants, 20% Savings)"
        ]
    )

# Deconstruct Strategy Splitting Rules
if "Balanced Strategy" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.50, 0.30, 0.20
elif "Aggressive Investment" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.40, 0.20, 0.40
else:
    p_needs, p_wants, p_savings = 0.60, 0.20, 0.20

# Absolute Dynamic Allocations Calculation
amt_needs = user_income * p_needs
amt_wants = user_income * p_wants
amt_savings = user_income * p_savings

st.markdown("</div>", unsafe_allow_html=True)

# Check to block visual rendering if no data is present
if user_income <= 0:
    st.info("👋 Please enter an income value greater than 0 above to generate where and how much you should spend.")
else:
    # =====================================================================
    # 4. CALCULATED TARGET BUDGET KPI CARDS
    # =====================================================================
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

    with kpi_col1:
        st.markdown(f"""
        <div class="kpi-wrapper border-purple">
            <div class="kpi-title">Essential Needs Limit ({int(p_needs*100)}%)</div>
            <div class="kpi-value" style="color: #4F46E5;">{curr_sym}{amt_needs:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi_col2:
        st.markdown(f"""
        <div class="kpi-wrapper border-orange">
            <div class="kpi-title">Lifestyle & Wants Cap ({int(p_wants*100)}%)</div>
            <div class="kpi-value" style="color: #F97316;">{curr_sym}{amt_wants:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi_col3:
        st.markdown(f"""
        <div class="kpi-wrapper border-green">
            <div class="kpi-title">Financial Savings Reserve ({int(p_savings*100)}%)</div>
            <div class="kpi-value" style="color: #10B981;">{curr_sym}{amt_savings:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================================
    # 5. DATA TARGETS SPLIT GRAPHING & ENGINE ANALYSIS
    # =====================================================================
    body_col_left, body_col_right = st.columns([1.8, 1.2])

    with body_col_left:
        # Dynamic Recommendation Details Action Grid
        st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#111114;'>Exact Spending Category Directives</h4>", unsafe_allow_html=True)
        
        # Build out direct spending instructions structured table row lists
        budget_directives = [
            {
                "Category Pool": "Essential Needs",
                "Subcategories Included": "Rent/Mortgage, Utilities, Groceries, Insurance, Minimum Debt Payments",
                "Target Percentage": f"{int(p_needs*100)}%",
                "Max Budget Recommendation": f"{curr_sym}{amt_needs:,.2f}",
                "ColorPill": "#EEF2FF", "TxtColor": "#4F46E5"
            },
            {
                "Category Pool": "Personal Lifestyle & Wants",
                "Subcategories Included": "Dining Out, Entertainment, Hobbies, Travel, Shopping, Subscriptions",
                "Target Percentage": f"{int(p_wants*100)}%",
                "Max Budget Recommendation": f"{curr_sym}{amt_wants:,.2f}",
                "ColorPill": "#FFFBEB", "TxtColor": "#D97706"
            },
            {
                "Category Pool": "Future Savings & Investments",
                "Subcategories Included": "Emergency Fund, Retirement accounts (401k/IRA), Stocks, Cash Reserves",
                "Target Percentage": f"{int(p_savings*100)}%",
                "Max Budget Recommendation": f"{curr_sym}{amt_savings:,.2f}",
                "ColorPill": "#ECFDF5", "TxtColor": "#059669"
            }
        ]
        
        table_html = """
        <table class='custom-table'>
            <thead>
                <tr style='background-color: #FAFAFA;'>
                    <th>Where You Should Spend</th>
                    <th>Examples Included Below</th>
                    <th>Budget Target Split</th>
                    <th>Recommended Amount Max</th>
                </tr>
            </thead>
            <tbody>
        """
        for row in budget_directives:
            table_html += f"""
            <tr>
                <td style='font-weight:600;'>📁 {row['Category Pool']}</td>
                <td style='color:#71717A; font-size:0.8rem;'>{row['Subcategories Included']}</td>
                <td><span class='pill-medium' style='background-color:{row['ColorPill']}; color:{row['TxtColor']};'>{row['Target Percentage']}</span></td>
                <td style='font-weight:700;'>{row['Max Budget Recommendation']}</td>
            </tr>
            """
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with body_col_right:
        # High Fidelity Visual Donut Matrix
        st.markdown("<div style='background-color:#FFFFFF; padding:1.5rem; border-radius:16px; border:1px solid #E4E4E7; min-height:360px;'>", unsafe_allow_html=True)
        st.markdown("<span style='font-weight:700; color:#111114;'>Visual Budget Distribution Target</span>", unsafe_allow_html=True)
        
        labels = ['Essential Needs', 'Lifestyle & Wants', 'Future Savings']
        values = [amt_needs, amt_wants, amt_savings]
        colors = ['#6366F1', '#F97316', '#10B981']
        
        gauge_fig = go.Figure(go.Pie(
            values=values,
            labels=labels,
            hole=0.7,
            marker=dict(colors=colors),
            textinfo='none',
            hoverinfo='label+value'
        ))
        
        gauge_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#111114", family="Plus Jakarta Sans"),
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=True,
            legend=dict(orientation="h", y=-0.1, x=-0.05)
        )
        
        st.plotly_chart(gauge_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
