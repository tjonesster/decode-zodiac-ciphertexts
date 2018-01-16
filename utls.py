

def get_ciphertext(path_to_file_with_ciphertext):
    """ Returns a list of lists

    :param path_to_file_with_ciphertext:
    :return:
    """
    with open(path_to_file_with_ciphertext) as inputfile:
        rows_of_ciphertext_characters = [[character for character in row.strip()] for row in inputfile.readlines()]
    return rows_of_ciphertext_characters

