n, m = map(int, input().split())
k = int(input())
my_list_i = []
my_list_j = []
my_list = []
for x in range(1, k+1):
    (i, j) = input().split()
    my_list_i += i
    my_list_j += j
print(*my_list_i)
print(*my_list_j)
for row in range(1, n+1):
    for column in range(1, m+1):
        print("*", end=" ")
    print()
