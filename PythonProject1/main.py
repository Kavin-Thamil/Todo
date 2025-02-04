#from PythonProject1.module.functions import get_todo, write_todo

import functions
import time

now = time.strftime("%H:%M:%S, %d-%m-%y")
print("It is now: ", now)

while True:
    user_input = input("Enter add, show, edit, remove or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = functions.get_todo()

        todos.append(todo.capitalize() + '\n')

        functions.write_todo(todos)

    elif user_input.startswith("show"):

        todos = functions.get_todo()

        #new_todos = (item.strip('\n') for item in todos) list comprehension method

        for index, item in enumerate(todos):
            item=item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_input.startswith("edit"):

        try:
            number = int(user_input[5:])
            number = number - 1

            todos = functions.get_todo()

            new_todo = input("Enter the new one: ")
            todos[number] = new_todo.capitalize() + '\n'

            functions.write_todo(todos)

        except ValueError:
            print("Invalid command!")
            continue

    elif user_input.startswith("remove"):

        try:
            number = int(user_input[7:])

            todos = functions.get_todo()

            index = number - 1
            todo_to_be_removed = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todo(todos)

            message = f"The item *{todo_to_be_removed}* was removed from the list."
            print(message)

        except IndexError:
            print("This command does not exist!")
            continue

    elif user_input.startswith("exit"):
        break

    else:
        print("Invalid command!")

print("Bye bye!")