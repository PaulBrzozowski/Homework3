#list input
inp = input()
#converting input to list of integers
arr = list(map(int, inp.split(" ")))
#list to hold non negative numbers
positive_arr = []
#appending non negative numbers to positive_arr
for i in range(len(arr)):
    if arr[i]>=0:
        positive_arr.append(arr[i])
#sorting 
positive_arr.sort()
#printing the output
for i in range(len(positive_arr)):
    print(positive_arr[i], end=" ")
    