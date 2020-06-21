f = 2
n = int(input('Enter an integer (2 or greater):'))
if n < 2:
    print('Error, Please enter a number equal or greater than 2.')
else:
    print('The prime factors of {0} are:'.format(n))
    while f != n:
        if n%f == 0:
            print(f)
            n = int(n/f)
        else:
            f = f + 1
    print(n)

