"""파이썬 조건문과 코딩 테스트에서 자주 사용하는 분기 패턴."""


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. if, elif, else --------------------------------------------------------
title("1. 기본 조건문")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)

# 들여쓰기가 같은 코드가 하나의 블록이다.
number = 10
if number > 0:
    print("양수")
    print("0보다 큽니다.")


# 2. 비교 연산과 논리 연산 -------------------------------------------------
title("2. 비교와 논리 연산")

age = 20
has_ticket = True

print(age == 20)
print(age != 19)
print(age >= 19 and has_ticket)
print(age < 19 or not has_ticket)

if 10 <= age < 30:
    print("10대 또는 20대")


# 3. 참과 거짓으로 판단되는 값 --------------------------------------------
title("3. Truthy와 Falsy")

# False로 판단: False, 0, 0.0, "", [], (), {}, set(), None
values = [0, "", [], None, 1, "Python", [0]]

for value in values:
    if value:
        print(repr(value), "-> True")
    else:
        print(repr(value), "-> False")

# 리스트가 비어 있는지 확인할 때 len(data) > 0보다 if data가 간결하다.
data = [1, 2, 3]
if data:
    print("리스트에 값이 있습니다.")


# 4. in과 not in -----------------------------------------------------------
title("4. 포함 여부")

numbers = [1, 3, 5, 7]

if 3 in numbers:
    print("3이 있습니다.")

if 2 not in numbers:
    print("2가 없습니다.")

word = "algorithm"
if "go" in word:
    print("go가 포함되어 있습니다.")


# 5. 중첩 조건문 -----------------------------------------------------------
title("5. 중첩 조건문")

number = 12

if number > 0:
    if number % 2 == 0:
        print("양의 짝수")
    else:
        print("양의 홀수")
else:
    print("0 또는 음수")

# 논리 연산자로 한 번에 표현할 수도 있다.
if number > 0 and number % 2 == 0:
    print("양의 짝수")


# 6. 조건 표현식 -----------------------------------------------------------
title("6. 조건 표현식")

# 참일 때의 값 if 조건 else 거짓일 때의 값
number = 7
result = "짝수" if number % 2 == 0 else "홀수"
print(result)

a = 10
b = 20
larger = a if a > b else b
print(larger)


# 7. pass ------------------------------------------------------------------
title("7. pass")

# 문법상 코드가 필요하지만 아직 동작을 작성하지 않을 때 사용한다.
number = 0
if number == 0:
    pass
else:
    print(number)


# 8. match-case ------------------------------------------------------------
title("8. match-case")

command = "start"

match command:
    case "start":
        print("시작합니다.")
    case "stop":
        print("중지합니다.")
    case _:
        print("알 수 없는 명령")


# 9. 코딩 테스트 패턴 ------------------------------------------------------
title("9. 코딩 테스트 패턴")

# 최댓값 갱신
maximum = -float("inf")
numbers = [3, 8, 2, 10, 5]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)

# 범위를 벗어난 경우 건너뛰기에서 자주 사용하는 조건
row, column = 2, 3
height, width = 5, 5

if 0 <= row < height and 0 <= column < width:
    print("격자 내부")

# 여러 값 중 하나와 같은지 확인
operator = "+"
if operator in ("+", "-", "*", "/"):
    print("지원하는 연산자")


# 입력 예제
# number = int(input())
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

title("연습 문제")
print("연도 하나를 입력받아 윤년인지 판별하는 조건문을 작성해 보세요.")
