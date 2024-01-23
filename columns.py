import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("https://c.pxhere.com/photos/f2/77/iris_flower_purple-1401467.jpg!d")

with col2:
   st.header("Verginica")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Setosa")
   st.image("https://static.streamlit.io/examples/owl.jpg")