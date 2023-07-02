try:
    a = float(input("float: "))
    print("{:,.2f}".format(a))
except ValueError:
    pass
