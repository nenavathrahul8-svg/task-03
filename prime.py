num = int(input("enter an integer"))
if num <=1:
    print(f'{num} is not prime.')
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not prime.')
            print(f'{i} is the factor of {num}.')
            break
    else:
        print(f'{num} is prime.')


# string palindrome
s = input("enter a string:")
rahul=(s[::-1])
if rahul==s:
    print("palindrome")
else:
    print("not palindrome")
