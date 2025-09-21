import streamlit as st

st.title("⚡ Cable Sizing Tool")
st.write("Hello, this is a test deployment!")

# Example input
load_current = st.slider("Load Current (A)", 5, 60, 20)

st.write(f"Selected load current: {load_current} A")
