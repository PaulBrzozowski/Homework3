#UHID 2037080
# Paul Brzozowski
# Fall 2022




# creates variable to place input and splits string into list
words = input().split()

# for loop to count amount of times word is used in list
for word in words:
    counter = 0
    for item in words:
        if word == item:
            counter += 1

    print(word, counter)