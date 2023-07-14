
# function which return reverse of a string
def palindrome(z):
    return z == z[::-1]

z = "16461"

ans = palindrome(z)

if ans:
    print("Yes")
else:
    print(" No")



x = ["1","2","3","1","3","4"]
x = list(dict.fromkeys(x))
print(x)

def duplicate(numbers):
    return list(set(numbers))
lst = duplicate(["a","b","c","a"])
print(lst)



x = input("num1")
y = input("num2 ")

sum = int(x) + int(y)

print("The sum is: ", sum)
