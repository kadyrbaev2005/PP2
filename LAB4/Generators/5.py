def down(n):
    i = 0
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in down(n):
    print(i)