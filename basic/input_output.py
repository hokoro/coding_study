# 기본 입력 = input()
# input()은 일반적인 입력

n_str = input() # 문자열 입력
n_int = int(input()) # 문자열 하나를 입력 받아서 int 형으로
n_float = float(input()) # 문자열 하나를 입력 받아서 float 형으로

print(n_str)
print(n_int)
print(n_float)

# int와 float은 반드시 숫자 문자열 0 ~ 9로 만들 수 있는 숫자여야한다.

# 코딩 테스트용 input을 sys 라이브러리 써서 입력 받는다
# sys를 쓰는 이유 : 입력을 많이 받을 경우
# ex) BFS,DFS 문제를 풀 때 수만 ~ 수십만개 정점(node)와 간선(edge)를 받는게 기본이다 입력이 많을 경우 sys.stdin을 사용해서 입력을 받는다.

import sys
n_sys =  sys.stdin.readline().strip() # sys.stdin.readline() 한줄 짜리 입력 strip() = \n 탭 공백 제거를 반드시 해야한다 입력 받을떄 \n이 포함이 됨


# 여러번의 값 한번에 입력 받기 (map, split)
# 입력 받은 수가 많아질 경우 입력 받는 방법이다.
# map: 입력 받은 데이터를 하나의 자료형으로 변경하기 위한 방법이다 map("자료형" , "입력값")
# split() : 입력 받은 데이터를 기준 텍스트

a,b,c = map(int , sys.stdin.readline().strip().split())

print(f'{a},{b},{c}')


# 문자열 여러 개 입력 받기
# 공백을 기준으로 나눈 문자열을 각각의 변수에 저장한다.
first_name, last_name = input().split()

print(first_name)
print(last_name)


# 정수 여러 개 입력 받기
# split()으로 나눈 문자열을 map()을 이용해 모두 int 형으로 변환한다.
x, y = map(int, input().split())

print(x + y)


# 입력 받은 정수들을 리스트로 만들기
# 입력되는 정수의 개수가 정해져 있지 않을 때 자주 사용하는 방법이다.
numbers = list(map(int, input().split()))

print(numbers)


# 원하는 문자를 기준으로 입력 나누기
# split(",")은 쉼표를 기준으로 문자열을 나눈다.
# 입력 예시: apple,banana,orange
fruits = input().split(",")

print(fruits)


# print()의 sep와 end
# sep: 출력할 값 사이에 넣을 문자를 설정한다.
print(2026, 7, 28, sep="-")  # 2026-7-28

# end: 출력 마지막에 넣을 문자를 설정한다.
# 기본값은 줄바꿈 문자(\n)이다.
print("Hello", end=" ")
print("Python")  # Hello Python


# f-string을 이용한 출력 형식 지정
name = "Python"
score = 95

print(f"{name} 점수: {score}")

# 실수의 소수점 자릿수 지정
pi = 3.141592
print(f"{pi:.2f}")  # 소수점 둘째 자리까지 출력: 3.14
print(f"{pi:.4f}")  # 소수점 넷째 자리까지 출력: 3.1416

# 큰 정수에 천 단위 구분 기호 넣기
money = 1234567
print(f"{money:,}")  # 1,234,567


# 빠른 출력
# 출력해야 하는 데이터가 많을 때 sys.stdout.write()를 사용할 수 있다.
# sys.stdout.write()는 print()와 달리 자동으로 줄바꿈하지 않는다.
sys.stdout.write("빠른 출력\n")

# 여러 결과를 한 번에 출력하는 방법
result = [1, 2, 3, 4, 5]
sys.stdout.write(" ".join(map(str, result)) + "\n")
