import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Styling
st.set_page_config(
    page_title="Money T - Advanced Financial Dashboard",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished UI
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #7e57c2; margin-bottom: 0.5rem; }
    .section-header { font-size: 1.4rem; font-weight: 600; color: #424242; margin-top: 1.5rem; margin-bottom: 1rem; }
    .card { background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# Initialize Session States for persistent tracking
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# 2. Sidebar Navigation & Global Parameters
with st.sidebar:
    st.markdown("<h1 style='color: #7e57c2;'>💜 Money T</h1>", unsafe_allow_html=True)
    st.caption("Strategic Wealth & Outlay Allocation Matrix")
    st.write("---")
    
    # Navigation Tool Selector
    menu_selection = st.radio(
        "Navigate Dashboard Tools",
        ["📊 Main Matrix Dashboard", "🧮 Financial Goal Calculator", "📈 Expense Analytics"]
    )
    
    st.write("---")
    st.markdown("### ⚙️ Global Parameters")
    currency = st.selectbox("Currency Token", ["USD ($)", "EUR (€)", "GBP (£)", "INR (₹)"])
    currency_symbol = currency.split("(")[1].replace(")", "")
    
    monthly_income = st.number_input(
        f"Monthly Net Income ({currency_symbol})", 
        min_value=0.0, 
        value=82000.0, 
        step=500.0
    )
    
    strategy = st.selectbox(
        "Matrix Strategy Split",
        ["Balanced Rule (50% Needs, 30% Wants, 20% Savings)", "Aggressive Saving (40% Needs, 20% Wants, 40% Savings)"]
    )

# Extract split ratios based on strategy selection
if "Balanced" in strategy:
    r_needs, r_wants, r_savings = 0.50, 0.30, 0.20
else:
    r_needs, r_wants, r_savings = 0.40, 0.20, 0.40

# Compute Target Bounds
target_needs = monthly_income * r_needs
target_wants = monthly_income * r_wants
target_savings = monthly_income * r_savings

# --- TOOL 1: MAIN MATRIX DASHBOARD ---
if menu_selection == "📊 Main Matrix Dashboard":
    st.markdown("<h1 class='main-title'>📍 June 2026 Matrix Allocation</h1>", unsafe_allow_html=True)
    
    # Quick KPI Summary Cards
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate current usage aggregates
    current_df = pd.DataFrame(st.session_state.expenses)
    spend_needs = current_df[current_df['Category'] == 'Essential Needs']['Amount'].sum() if not current_df.empty else 0.0
    spend_wants = current_df[current_df['Category'] == 'Personal Lifestyle & Wants']['Amount'].sum() if not current_df.empty else 0.0
    spend_savings = current_df[current_df['Category'] == 'Future Savings & Investments']['Amount'].sum() if not current_df.empty else 0.0
    total_spent = spend_needs + spend_wants + spend_savings
    margin_left = monthly_income - total_spent
    
    col1.metric("Total Income", f"{currency_symbol}{monthly_income:,.2f}")
    col2.metric("Total Logged Outlays", f"{currency_symbol}{total_spent:,.2f}", delta=f"-{total_spent:,.2f}", delta_color="inverse")
    col3.metric("Remaining Margin", f"{currency_symbol}{margin_left:,.2f}", delta=f"{((margin_left/monthly_income)*100):.1f}% Remainder")
    col4.metric("Active Plan Profile", strategy.split(" ")[0])
    
    st.write("---")
    
    # Split View: Log Outlay (Left) vs Directive Matrix (Right)
    left_flow, right_matrix = st.columns([1, 2], gap="large")
    
    with left_flow:
        st.markdown("<div class='section-header'>✍️ Log Outlay (June)</div>", unsafe_allow_html=True)
        with st.form("outlay_form", clear_on_submit=True):
            merchant = st.text_input("Merchant/Recipient", placeholder="e.g., Target, Electric Corp")
            category = st.selectbox("Strategic Allocation Category", ["Essential Needs", "Personal Lifestyle & Wants", "Future Savings & Investments"])
            amount = st.number_input(f"Amount Paid ({currency_symbol})", min_value=0.0, step=10.0)
            
            submit_btn = st.form_submit_button("Commit Outlay Trace", use_container_width=True)
            if submit_btn and merchant and amount > 0:
                st.session_state.expenses.append({
                    "Merchant": merchant,
                    "Category": category,
                    "Amount": amount
                })
                st.rerun()

    with right_matrix:
        st.markdown("<div class='section-header'>Exact Strategic Allocation Directives Matrix</div>", unsafe_allow_html=True)
        
        # Build clean visual table matrix
        matrix_data = {
            "WHERE YOU SPEND": ["📁 Essential Needs", "📁 Personal Lifestyle & Wants", "📁 Future Savings & Investments"],
            "TARGET SPLIT %": [f"{r_needs*100:.0f}%", f"{r_wants*100:.0f}%", f"{r_savings*100:.0f}%"],
            "TARGET ALLOCATION BOUND": [f"{currency_symbol}{target_needs:,.2f}", f"{currency_symbol}{target_wants:,.2f}", f"{currency_symbol}{target_savings:,.2f}"],
            "CURRENT MONTH SPEND": [f"{currency_symbol}{spend_needs:,.2f}", f"{currency_symbol}{spend_wants:,.2f}", f"{currency_symbol}{spend_savings:,.2f}"],
            "AVAILABLE SURPLUS REMAINDER": [f"{currency_symbol}{target_needs-spend_needs:,.2f}", f"{currency_symbol}{target_wants-spend_wants:,.2f}", f"{currency_symbol}{target_savings-spend_savings:,.2f}"]
        }
        st.table(pd.DataFrame(matrix_data))

    # Live Ledger Output below
    st.write("---")
    st.markdown("<div class='section-header'>Live Session Expense Ledger</div>", unsafe_allow_html=True)
    if st.session_state.expenses:
        st.dataframe(pd.DataFrame(st.session_state.expenses), use_container_width=True)
        if st.button("Reset Current Session Logs"):
            st.session_state.expenses = []
            st.rerun()
    else:
        st.info("No expenses recorded yet for the month of June.")

# --- TOOL 2: FINANCIAL GOAL CALCULATOR ---
elif menu_selection == "🧮 Financial Goal Calculator":
    st.markdown("<h1 class='main-title'>🧮 Future Wealth & Compound Calculator</h1>", unsafe_allow_html=True)
    st.write("Project how your **Future Savings & Investments** matrix tier will grow over time.")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        starting_amt = st.number_input(f"Initial Investment Principal ({currency_symbol})", min_value=0, value=10000)
        years = st.slider("Time Horizon (Years)", min_value=1, max_value=40, value=15)
        rate = st.slider("Expected Annual Return / Interest Rate (%)", min_value=1.0, max_value=15.0, value=8.0, step=0.5)
        
        # Suggest regular monthly deposit from the current strategy parameters
        monthly_deposit = st.number_input(f"Suggested Monthly Deposit (From Savings Matrix Bound)", min_value=0.0, value=target_savings)

    # Compute compound logic
    months = years * 12
    monthly_rate = (rate / 100) / 12
    balance_list = []
    current_balance = starting_amt
    
    for m in range(1, months + 1):
        current_balance = (current_balance + monthly_deposit) * (1 + monthly_rate)
        if m % 12 == 0:
            balance_list.append({"Year": m // 12, "Future Value": round(current_balance, 2)})
            
    df_calc = pd.DataFrame(balance_list)

    with col2:
        st.markdown(f"### Target Capitalization Forecast")
        st.metric(label=f"Estimated Total Wealth after {years} Years", value=f"{currency_symbol}{current_balance:,.2f}")
        
        # Dynamic growth chart
        fig = px.line(df_calc, x="Year", y="Future Value", title="Compound Interest Trajectory Curve", color_discrete_sequence=['#7e57c2'])
        st.plotly_chart(fig, use_container_width=True)

# --- TOOL 3: EXPENSE ANALYTICS ---
elif menu_selection == "📈 Expense Analytics":
    st.markdown("<h1 class='main-title'>📈 Allocation Insights & Analytics</h1>", unsafe_allow_html=True)
    
    if st.session_state.expenses:
        df_analytics = pd.DataFrame(st.session_state.expenses)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Outlay Distribution by Category")
            fig_pie = px.pie(df_analytics, values="Amount", names="Category", color_discrete_sequence=px.colors.sequential.Purples_r)
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with col2:
            st.markdown("### Highest Outlay Recipients")
            fig_bar = px.bar(df_analytics, x="Merchant", y="Amount", color="Category", title="Top Merchant Outlays", color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("Please navigate to the Main Matrix Dashboard and enter sample data logs to unlock visual analytic metrics charts.")
