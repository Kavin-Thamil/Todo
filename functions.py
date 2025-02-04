FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ To read the To-dos from the file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """To write in the To-dos file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())