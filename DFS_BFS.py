# DFS_BFS.py
from collections import deque


# 그래프 탐색 알고리즘의 대표적인 두 가지 알고리즘 DFS BFS

# 두 가지 자료구조
# 스택 자료구조 - 먼저 입력된 자료가 나중에 출력된다. 선입 후출. 박스 쌓기.

# 큐 자료구조 - 먼저 입력된 자료가 먼저 나가는 형식. 선입 선출. 터널과 같은 형태.
# 큐 자료구조를 이용할 때는 collections 안에 deque 라이브러리를 이용한다.
# deque 라이브러리는 큐와 스택 둘의 장접을 합친 라이브러리 라고 할 수 있다.

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(5)
queue.append(7)
queue.append(5)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# deque([3, 5, 7, 5, 1, 4])
# deque([4, 1, 5, 7, 5, 3])


# 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.
def recursive_function_1():
    print('재귀 함수를 호출합니다')
    recursive_function_1()


# 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
def recursive_function_2(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function_2(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')


# 팩토리얼 구현(수학적으로 0!과 1!의 값은 1입니다.)
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:      # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)


# 최대공약수 계산(유클리드 호제법) gcd = greatest common divisor 최대 공약수
# 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R 이라고 할때
# A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# recursive_function_1()
# recursive_function_2(1)               # 스택에 자료를 넣었다가 꺼내고 종료하는 것같이 나옴.
# print('반복적으로 구현:', factorial_iterative(5))
# print('재귀적으로 구현:', factorial_recursive(5))
print(gcd(192, 162))

# 재귀합수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있지만 타인이 이해하기 어려울 수 있다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
# 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.
# DFS를 구현할 때 많이 사용하곤 함.



