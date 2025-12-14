import streamlit as st
import pandas as pd

st.title("1. Basic Page Elements")

st.header("Headers and text")
st.subheader("This is a subheader")
st.caption("Small, grey caption text")

st.write("`st.write` is very flexible.")
st.text("Plain fixed-width text.")
st.markdown("You can use **Markdown** and *italic* text.")

st.divider()

st.header("Display data")
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 32, 29]
})
st.dataframe(df)

st.divider()

st.header("Images")
st.image(
    "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
    caption="Streamlit logo"
)
