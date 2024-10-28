num_list = [56, 9, 11, 2, 35, 45]
new_num_list = []


def max_num():
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):
            if num_list[i] == num_list[j]:
                print(num_list[i], num_list[j])
                print(new_num_list)
                break
            if num_list[i] < 10 < num_list[j]:
                new_num = num_list[j]
                while new_num >= 10:
                    new_num //= 10
                if new_num > num_list[i]:
                    new_num_list.append(num_list[j])
                elif new_num < num_list[i]:
                    new_num_list.append(num_list[i])
                print(num_list[i], num_list[j])
                print(new_num_list)
                break
            elif num_list[i] > 10 > num_list[j]:
                new_num = num_list[i]
                while new_num >= 10:
                    new_num //= 10
                if new_num > num_list[j]:
                    new_num_list.append(num_list[i])
                elif new_num < num_list[j]:
                    new_num_list.append(num_list[j])
                print(num_list[i], num_list[j])
                print(new_num_list)
                break
            elif (num_list[i] <= 10 and num_list[j] <= 10) or (num_list[i] > 10 and num_list[j] > 10):
                if num_list[i] > num_list[j]:
                    new_num_list.append(num_list[i])
                elif num_list[i] < num_list[j]:
                    new_num_list.append(num_list[j])
                print(num_list[i], num_list[j])
                print(new_num_list)
                break
    print(new_num_list)


max_num()

