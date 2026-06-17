import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#667eea,#764ba2);
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

.main-card{
    background:rgba(255,255,255,0.95);
    border-radius:30px;
    padding:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.15);
}

.metric-card{
    background:white;
    border-radius:20px;
    padding:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-align:center;
}

.card{
    background:white;
    border-radius:20px;
    padding:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

[data-testid="stSidebar"]{
    background:#f8f9ff;
}

h1,h2,h3{
    color:#1F2937;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("## 💰 Personal Finance")

    selected = option_menu(
        "",
        [
            "Dashboard",
            "Budgeting",
            "Income",
            "Expenses",
            "Investment",
            "Debts",
            "Goals"
        ],
        icons=[
            "house",
            "piggy-bank",
            "graph-up-arrow",
            "wallet2",
            "bar-chart",
            "credit-card",
            "bullseye"
        ],
        default_index=0
    )

# ==================================================
# DATA
# ==================================================

months = [
    "JAN","FEB","MAR","APR","MAY","JUN",
    "JUL","AUG","SEP","OCT","NOV","DEC"
]

income = [
    22000,24000,26000,31000,31000,29000,
    35000,38000,36000,36000,36000,39000
]

expense = [
    23000,29000,25000,22000,25000,26000,
    22000,22000,24000,21000,26000,24000
]

df = pd.DataFrame({
    "Month": months,
    "Income": income,
    "Expense": expense
})

# ==================================================
# MAIN CONTAINER
# ==================================================

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

col1,col2 = st.columns([4,1])

with col1:
    st.title("💰 Personal Finance Dashboard")

with col2:
    st.text_input("", placeholder="Search")

# ==================================================
# MONTH FILTER
# ==================================================

selected_month = st.radio(
    "",
    months,
    horizontal=True
)

st.write("")

# ==================================================
# TOP ROW
# ==================================================

left,middle,right = st.columns([2.2,1,1])

# --------------------------------------------------
# INCOME VS EXPENSE CHART
# --------------------------------------------------

with left:

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=months,
            y=income,
            name="Income",
            marker_color="#7C83FD"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=months,
            y=expense,
            mode="lines+markers",
            name="Expense",
            line=dict(color="#FF4FD8", width=4)
        )
    )

    fig.update_layout(
        title="Income vs Expenses",
        height=320,
        template="plotly_white",
        margin=dict(l=10,r=10,t=40,b=10)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# RATIO DONUT
# --------------------------------------------------

with middle:

    fig2 = go.Figure(
        go.Pie(
            labels=["Income","Expense"],
            values=[56,44],
            hole=.72,
            marker_colors=["#6C63FF","#F472D0"]
        )
    )

    fig2.update_layout(
        title="Ratio",
        height=320,
        showlegend=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# --------------------------------------------------
# DEBIT CARD
# --------------------------------------------------

with right:

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#667eea,#7F56D9);
    border-radius:20px;
    padding:25px;
    color:white;
    height:260px;
    ">
    <h3>💳 Debit Card</h3>
    <br>
    <h1>$4,473</h1>
    <p>Available Balance</p>
    <br>
    <p>**** **** **** 4851</p>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# BOTTOM SECTION
# ==================================================

c1,c2,c3,c4 = st.columns(4)

# --------------------------------------------------
# BUDGET PLAN
# --------------------------------------------------

with c1:

    fig3 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=46,
            title={"text":"Budget Used"},
            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"#7C3AED"}
            }
        )
    )

    fig3.update_layout(height=280)

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# --------------------------------------------------
# INVESTMENT
# --------------------------------------------------

with c2:

    fig4 = go.Figure()

    fig4.add_trace(
        go.Scatterpolar(
            r=[90,70,55,80,60],
            theta=[
                "Stocks",
                "Mutual Fund",
                "Gold",
                "FD",
                "Crypto"
            ],
            fill="toself"
        )
    )

    fig4.update_layout(
        title="Investment",
        height=280
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# --------------------------------------------------
# GOALS
# --------------------------------------------------

with c3:

    fig5 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=40,
            title={"text":"Financial Goal"},
            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"#4F46E5"}
            }
        )
    )

    fig5.update_layout(height=280)

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

with c4:

    summary = pd.DataFrame({
        "Category":[
            "Budget",
            "Income",
            "Expenses",
            "Investment",
            "Debts",
            "Goals"
        ],
        "Amount":[
            138014,
            87812,
            68970,
            96171,
            79116,
            93644
        ]
    })

    st.subheader("Summary")

    st.dataframe(
        summary,
        hide_index=True,
        use_container_width=True
    )

# ==================================================
# AI INSIGHTS
# ==================================================

st.subheader("🧠 AI Financial Insights")

income_total = sum(income)
expense_total = sum(expense)

saving_rate = round(
    ((income_total-expense_total)/income_total)*100,
    1
)

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Savings Rate",
        f"{saving_rate}%"
    )

with col2:
    predicted = expense_total * 1.08

    st.metric(
        "Predicted Next Month Expense",
        f"${predicted:,.0f}"
    )

with col3:

    if saving_rate > 20:
        st.success("Healthy Financial Status")
    elif saving_rate > 10:
        st.warning("Moderate Financial Status")
    else:
        st.error("High Spending Risk")

# ==================================================
# TRANSACTIONS
# ==================================================

st.subheader("Recent Transactions")

transactions = pd.DataFrame({
    "Date":[
        "01-Apr",
        "04-Apr",
        "06-Apr",
        "10-Apr",
        "14-Apr"
    ],
    "Description":[
        "Salary",
        "Amazon",
        "Netflix",
        "Electricity Bill",
        "Restaurant"
    ],
    "Amount":[
        5000,
        -250,
        -15,
        -120,
        -90
    ]
})

st.dataframe(
    transactions,
    use_container_width=True,
    hide_index=True
)

# ==================================================
# DOWNLOAD
# ==================================================

st.download_button(
    "📥 Export Transactions",
    transactions.to_csv(index=False),
    file_name="finance_report.csv"
)

st.markdown("</div>", unsafe_allow_html=True)
