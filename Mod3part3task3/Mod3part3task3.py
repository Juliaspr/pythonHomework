num_list = [56, 9, 11, 2, 35, 45]
new_num_list = []

def decimal(num_list):
    for i in range(0, len(num_list)):
        new = num_list[i]
        if new>10:
            while new>10:
                new = new // 10
            new_num_list.append(new)
        else: new_num_list.append(new)


def max_num(new_num_list, num_list):
    max_num_list = []
    while any(x>0 for x in new_num_list):
        i = new_num_list.index(max(new_num_list))
        max_num_list.append(num_list[i])
        new_num_list[i] = 0
    max_num = int(''.join(map(str,max_num_list)))
    print(max_num)


decimal(num_list)
max_num(new_num_list, num_list)

