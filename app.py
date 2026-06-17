import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =====================================================================
# 1. APPLICATION ARCHITECTURE & UI TEMPLATE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Personal Finance - Allocation Suite",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_personal_finance_theme():
    """Injects high-fidelity stylesheets matching the new white-purple gradient layout."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #F3F4F6 0%, #EEEFFF 100%) !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        h1, h2, h3, h4, h5, h6, p, span, label, div, td, th {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* --- SIDEBAR WORKSPACE CONTROLS --- */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0;
            padding-top: 1.5rem !important;
        }
        
        .sidebar-nav-item {
            display: flex;
            align-items: center;
            padding: 0.85rem 1.2rem;
            border-radius: 14px;
            margin-bottom: 0.4rem;
            color: #718096;
            font-weight: 600;
            font-size: 0.95rem;
        }
        .sidebar-nav-item.active {
            background: linear-gradient(90deg, #8B5CF6 0%, #6366F1 100%);
            color: #FFFFFF !important;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
        }
        
        /* --- HORIZONTAL MONTH SELECTOR HEADER BANNER --- */
        .month-banner-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #FFFFFF;
            padding: 0.5rem 1rem;
            border-radius: 30px;
            border: 1px solid #E2E8F0;
            margin-bottom: 1.5rem;
            overflow-x: auto;
        }
        .month-pill {
            padding: 0.4rem 0.85rem;
            font-size: 0.75rem;
            font-weight: 700;
            color: #A0AEC0;
            text-transform: uppercase;
            border-radius: 20px;
            letter-spacing: 0.05em;
        }
        .month-pill.active {
            background: linear-gradient(90deg, #8B5CF6 0%, #3B82F6 100%);
            color: #FFFFFF;
            box-shadow: 0 2px 6px rgba(139, 92, 246, 0.3);
        }

        /* --- DYNAMIC WHITE CARD SURFACES --- */
        .finance-card {
            background-color: #FFFFFF;
            padding: 1.5rem;
            border-radius: 20px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.01);
            margin-bottom: 1.5rem;
        }
        
        /* --- PLANNED DIRECTIVE TABLE SYSTEMS --- */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            background-color: #FFFFFF;
        }
        .custom-table th {
            text-align: left;
            padding: 0.85rem 1rem;
            color: #A0AEC0;
            font-weight: 600;
            font-size: 0.8rem;
            border-bottom: 1px solid #EDF2F7;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .custom-table td {
            padding: 1.1rem 1rem;
            color: #2D3748;
            font-size: 0.88rem;
            border-bottom: 1px solid #EDF2F7;
        }
        .pill-medium {
            padding: 0.3rem 0.75rem;
            border-radius: 8px;
            font-size: 0.75rem;
            font-weight: 700;
        }
        
        #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

inject_personal_finance_theme()

# =====================================================================
# 2. RUNTIME INTERNAL STORAGE SYSTEM
# =====================================================================
if 'user_expenses' not in st.session_state:
    st.session_state['user_expenses'] = []

# =====================================================================
# 3. SIDEBAR NAVIGATION & TRANSACTION CONTROL PANEL
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='font-weight:800; color:#2D3748; margin-left:0.5rem;'>📊 PERSONAL</h2><p style='color:#718096; font-size:0.8rem; margin-top:-0.75rem; margin-left:0.5rem; font-weight:600; letter-spacing:0.05em;'>FINANCE ENGINE</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-nav-item active">🏠 Dashboard</div>', unsafe_allow_html=True)
    st.markdown("<br><hr style='border-color:#E2E8F0;'><br>", unsafe_allow_html=True)
    
    # Clean Transaction Logger inside the panel sidebar layout
    st.markdown("<h4 style='font-weight:700; color:#2D3748; margin-bottom:1rem;'>✍️ Log Transaction</h4>", unsafe_allow_html=True)
    entry_title = st.text_input("Merchant Name", placeholder="e.g., Landlord Corp, Target")
    entry_category = st.selectbox("Category Target Pool", ["Essential Needs", "Personal Lifestyle & Wants", "Future Savings & Investments"])
    entry_amount = st.number_input("Amount Charged", min_value=0.0, value=0.0, step=25.0)
    add_btn = st.button("Log Expense entry", use_container_width=True)

    if add_btn and entry_title and entry_amount > 0:
        st.session_state['user_expenses'].append({
            "Merchant": entry_title,
            "Category": entry_category,
            "Amount": entry_amount
        })
        st.toast(f"Logged entry for {entry_title}!", icon="✅")

# =====================================================================
# 4. TEMPLATE MONTH BANNER HORIZONTAL SELECTOR COMPONENT
# =====================================================================
st.markdown("""
<div class="month-banner-container">
    <div class="month-pill">January</div>
    <div class="month-pill">February</div>
    <div class="month-pill">March</div>
    <div class="month-pill active">April</div>
    <div class="month-pill">May</div>
    <div class="month-pill">June</div>
    <div class="month-pill">July</div>
    <div class="month-pill">August</div>
    <div class="month-pill">September</div>
    <div class="month-pill">October</div>
    <div class="month-pill">November</div>
    <div class="month-pill">December</div>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# 5. INPUT PARAMETER ENGINE 
# =====================================================================
st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#2D3748;'>⚙️ Budget Parameter Configuration</h4>", unsafe_allow_html=True)

config_col1, config_col2, config_col3 = st.columns([1.5, 1.5, 2])

with config_col1:
    currency_choice = st.selectbox(
        "Reporting Currency Token",
        options=["USD ($)", "EUR (€)", "GBP (£)", "JPY (¥)", "INR (₹)"]
    )
    symbols = {"USD ($)": "$", "EUR (€)": "€", "GBP (£)": "£", "JPY (¥)": "¥", "INR (₹)": "₹"}
    curr_sym = symbols[currency_choice]

with config_col2:
    user_income = st.number_input(
        f"Enter Real Monthly Net Income ({curr_sym}):", 
        min_value=0.0, 
        value=80000.0,
        step=1000.0
    )

with config_col3:
    allocation_strategy = st.selectbox(
        "Select Matrix Allocation Target Strategy",
        options=[
            "Balanced Strategy (50% Needs, 30% Wants, 20% Savings)",
            "Aggressive Wealth Accumulation (40% Needs, 20% Wants, 40% Savings)",
            "Conservative Baseline Rule (60% Needs, 20% Wants, 20% Savings)"
        ]
    )

if "Balanced Strategy" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.50, 0.30, 0.20
elif "Aggressive Wealth Accumulation" in allocation_strategy:
    p_needs, p_wants, p_savings = 0.40, 0.20, 0.40
else:
    p_needs, p_wants, p_savings = 0.60, 0.20, 0.20

amt_needs = user_income * p_needs
amt_wants = user_income * p_wants
amt_savings = user_income * p_savings

st.markdown("</div>", unsafe_allow_html=True)

# Process computations based on live arrays
df_entries = pd.DataFrame(st.session_state['user_expenses']) if st.session_state['user_expenses'] else pd.DataFrame(columns=["Merchant", "Category", "Amount"])

spent_needs = df_entries[df_entries['Category'] == "Essential Needs"]['Amount'].sum()
spent_wants = df_entries[df_entries['Category'] == "Personal Lifestyle & Wants"]['Amount'].sum()
spent_savings = df_entries[df_entries['Category'] == "Future Savings & Investments"]['Amount'].sum()

total_all_expenses = spent_needs + spent_wants + spent_savings
used_percentage = int((total_all_expenses / user_income * 100)) if user_income > 0 else 0

if user_income <= 0:
    st.info("👋 Setup your monthly income parameter configuration above to trigger the dynamic tracking curves.")
else:
    # =====================================================================
    # 6. CENTRAL MATRIX AND BUDGET RATIO PROGRESS GRAPH
    # =====================================================================
    row1_left, row1_right = st.columns([2, 1])
    
    with row1_left:
        st.markdown("<div class='finance-card' style='min-height:380px;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin:0 0 1.25rem 0; font-weight:700; color:#2D3748;'>Exact Strategic Allocation Directives Matrix</h4>", unsafe_allow_html=True)
        
        table_html = f"""
        <table class='custom-table'>
            <thead>
                <tr>
                    <th>Where You Should Spend</th>
                    <th>Examples & Subcategories Covered</th>
                    <th>Target Split</th>
                    <th>Remaining Spending Budget Available</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style='font-weight:700; color:#4F46E5;'>📁 Essential Needs</td>
                    <td style='color:#718096; font-size:0.8rem;'>Rent/Mortgage, Utilities, Groceries, Insurance, Minimum Debt Payments</td>
                    <td><span class='pill-medium' style='background-color:#EEF2FF; color:#4F46E5;'>{int(p_needs*100)}%</span></td>
                    <td style='font-weight:700; font-size:1rem; color:#2D3748;'>{curr_sym}{(amt_needs - spent_needs):,.2f}</td>
                </tr>
                <tr>
                    <td style='font-weight:700; color:#D97706;'>📁 Personal Lifestyle & Wants</td>
                    <td style='color:#718096; font-size:0.8rem;'>Dining Out, Entertainment, Hobbies, Travel, Shopping, Subscriptions</td>
                    <td><span class='pill-medium' style='background-color:#FFFBEB; color:#D97706;'>{int(p_wants*100)}%</span></td>
                    <td style='font-weight:700; font-size:1rem; color:#2D3748;'>{curr_sym}{(amt_wants - spent_wants):,.2f}</td>
                </tr>
                <tr>
                    <td style='font-weight:700; color:#059669;'>📁 Future Savings & Investments</td>
                    <td style='color:#718096; font-size:0.8rem;'>Emergency Fund, Retirement accounts (401k/IRA), Stocks, Cash Reserves</td>
                    <td><span class='pill-medium' style='background-color:#ECFDF5; color:#059669;'>{int(p_savings*100)}%</span></td>
                    <td style='font-weight:700; font-size:1rem; color:#2D3748;'>{curr_sym}{(amt_savings - spent_savings):,.2f}</td>
                </tr>
            </tbody>
        </table>
        """
        st.markdown(table_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with row1_right:
        st.markdown("<div class='finance-card' style='text-align:center; min-height:380px;'>", unsafe_allow_html=True)
        st.markdown("<p style='margin:0; font-weight:700; color:#718096; text-transform:uppercase; font-size:0.8rem; letter-spacing:0.05em; text-align:left;'>Ratio Income Used</p>", unsafe_allow_html=True)
        
        ratio_fig = go.Figure(go.Pie(
            values=[total_all_expenses, max(0.0, user_income - total_all_expenses)],
            labels=['Income Spent', 'Income Available'],
            hole=0.78,
            marker=dict(colors=['#8B5CF6', '#E2E8F0']),
            textinfo='none',
            hoverinfo='label+value'
        ))
        ratio_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            annotations=[dict(text=f"<span style='font-size:2.2rem; font-weight:800; color:#2D3748;'>{used_percentage}%</span><br><span style='font-size:0.75rem; color:#A0AEC0; font-weight:600;'>USED</span>", x=0.5, y=0.5, showarrow=False)]
        )
        st.plotly_chart(ratio_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================================
    # 7. VISUAL WORKSPACE OVERVIEW BAR GRAPH (FIXED PROPERTY SYSTEM)
    # =====================================================================
    st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#2D3748;'>📊 Live Target vs Spent Allocation Breakdown</h4>", unsafe_allow_html=True)
    
    categories = ['Essential Needs', 'Personal Lifestyle & Wants', 'Future Savings & Investments']
    target_caps = [amt_needs, amt_wants, amt_savings]
    current_outlays = [spent_needs, spent_wants, spent_savings]
    
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(
        name='Target Budget Limit',
        x=categories,
        y=target_caps,
        marker_color='#E2E8F0',
        marker_corner_radius=10  # <-- Corrected syntax property replacement
    ))
    bar_fig.add_trace(go.Bar(
        name='Current Real Outlays',
        x=categories,
        y=current_outlays,
        marker_color='#8B5CF6',
        marker_corner_radius=10  # <-- Corrected syntax property replacement
    ))
    
    bar_fig.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#2D3748", family="Plus Jakarta Sans"),
        margin=dict(l=40, r=20, t=20, b=20),
        legend=dict(orientation="h", y=1.1, x=0),
        hovermode="x unified"
    )
    bar_fig.update_xaxes(showgrid=False, tickfont=dict(color="#718096", size=11, weight="bold"))
    bar_fig.update_yaxes(showgrid=True, gridcolor="#EDF2F7", tickfont=dict(color="#718096"))
    
    st.plotly_chart(bar_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================================
    # 8. LOWER LEDGER LOG MATRIX & RADIAL SUMMARY DISTRIBUTION
    # =====================================================================
    row2_left, row2_right = st.columns([1.5, 1.5])
    
    with row2_left:
        st.markdown("<div class='finance-card' style='min-height:380px;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin:0 0 1rem 0; font-weight:700; color:#2D3748;'>Live Tracking Ledger Log</h4>", unsafe_allow_html=True)
        if not df_entries.empty:
            st.dataframe(df_entries, use_container_width=True, hide_index=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Reset Matrix Ledger Data"):
                st.session_state['user_expenses'] = []
                st.rerun()
        else:
            st.markdown("<p style='color:#A0AEC0; font-size:0.85rem; padding-top:2rem; text-align:center;'>No outlays logged inside this active monthly workspace session.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with row2_right:
        st.markdown("<div class='finance-card' style='min-height:380px;'>", unsafe_allow_html=True)
        st.markdown("<p style='margin:0 0 0.5rem 0; font-weight:700; color:#718096; text-transform:uppercase; font-size:0.8rem; letter-spacing:0.05em;'>Active Allocation Outflows</p>", unsafe_allow_html=True)
        
        donut_fig = go.Figure(go.Pie(
            values=[spent_needs, spent_wants, spent_savings, max(0.0, user_income - total_all_expenses)],
            labels=['Needs Outflows', 'Wants Outflows', 'Savings Transferred', 'Remaining Safety Margin'],
            hole=0.72,
            marker=dict(colors=['#6366F1', '#F59E0B', '#10B981', '#F1F5F9']),
            textinfo='none',
            hoverinfo='label+value'
        ))
        donut_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=True,
            legend=dict(orientation="h", y=-0.1, x=-0.05, font=dict(color="#4A5568", size=10))
        )
        st.plotly_chart(donut_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
