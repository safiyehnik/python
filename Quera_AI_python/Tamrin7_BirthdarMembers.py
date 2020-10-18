import statistics
birthday_age = input().split(" ")
my_list = []
for number in birthday_age:
    my_list.append(int(number))
sorted(my_list)
average = statistics.mean(my_list)
mid = statistics.median(my_list)
mod = statistics.mode(my_list)
convert_average = "{:.2f}".format(average)
convert_mid = "{:.2f}".format(mid)
print(convert_average)
print(convert_mid)
print(mod)
