N = int(input("Enter the No of Students: "))
my_list = []
weight_list = []
weight_list2 = []
i = 0
while i < N:
    k = float(input("Enter the weight in lbs of Student {}: ".format(i+1)))
    my_list.append(k)
    i = i + 1
print(my_list)
# Using Loops
print("Using Loops:")
for n in my_list:
    weight_list.append(n * 0.453592)
print(weight_list)
# Using List Comprehensions
print("Using List Comprehensions:")
weight_list2 = [n * 0.453592 for n in my_list]
print(weight_list2)
