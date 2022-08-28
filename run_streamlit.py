import pandas as pd
import streamlit as st


def load_data(PATH):
    return pd.read_excel("dump.xlsx")


st.title("FPL sortings alg.")

data = load_data("x")

st.subheader("Raw data")

now_cost = st.slider("now_cost", 40, 140, (40, 140))  # min: 0h, max: 23h, default: 17h


filtered_data = data[(data["now_cost"] < now_cost[1]) & (data["now_cost"] > now_cost[0])]

columns = st.multiselect(
    "select columns", filtered_data.columns.tolist(), default=filtered_data.columns.tolist()
)

st.dataframe(filtered_data[columns])