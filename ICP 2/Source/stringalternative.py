def string_alternative():
    string_name = input("Please enter any string: ")
    print(string_name)
    # length of the string
    sl = len(string_name)
    print(sl)
    i = 0
    # creating a new string
    new_string = ""
    while i < sl:
        if i % 2 == 0:
            new_string += string_name[i]
        i = i+1
    print(new_string)

if __name__ == '__main__':
    string_alternative()


