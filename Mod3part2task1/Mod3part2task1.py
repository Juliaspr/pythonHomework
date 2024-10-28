original_list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
original_list = sorted([str(x)for x in original_list])
repetitive_list=[]
i=0

for i in range(0, len(original_list)-1):
    if original_list[i] == original_list[i+1]:
        repetitive_list.append(original_list[i])
print(repetitive_list)
