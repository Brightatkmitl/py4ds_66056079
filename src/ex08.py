"""
Execise 8
"""


def write_to_file(file, text):
    with open(file,'w') as fileObj:
        fileObj.write(text)




    """
    Write the given message to a file with the provided filename.

    Args:
        filename (str): The name of the file to write to.
        message (str): The message to write to the file.

    Returns:
        None
    """
    # TODO : complete this
    pass


def read_from_file(file):
    with open(file) as fileObj:

        return fileObj.read()


    """
    Read the contents of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    # TODO : complete this
    pass


def append_to_file(file, text):
    with open(file,"a") as fileObj:
        fileObj.write(text)

    """
    Append the given message to the end of the specified file.

    Args:
        filename (str): The name of the file to append the message to.
        message (str): The message to append to the file.

    Returns:
        None: This function does not return anything.
    """
    # TODO : complete this
    pass
