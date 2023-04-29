def my_function(palindrome):
    if palindrome == palindrome[::-1]:
        print ("Yes, it is!")
    else:
        print ("No, it isn't")

x = str(input())
my_function(x)

