# 정렬 :  선택정렬, 버블정렬, 퀵정렬...

# 1. 오름차순(작은값을 앞으로 배치)
dataset = [3,5,1,2,4]
n = len(dataset)

print(f"dataset:{dataset}, 개수:{n}")

print("1. 선택정렬: 오름차순")
for i in range(0, n-1): #총개수-1 : 5-1개

    for j in range(i+1, n):
        # print(f"dataset[{i}]={dataset[i]} > dataset[{j}]={dataset[j]}")

        if (dataset[i] > dataset[j]):
            temp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = temp

    print(i+1,dataset)


print("2. 선택정렬: 내림차순")
for i in range(0, n-1): #총개수-1 : 5-1개

    for j in range(i+1, n):
        # print(f"dataset[{i}]={dataset[i]} > dataset[{j}]={dataset[j]}")

        if (dataset[i] < dataset[j]):
            # temp = dataset[i]
            # dataset[i] = dataset[j]
            # dataset[j] = temp
            dataset[i], dataset[j] = dataset[j], dataset[i]

    print(i+1,dataset)
