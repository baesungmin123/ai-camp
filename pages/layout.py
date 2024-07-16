import streamlit as st

st.bar_chart({"data": [1,5,2,6,2,1]})

with st.expandar("See explanation"):
    st.write(st.session_state.key)
    st.image("https://static.streamlit.io/examples/dice.jp")