import streamlit as st
import pandas as pd
import numpy as np

st.title("3. Charts Demo")

data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
