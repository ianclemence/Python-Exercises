# Python Program
# to read file character by character


file = open('File1.txt', 'r')

while 1:

    # read by character
    char = file.read(1)
    if not char:
        break

    print(char)

file.close()