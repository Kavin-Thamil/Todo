import streamlit as st
import functions

todos = functions.get_todos()

st.header("To-Do App")
st.subheader("This is a To-do app")
st.text("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)