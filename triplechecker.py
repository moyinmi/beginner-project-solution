def triple_checker():
    while True:
        a = int(input("Enter a side: "))
        b = int(input("Enter a side: "))
        c = int(input("Enter a side: "))
        h = max(a, b, c)
        if (a**2) + (b**2) == (h**2):
            print("Triangle is a pythagorean triple")
        else:
            print("triangle is not a pythagorean tripple")

triple_checker()
