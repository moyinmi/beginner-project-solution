num = int(input("Enter a number in the order to generate the sequence; "))

def sequenceGenerator(num):
    a = 0
    b = int(input("Enter the number that you want to produce a fibbonaci series for: "))
    if num <= a:
        print("please a enter a postive integer")
    elif num == b:
        print("Fibonacci sequence", num, ":")
        print(a)
    elif num > 1:
        print(a, b, end=" ")
        for i in range(2, num):
            c = a+b
            print(c, end=" ")
            a,b = b,c

sequenceGenerator(num)