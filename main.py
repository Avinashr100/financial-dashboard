
import streamlit as st

st.set_page_config(page_title="📊 Financial Tools", layout="centered")

st.title("🧭 Choose a Financial View")
st.markdown("Welcome! Select what you'd like to explore:")

st.page_link("financials_app.py", label="📘 Monthly Financial Statements", icon="📅")
st.page_link("yearly_summary_app.py", label="📆 Yearly Summary Comparison", icon="📈")
st.page_link("dashboard_app.py", label="📊 Dashboard - Trends", icon="📊")
