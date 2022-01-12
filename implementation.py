# implementation.py
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
import time
import datetime


# 퀴즈
# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 x 1  크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. 여행가 A는 상, 하, 좌, 우 방향으로
# 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있습니다.
# 여행가 A가 N x N 크기의 정사각형 공간을 벗어나느 움직임은 무시 됩니다. 예를 들어 (1, 1)의 위치 에서 L 혹은
# U를 만나면 무시 됩니다.

# 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다.
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다.
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백을 기준으로 구분하여 출력합니다.
n = int(input())
plan = list(input().split())
# R R R U D D

start_time = time.time()

start = [1, 1]
for i in plan:
    if i == 'L':
        start[1] -= 1
    if i == 'R':
        start[1] += 1
    if i == 'U':
        start[0] -= 1
    if i == 'D':
        start[0] += 1
    if start[0] == 0:
        start[0] += 1
    if start[1] == 0:
        start[1] += 1

print(start)

end_time = time.time()
result = str(datetime.timedelta(end_time - start_time))
print(result)

# 해설

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
nx, ny = 0, 0

start_time = time.time()

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

end_time = time.time()
result = str(datetime.timedelta(end_time - start_time))
print(result)

# 퀴즈
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를
# 구하는 프로그램을 작성하세요. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
# 0 <= N <= 23

n = int(input())
time_self = [0, 0, 0]
count = 0

st_time = time.time()

for i in range(n+1):
    time_self[0] = i
    for j in range(60):
        time_self[1] = j
        for k in range(60):
            time_self[2] = k
            nums = []
            for n in time_self:
                for m in str(n):
                    nums.append(m)
            if '3' in nums:
                count += 1

print(count)
ed_time = time.time()
print(f'{ed_time - st_time:.5f} sec')

# 컴퓨터는 1초에 2천만번 정도의 연산을 한다고 가정하고 푸는 것이 합리적이다.

# 해설
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 퀴즈
# 8 x 8 좌표 평면에서 나이트가 움직일 수 있는 모든 경우의 수를 구하세요
# 나이트는 수평으로 두 칸 이동 후 수직으로 한칸 이동
# 수직으로 두 칸 이동 후 수평으로 한칸 이동 만 가능
# 행은 1 ~ 8 열은 a ~ h 로 표현 한다.

n = str(input())
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

st_time = time.time()
start_pos = []
for i, c in enumerate(columns):
    for j, r in enumerate(rows):
        if n == c + r:
            start_pos += [i, j]

print(start_pos)
a = start_pos[0]
b = start_pos[1]

count = 0
for m in move:
    a += m[0]
    b += m[1]
    if a > 0 and b > 0 and columns[a] + rows[b] != n:
        count += 1
    a = start_pos[0]
    b = start_pos[1]

print(count)

ed_time = time.time()
print(f'{ed_time - st_time:.5f} sec')

# 해설
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 퀴즈
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 1 <= 문자열의 길이 <= 10,000

n = input()

num_li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

new, num = [], 0
for w in n:
    if w in num_li:
        num += int(w)
    else:
        new.append(w)
        print(new)

new.sort()

anw = ''
for s in new:
    anw += s

anw += str(num)

print(anw)

# 이렇게 하면 됨
if num != 0:
    print(''.join(new) + str(num))
else:
    print(''.join(new))

# 해설
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))


