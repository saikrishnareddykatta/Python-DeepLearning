# String entered by user
stringInput = input("Please Enter an String: ")
# checking if word "python" is present in the string and replacing it with "pythons"
if "python" in stringInput:
    print(stringInput.replace("python", "pythons"))
else:
    print("there is no word named python in the string provided by the user")