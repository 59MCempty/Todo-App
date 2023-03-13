import function

while True:
    user = input("Enter add, show, edit, delete or exit: ")
    user = user.strip()

    if user.startswith("add"):
        todos = function.get_todos()
        todo = user[4:] + "\n"
        todos.append(todo)

        function.write_todos(todos)

    elif user.startswith("show"):
        todos = function.get_todos()

        for number, value in enumerate(todos):
            value = value.strip("\n")
            print(f"{number + 1}-{value}")

    elif user.startswith("edit"):
        try:
            todos = function.get_todos()

            number_todo_edit = int(user[5:]) - 1
            new_todo = input("Enter new todo: ") + "\n"

            todos[number_todo_edit] = new_todo

            function.write_todos(todos)
        except IndexError:
            print("Number in not valid")
    elif user.startswith("delete"):
        try:
            todos = function.get_todos()

            number_todo_delete = int(user[7:]) - 1
            todos.pop(number_todo_delete)

            function.write_todos(todos)
            print(f"{number_todo_delete} has deleted")
        except IndexError:
            print("Number in not valid")
    elif user.startswith("exit"):
        break
    else:
        print("Syntax is not valid")

print("Bye!")
