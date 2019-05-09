

def add_number(num1, num2):
    return num1 + num2


def print_people(*people):

    """Sorts the list of people passed in, and prints out each name

    Parameters:
        people (list): List of strings denoting names

    Returns:
        Nothing

    """

    sort_people = sorted(people)
    for person in sort_people:
        print(person)


print(add_number(2, 3))
print_people("Dave", "Sam", "Chris", "Simon", "Agatha", "Dimitri")
print(print_people.__doc__)
help(print_people)
