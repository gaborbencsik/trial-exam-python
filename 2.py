# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.


def count_letters(filename):
    count_a = 0
    for character in range(len(filename)):
        if filename[character] == "a":
            count_a += 1
    return count_a

print(count_letters("almafa.txt"))
print(count_letters(""))
