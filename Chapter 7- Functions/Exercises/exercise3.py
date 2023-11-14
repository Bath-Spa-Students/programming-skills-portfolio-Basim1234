#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('small', 'Art Gallery!')
make_shirt(message="Bath spa.", size='large')