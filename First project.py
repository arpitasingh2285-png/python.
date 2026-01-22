def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
#driver code
num=int(input("Enter the number of terms:"))
print("Fibonacci series:")
for term in fibonacci(num):
    print(term,end=" ")