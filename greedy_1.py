# greedy_1.py
import time
import datetime

# 퀴즈
# 거스름돈 문제
# 거슬러 줘야 할 돈에 대해 최소의 동전갯수로 거슬러 주면 몇개의 동전이 필요할까요?
change = 1260
coin = [500, 100, 50, 10]

count = 0

for c in coin:
    count += change // c
    change %= c

print(count)

# 그리디 알고리즘이란 현재 상황에서 지금 당장 좋은 것만 고르는 방법.
# 늘 최선의 결과를 얻는다는 보장은 없지만 코딩 테스트로는 그런 문제들이 출제 된다.
# 동전 문제에선 동전들이 배수로 이뤄져 있기 때문에 그리디가 최적임이 보장된다. (정당성 검토)
# 여기서 시간 복잡도는 동전의 종류만큼 반복되기 때문에 동전의 종류 이다.

# 퀴즈
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세요
# 1번 N에서 1을 뺍니다. 2번 N이 K로 나누어 떨어질때 N을 K로 나눕니다.
# N(1 <= N <= 100,000) 과 K(2 <= K <= 100,000) 자연수

start_time = time.time()

N, K = map(int, input().split())
count = 0

while N != 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1

    if N == 1:
        break

end_time = time.time()

print(f"{end_time - start_time:.5f} sec")
sec = (end_time - start_time)
result = datetime.timedelta(seconds=sec)
print(result)
result_list = str(result).split('.')
print(result_list[0])

print(count)

# 2.91936 sec
# 0:00:02.919359
# 0:00:02

# N을 한번씩 확인하기 때문에 오래 걸림.

# 해설
start_time = time.time()

n, k = map(int, input().split())

result = 0

while True:
    # N 이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k       # n이 되야 하는 수
    result += (n - target)      # 1번의 수행 횟수
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1                 # 2번 수행시 1 더해주는 것. 밑에 두면 1이 되었을 때도 더해지기 때문에 위에 둔다.
    n //= k
end_time = time.time()

sec = (end_time - start_time)
result_time = datetime.timedelta(seconds=sec)
print(result_time)
result_list = str(result_time).split('.')
print(result_list[0])

result += (n - 1)               # n이 k보다 작은 경우로 1 이상의 수가 되어 1을 빼줘 맞춰줄 필요가 있다.
print(result)

# 0:00:01.567652
# 0:00:01

# 로그 시간 복잡도를 가져 더 빠르다! 나누기로 급격히 수가 줄기 때문!

# 퀴즈
# 각 자리가 숫자(0부터9) 로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x' 혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
# 단, +보다 X를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
# 예 02984 라는 문자열로 만들 수 있는 가장 큰 수는((((0+2) x 9) x8) x4 = 576입니다. 또 만들어질 수 있는
# 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

num = str(input())
max_num = 0

for n in num:
    n = int(n)
    if n == 0 or n == 1 or max_num == 0:
        max_num += n
    else:
        max_num *= n

print(max_num)

# 해설

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# 퀴즈
# 모험가 길드
# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한
# 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
# 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보가 주어졌을 때,
# 여행을 더날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
# 예를 들어 N = 5 각각의 공포도는 2 3 1 2 2
# 이 경우 그룹 1에 공포도가 1, 2, 3인 모험가를 한명씩 넣고, 그룹 2에 공포도가 2인 남은 두명을 넣게 되면 총
# 2개의 그룹을 만들 수 있다.
# 또 몇 명의 모험가는 마을에 그대로 남아 있어도 됨.
# 첫째 줄에 모험가의 수 N이 주어집니다. (1 <= N <= 100,000)
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.


n = int(input())
fear_li = map(int, input().split())

team_num = 0

for i in fear_li:
    if n > 0:
        if i == 1:
            n -= i
            team_num += 1
        else:
            n -= i
            team_num += 1
    else:
        break

print(team_num)

n = int(input())
fear_li = list(map(int, input().split()))
fear_li.sort()

team_num = 0
for i in fear_li:
    if n > i:
        n -= i
        team_num += 1
    else:
        break

print(team_num)


# 해설
# 오름차순 정렬 후 최소의 수로 그룹을 결성하자!
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0             # 총 그룹의 수
count = 0              # 혅재 그웁에 포함된 모험가의 수

for i in data:         # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1         # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:     # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1    # 총 그룹의 수 증가시키기
        count = 0      # 현재 그룹에 포함된 모험가의 수 초기화

print(result)

