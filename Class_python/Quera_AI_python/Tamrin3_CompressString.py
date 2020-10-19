a = str(input())
counter = 1
final_my_str = ""
first = a[0]
if len(a) == 1:
    final_my_str += first + "1"
for ch in range(1, len(a)):
    if a[ch] == first:
        counter += 1
    if a[ch] != first:
        final_my_str += first + str(counter)
        counter = 1
        first = a[ch]
    if ch == len(a) - 1:
        final_my_str += first + str(counter)
print(final_my_str)
