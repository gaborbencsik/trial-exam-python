# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def count_letters_in_file(filename):
    count_a = 0
    f = open(filename, 'r')
    rows = f.readlines()
    f.close()

    for line in rows:
        for character in line:
            if character == "a":
                count_a += 1
    return count_a

print(count_letters_in_file('text.txt'))
