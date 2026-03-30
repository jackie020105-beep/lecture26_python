stack=[]
capacity = 5

def isFull():
    if len(stack) == capacity:
        return True
    else:
        return False
    
def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False



def push(data):
    if isFull():
        print('satck이 차 있어서 더 이상 추가 불가')
    else:
        stack.append(data)
def pop():
    if isEmpty():
        print('satck에 빠져나갈 수가 없음')
        return -1
    else:
        return stack.pop()
def peek():
    if isEmpty():
        print('satck에 출력할 수가 없음')
        return -1
    else:
        print(stack[-1])
    




print(f'[[정수형 스택 연산 실습 (용량 : {capacity})]]')



while True:
    # 메뉴를 출력
    print('==========================')
    print('1.push 2.Pop 3.Peek 0.Exit')
    print('==========================')
    menu = int(input('> 메뉴 선택:'))
    if menu == 0:
        break
    elif menu == 1:
        data = int(input('데이터 입력:'))
        push(data)
    elif menu == 2:
        data = pop()
        print(('> [pop] 가져온 데이터:', data))
    elif menu == 3:
        data = peek()
        

    print(('> 현재 스택 상태:', stack))

print('[[정수형 스택 연산 실습 종료]]')