# 리스트와 반복구조 프로그래밍 연습
# 정수로 구성되어 있는 리스트를 파라미터로 입력받아 다음의 기능을 수행하는 함수 구현


# getIndex(num_list, target)
# - 주어진 데이터 target이 어디에 저장되어 있는지 index를 반환

num_list = [23, 45, 27, 11, 25, 65, 78]

def getIndex(num_list, target):
    for i in range(len(num_list)):
        if num_list[i]==target:
            return i

print(getIndex(num_list, 25))


# getMax(num_list)
# - 리스트에 저장된 숫자 중 가장 큰 숫자 반환

num_list = [23, 45, 27, 11, 25, 65, 78]
def getMax(num_list):
    a = num_list[0]
    for i in range(len(num_list)):
        if num_list[i]>a:
            a=num_list[i]
    return a
print(getMax(num_list))                   

# getMin(num_list)
# - 리스트에 저장된 숫자 중 가장 작은 숫자 반환

num_list = [23, 45, 27, 11, 25, 65, 78]
def getMin(num_list):
    a = num_list[0]
    for i in range(len(num_list)):
        if num_list[i]<a:
            a=num_list[i]
    return a
print(getMin(num_list))    


# countGT(num_list, target)
# - 리스트에 저장된 숫자 중 입력된 숫자 target보다 큰 수가 몇 개 있는지 구하여 반환

num_list = [23, 45, 27, 11, 25, 65, 78]
def countGT(num_list, target):
    count = 0
    for i in range(len(num_list)):
        if num_list[i] > target:
            count += 1
    return count 

print(countGT(num_list, 42))



# sumList(nun_list)
# - 리스트에 저장된 모든 값 더하여 반환

num_list = [23, 45, 27, 11, 25, 65, 78]
def sumList(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
    return sum

print(sumList(num_list))


# swapList(num_list)
# - 리스트에 저장된 숫자를 역순으로 저장

num_list = [23, 45, 27, 11, 25, 65, 78]
def swapList(num_list):
    for i in range(len(num_list)//2):
        num_list[i], num_list[len(num_list) - 1 - i] = num_list[len(num_list) - 1 - i], num_list[i]
    return num_list

print(swapList(num_list))