bottles = 100
while bottles >= 1:
    if bottles == 1:
        print("There is 1 bottle of beer on the wall")
        break
    print("There are " + str(bottles) + " bottles of beer on the wall")
    print("taking one down")
    bottles -= 1