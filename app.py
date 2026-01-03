import streamlit as st

st.set_page_config(page_title="Email Dashboard", layout="centered")

st.title("📊 Email Monitoring Dashboard")

st.metric("📥 Inbox", 120)
st.metric("🚫 Spam", 25)
st.metric("📤 Sent", 300)
st.metric("❌ Failed", 5)

st.subheader("📌 Status")
st.success("SMTP Server is Active")
