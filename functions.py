
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):      # function with default argument
    """ Read a test file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local      # returns as list


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)      # does not return a value


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())
