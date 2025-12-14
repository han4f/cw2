import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title("Layout Demo")

with st.sidebar:
    st.header("Controls")
    n = st.slider("Number of rows", 10, 200, 50)

data = pd.DataFrame(np.random.randn(n, 3), columns=["A", "B", "C"])

col1, col2 = st.columns(2)
with col1:
    st.line_chart(data)
with col2:
    st.bar_chart(data)

with st.expander("See data"):
    st.dataframe(data)
