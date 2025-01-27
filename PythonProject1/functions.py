FILEPATH = "todos.txt"

def get_todo(filename = FILEPATH):
    """ To read the To-dos from the file"""
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todo(todos_local, filename = FILEPATH):
    """To write in the To-dos file"""
    with open(filename, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print(get_todo())