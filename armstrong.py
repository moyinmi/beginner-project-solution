
number = input("Enter a number: ")
n = len(number)

def myfunc(number, n):
    number_total = 0
    for no in str(number):
        number_total += int(no)**n
    if number_total == int(number):
        return "It's Armstrong"
    else:
        return "It's not Armstrong"
print(myfunc(number, n))
