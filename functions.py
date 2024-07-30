FILEPATH = "Files/todo.txt"


def get_todos(filepath=FILEPATH):
    """ Function to get the todos from the text file"""
    with open(filepath, 'r') as func_file:
        func_todos = func_file.readlines()
    return func_todos


def write_todos(write_func_todos, filepath=FILEPATH):
    """Function to write the todos to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(write_func_todos)


if __name__ == "__main__":
    print("test")
    print(get_todos())
