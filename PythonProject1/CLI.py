#from PythonProject1.module.functions import get_todo, write_todo

from PythonProject1 import functions
import time

now = time.strftime("%H:%M:%S, %d-%m-%y")
print("It is now: ", now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.capitalize() + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        #new_todos = (item.strip('\n') for item in todos) list comprehension method

        for index, item in enumerate(todos):
            item=item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new one: ")
            todos[number] = new_todo.capitalize() + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command!")
            continue

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[7:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_be_removed = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"The item *{todo_to_be_removed}* is completed!."
            print(message)

        except IndexError:
            print("This command does not exist!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command!")

print("Bye bye!")