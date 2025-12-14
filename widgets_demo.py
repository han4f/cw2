import streamlit as st

st.title("2. Basic Widgets Demo")

name = st.text_input("What is your name?")
if st.button("Say hello"):
    if name:
        st.success(f"Hello, {name} 👋")
    else:
        st.warning("Please enter your name")

age = st.number_input("Your age", 0, 120, 25)
st.write("Age:", age)

color = st.selectbox("Favourite colour", ["Red", "Green", "Blue"])
st.write("Colour:", color)

agree = st.checkbox("I agree")
if agree:
    st.info("Thanks for agreeing")

date = st.date_input("Pick a date")
st.write("Date:", date)
