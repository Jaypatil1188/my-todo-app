import streamlit as st
import Module

todos = Module.my_Todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Module.write_Todo(todos)


st.title("My Todo App")
st.subheader("Hell0,Welcome")

try:
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            Module.write_Todo(todos)
            del st.session_state[i]
            st.rerun()
except IndexError:
    st.popover("please click wisely")


st.text_input(label=" ", placeholder="Add Todos here",
              on_change=add_todo, key='new_todo')

