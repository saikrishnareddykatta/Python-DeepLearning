file = open("info.txt","r+")
# creating a dictionary to save the words and their counts
count = {}
# reading each word in the file split with space
for word in file.read().split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
file.write(str(count))
file.close()