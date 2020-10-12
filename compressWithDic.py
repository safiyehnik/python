a = "ddDDCCCfghhhd"
new_my_str = {}
for ch in a:
    if ch in new_my_str:
        new_my_str[ch] += 1
    else:
        new_my_str[ch] = 1
for char in new_my_str:
    if new_my_str[char] > 1:
        print(str(new_my_str[char]) + char, end="")
    else:
        print("1" + char, end="")


