import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
background:#F5F7FA;
}

[data-testid="stSidebar"]{
background:#111827;
}

.metric-card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 2px 10px rgba(0,0,0,0.08);
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 2px 10px rgba(0,0,0,0.08);
}

h1,h2,h3{
color:#111827;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 💰 Finance AI")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Transactions",
            "Analytics",
            "Goals",
            "Settings"
        ],
        icons=[
            "house",
            "credit-card",
            "graph-up",
            "bullseye",
            "gear"
        ],
        default_index=0
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

col1,col2 = st.columns([4,1])

with col1:
    st.title("Welcome Back 👋")
    st.caption("Track your finances smarter")

with col2:
    st.text_input("",placeholder="Search")

st.divider()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Total Income",
        "$8,500",
        "+35%"
    )

with c2:
    st.metric(
        "Total Spending",
        "$3,500",
        "+7%"
    )

with c3:
    st.metric(
        "Budget Goal",
        "$9,254",
        "+15%"
    )

with c4:
    st.metric(
        "Transactions",
        "17,000",
        "+85%"
    )

# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------

months = [
"Jan","Feb","Mar","Apr","May","Jun",
"Jul","Aug","Sep","Oct","Nov","Dec"
]

income = [
3000,3500,4200,3900,4500,5200,
5400,6200,6500,7200,8100,8500
]

expense = [
2200,2600,3100,2800,2900,3300,
3400,3600,3700,3800,3900,3500
]

df = pd.DataFrame({
    "Month":months,
    "Income":income,
    "Expense":expense
})

# --------------------------------------------------
# CHARTS
# --------------------------------------------------

left,right = st.columns([2,1])

with left:

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Income"],
            mode='lines+markers',
            name="Income"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Expense"],
            mode='lines+markers',
            name="Expense"
        )
    )

    fig.update_layout(
        title="Cash Flow Trend",
        template="plotly_white",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    progress = 72

    fig2 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=progress,
            title={"text":"Savings Goal"},
            gauge={
                "axis":{"range":[0,100]}
            }
        )
    )

    fig2.update_layout(height=420)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# --------------------------------------------------
# BOTTOM SECTION
# --------------------------------------------------

left,right = st.columns([2,1])

with left:

    st.subheader("Recent Transactions")

    tx = pd.DataFrame({
        "Name":[
            "Amazon",
            "Netflix",
            "Salary",
            "Uber",
            "Swiggy"
        ],
        "Category":[
            "Shopping",
            "Subscription",
            "Income",
            "Transport",
            "Food"
        ],
        "Amount":[
            -250,
            -15,
            5000,
            -80,
            -40
        ]
    })

    st.dataframe(
        tx,
        use_container_width=True,
        hide_index=True
    )

with right:

    spend = pd.DataFrame({
        "Category":[
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Others"
        ],
        "Amount":[
            900,
            700,
            1200,
            600,
            300
        ]
    })

    fig3 = px.pie(
        spend,
        names="Category",
        values="Amount",
        hole=.65
    )

    fig3.update_layout(
        title="Expense Distribution",
        height=350
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
