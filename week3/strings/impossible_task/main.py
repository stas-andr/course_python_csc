s = input()
a = input()
b = input()

count_change_str = 0

if a in b and a in s:
    print("Impossible")
else:
    while count_change_str <= 1000:
        old_string = s
        s = s.replace(a, b)
        if  s != old_string:
            count_change_str += 1  
        else:
            break
    if count_change_str > 1000:
        print("Impossible")
    else:
        print(count_change_str)
