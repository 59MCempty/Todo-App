import streamlit as st
import function


todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo-App")
st.header("This is My Todo-App")
st.subheader("This app is to increase your productivity")

text_todo = st.text_input(label="Enter todo",placeholder="Type Here", on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.session_state