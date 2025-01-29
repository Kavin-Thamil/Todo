FILEPATH = "todos.txt"

def get_todos(filename = FILEPATH):
    """ To read the To-dos from the file"""
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filename = FILEPATH):
    """To write in the To-dos file"""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())