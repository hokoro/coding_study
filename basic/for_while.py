"""for, while 반복문과 코딩 테스트에서 자주 사용하는 반복 패턴."""


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. for 기본 --------------------------------------------------------------
title("1. for 반복문")

for number in [1, 2, 3]:
    print(number)

for character in "Python":
    print(character, end=" ")
print()


# 2. range() ---------------------------------------------------------------
title("2. range()")

print(list(range(5)))         # 0, 1, 2, 3, 4
print(list(range(2, 6)))      # 2, 3, 4, 5
print(list(range(1, 10, 2)))  # 1부터 2씩 증가
print(list(range(5, 0, -1)))  # 5부터 1씩 감소

for index in range(3):
    print(index)


# 3. enumerate() -----------------------------------------------------------
title("3. enumerate()")

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# 4. zip() -----------------------------------------------------------------
title("4. zip()")

names = ["Kim", "Lee", "Park"]
scores = [90, 80, 100]

for name, score in zip(names, scores):
    print(name, score)


# 5. 딕셔너리 순회 ---------------------------------------------------------
title("5. 딕셔너리 순회")

scores = {"Kim": 90, "Lee": 80}

for name in scores:
    print(name, scores[name])

for name, score in scores.items():
    print(name, score)


# 6. 중첩 반복문 -----------------------------------------------------------
title("6. 중첩 반복문")

for row in range(2):
    for column in range(3):
        print((row, column), end=" ")
    print()

matrix = [[1, 2, 3], [4, 5, 6]]
total = 0

for row in matrix:
    for value in row:
        total += value

print("합계:", total)


# 7. while -----------------------------------------------------------------
title("7. while 반복문")

count = 3

while count > 0:
    print(count)
    count -= 1  # 조건이 언젠가 False가 되도록 값을 변경해야 한다.

print("종료")


# 8. break와 continue ------------------------------------------------------
title("8. break와 continue")

for number in range(1, 11):
    if number == 5:
        break
    print(number, end=" ")
print()

for number in range(1, 11):
    if number % 2 == 1:
        continue
    print(number, end=" ")
print()


# 9. 반복문의 else ---------------------------------------------------------
title("9. 반복문의 else")

# 반복문이 break 없이 정상 종료되면 else가 실행된다.
target = 7
numbers = [1, 3, 5]

for number in numbers:
    if number == target:
        print("찾음")
        break
else:
    print("찾지 못함")


# 10. 누적 계산 ------------------------------------------------------------
title("10. 누적 계산")

numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print(total)

maximum = numbers[0]
for number in numbers[1:]:
    if number > maximum:
        maximum = number

print(maximum)


# 11. 리스트 컴프리헨션 ----------------------------------------------------
title("11. 리스트 컴프리헨션")

squares = [number ** 2 for number in range(1, 6)]
evens = [number for number in range(1, 11) if number % 2 == 0]
matrix = [[row * 3 + column for column in range(3)] for row in range(2)]

print(squares)
print(evens)
print(matrix)


# 12. 코딩 테스트 입력 반복 ------------------------------------------------
title("12. 입력 반복")

# n = int(input())
# numbers = [int(input()) for _ in range(n)]

# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# 테스트 케이스가 여러 개인 경우
# test_case = int(input())
# for _ in range(test_case):
#     a, b = map(int, input().split())
#     print(a + b)

title("연습 문제")
print("1부터 100까지의 숫자 중 3의 배수 합계를 반복문으로 구해 보세요.")
