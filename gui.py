import PySimpleGUI as sg
from function import get_todos,write_todos
import time

clock = sg.Text(' ', key="clock")
label = sg.Text("Add todo")
input_box = sg.Input(tooltip="Enter new Todo", key="todo_input")
add_button = sg.Button("Add")

edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
list_todo = sg.Listbox(values=get_todos(), key="todo_edit", enable_events=True, size=[45, 10])

window = sg.Window("My Todo App", layout=[[clock],
                                          [label],
                                          [input_box, add_button],
                                          [list_todo, edit_button, delete_button],
                                          ],
                                          font=("Helvatica", 20))


while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo_input"] + "\n"
            todos.append(new_todo)

            print(todos)

            write_todos(todos)

            window["todo_input"].update(value="")
            window["todo_edit"].update(values=todos)
        case "Edit":
            try:
                todos = get_todos()
                edit_todo = values["todo_input"] + "\n"
                edit = values["todo_edit"][0]

                index = todos.index(edit)
                todos[index] = edit_todo

                write_todos(todos)
                window["todo_input"].update(value=edit_todo)
                window["todo_edit"].update(values=todos)
            except IndexError:
                sg.popup("Please type or select item first")
        case "Delete":
            todos = get_todos()

            delete_todo = values["todo_edit"][0]

            todos.remove(delete_todo)

            write_todos(todos)

            window["todo_edit"].update(values=todos)
        case sg.WIN_CLOSED:
            break
window.close()
