# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_param(old_list):
    new_list = []
    try:
        if type(old_list) is list:
            for item in old_list:
                new_list.append(2 * item)
            return new_list
    except ValueError:
        print('This is not a list') # None-t ír csak :(


lista = [3, 4, 5, 6]
print(double_param(lista))

lista2 = "string"
print(double_param(lista2))

lista3 = ["a", "b"]
print(double_param(lista3))
