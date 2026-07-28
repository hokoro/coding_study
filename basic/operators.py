"""
파이썬 기본 연산자 학습 자료

이 파일을 실행하면 각 연산의 결과를 직접 확인할 수 있습니다.

    python basic/operators.py

"""


def title(text):
    """실행 결과에서 단원을 구분하기 위한 함수입니다."""
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 산술 연산자 -----------------------------------------------------------
title("1. 산술 연산자")

a = 10
b = 3

print("a =", a, ", b =", b)
print("a + b =", a + b)    # 덧셈: 13
print("a - b =", a - b)    # 뺄셈: 7
print("a * b =", a * b)    # 곱셈: 30
print("a / b =", a / b)    # 나눗셈: 결과는 항상 실수(float)
print("a // b =", a // b)  # 몫(내림 나눗셈): 3 소수점 날림
print("a % b =", a % b)    # 나머지: 1
print("a ** b =", a ** b)  # 거듭제곱: 10의 3제곱 = 1000

# divmod(a, b)는 몫과 나머지를 한 번에 반환합니다.
quotient, remainder = divmod(a, b)
print("divmod(a, b) =", (quotient, remainder))

# 주의: //는 단순히 소수점만 버리는 것이 아니라 아래 방향으로 내림합니다.
print("-10 / 3 =", -10 / 3)
print("-10 // 3 =", -10 // 3)  # -3이 아니라 -4


# 2. 문자열에도 사용할 수 있는 산술 연산자 -------------------------------
title("2. 문자열 연산")

word = "Python"
print('"Hello, " + word =', "Hello, " + word)  # 문자열 연결
print('"Hi! " * 3 =', "Hi! " * 3)             # 문자열 반복


# 3. 비교 연산자 -----------------------------------------------------------
title("3. 비교 연산자")

x = 5
y = 8

print("x == y :", x == y)  # 같다
print("x != y :", x != y)  # 같지 않다
print("x > y  :", x > y)   # 크다
print("x < y  :", x < y)   # 작다
print("x >= 5 :", x >= 5)  # 크거나 같다
print("y <= 8 :", y <= 8)  # 작거나 같다

# 파이썬에서는 여러 비교를 자연스럽게 연결할 수 있습니다.
age = 20
print("10 <= age < 30 :", 10 <= age < 30)


# 4. 논리 연산자 -----------------------------------------------------------
title("4. 논리 연산자")

is_adult = True
has_ticket = False

print("is_adult and has_ticket :", is_adult and has_ticket)
print("is_adult or has_ticket  :", is_adult or has_ticket)
print("not is_adult            :", not is_adult)

# 논리 연산의 기본 우선순위: not > and > or
print("True or False and False :", True or False and False)
print("(True or False) and False :", (True or False) and False)

# 0, 빈 문자열, 빈 리스트, None 등은 조건식에서 False로 취급됩니다.
print("bool(0) =", bool(0))
print('bool("") =', bool(""))
print("bool([]) =", bool([]))
print("bool(1) =", bool(1))


# 5. 할당(대입) 연산자 -----------------------------------------------------
title("5. 할당 연산자")

number = 10
print("처음 number =", number)

number += 3   # number = number + 3
print("number += 3 ->", number)
number -= 2   # number = number - 2
print("number -= 2 ->", number)
number *= 4   # number = number * 4
print("number *= 4 ->", number)
number //= 5  # number = number // 5
print("number //= 5 ->", number)
number %= 3   # number = number % 3
print("number %= 3 ->", number)
number **= 3  # number = number ** 3
print("number **= 3 ->", number)


# 6. 멤버십 연산자 ---------------------------------------------------------
title("6. 멤버십 연산자")

fruits = ["apple", "banana", "orange"]

print('"banana" in fruits :', "banana" in fruits)
print('"grape" not in fruits :', "grape" not in fruits)
print('"th" in "Python" :', "th" in "Python")


# 7. 식별 연산자 -----------------------------------------------------------
title("7. 식별 연산자")

# ==는 두 값이 같은지, is는 두 변수가 동일한 객체를 가리키는지 확인합니다.
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("list_a == list_b :", list_a == list_b)  # 값은 같음
print("list_a is list_b :", list_a is list_b)  # 서로 다른 객체
print("list_a is list_c :", list_a is list_c)  # 동일한 객체

# None과 비교할 때는 == 대신 is를 사용하는 것이 권장됩니다.
result = None
print("result is None :", result is None)
print("result is not None :", result is not None)


# 8. 비트 연산자 -----------------------------------------------------------
title("8. 비트 연산자")

# 비트 연산은 정수를 2진수 비트 단위로 계산합니다.
# 10 = 0b1010, 6 = 0b0110
bit_a = 10
bit_b = 6

print("bit_a =", bit_a, "->", format(bit_a, "08b"))
print("bit_b =", bit_b, "->", format(bit_b, "08b"))

print("bit_a & bit_b =", bit_a & bit_b)  # AND: 둘 다 1인 비트만 1
print("                 ", format(bit_a & bit_b, "08b"))

print("bit_a | bit_b =", bit_a | bit_b)  # OR: 하나라도 1이면 1
print("                 ", format(bit_a | bit_b, "08b"))

print("bit_a ^ bit_b =", bit_a ^ bit_b)  # XOR: 서로 다른 비트만 1
print("                 ", format(bit_a ^ bit_b, "08b"))

print("~bit_a =", ~bit_a)  # NOT(비트 반전): 파이썬에서는 ~n == -(n + 1)
print("~bit_a == -(bit_a + 1) :", ~bit_a == -(bit_a + 1))

print("bit_a << 1 =", bit_a << 1)  # 왼쪽 이동: 보통 2를 곱한 효과
print("bit_a >> 1 =", bit_a >> 1)  # 오른쪽 이동: 보통 2로 나눈 몫의 효과

# 비트 연산 진리표
# p q | p & q | p | q | p ^ q
# 0 0 |   0   |   0   |   0
# 0 1 |   0   |   1   |   1
# 1 0 |   0   |   1   |   1
# 1 1 |   1   |   1   |   0


# 9. 논리 연산과 비트 연산의 차이 ----------------------------------------
title("9. 논리 연산과 비트 연산의 차이")

# and, or, not: 값 전체의 참/거짓을 판단하는 논리 연산
# &, |, ^, ~: 정수의 각 비트를 계산하는 비트 연산
print("True and False =", True and False)
print("10 & 6 =", 10 & 6)


# 10. 연산자 우선순위 ------------------------------------------------------
title("10. 연산자 우선순위")

# 자주 사용하는 연산자의 대략적인 우선순위(높음 -> 낮음)
# ** -> 단항 +, -, ~ -> *, /, //, % -> +, -
# -> <<, >> -> & -> ^ -> | -> 비교 연산 -> not -> and -> or
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# 가장 안전하고 읽기 쉬운 방법은 의도를 괄호로 명확히 표현하는 것입니다.


# 연습 문제 ---------------------------------------------------------------
title("연습 문제")

print(
    """
1. 다음 연산의 결과를 작성해주세요 2*3**2 = ?
"""
)
