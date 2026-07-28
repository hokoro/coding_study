"""
파이썬 자료형 변환 학습 자료

코딩 테스트에서 자주 사용하는 입력과 자료형 변환 방법을 정리한 파일입니다.
"""


def title(text):
    """실행 결과에서 단원을 구분하기 위한 함수입니다."""
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 기본 자료형 변환 ------------------------------------------------------
title("1. 기본 자료형 변환")

# type()을 사용하면 값의 자료형을 확인할 수 있다.
integer_number = int("10")       # 문자열 -> 정수
float_number = float("3.14")     # 문자열 -> 실수
number_text = str(100)           # 정수 -> 문자열
boolean_value = bool(1)          # 숫자 -> 논리형
character_list = list("Python")  # 문자열 -> 리스트
number_tuple = tuple([1, 2, 3])  # 리스트 -> 튜플
number_set = set([1, 1, 2])      # 리스트 -> 집합

print(integer_number, type(integer_number))
print(float_number, type(float_number))
print(number_text, type(number_text))
print(boolean_value, type(boolean_value))
print(character_list, type(character_list))
print(number_tuple, type(number_tuple))
print(number_set, type(number_set))

# set은 중복된 값을 제거한다.
print("set([1, 1, 2]) =", number_set)


# 2. 문자열을 리스트로 변환 -----------------------------------------------
title("2. 문자열을 리스트로 변환")

# 문자열에 list()를 사용하면 한 글자씩 나뉘어 리스트에 저장된다.
characters = list("123")
print(characters)  # ['1', '2', '3']

# 문자열의 각 문자를 정수로 저장하려면 map()을 함께 사용한다.
digits = list(map(int, "123"))
print(digits)  # [1, 2, 3]

# 파이썬에서는 보통 배열이라고 표현하기도 하지만 정확한 자료형은 list이다.
print(type(digits))  # <class 'list'>


# 3. list()와 split()의 차이 ----------------------------------------------
title("3. list()와 split()의 차이")

text = "10 20 30"

# list(문자열): 공백을 포함하여 모든 문자를 한 글자씩 나눈다.
print(list(text))
# ['1', '0', ' ', '2', '0', ' ', '3', '0']

# split(): 공백을 기준으로 문자열을 나눈다.
print(text.split())
# ['10', '20', '30']

# split() 결과의 각 문자열을 int로 변환하여 정수 리스트를 만든다.
numbers = list(map(int, text.split()))
print(numbers)
# [10, 20, 30]


# 4. 정수 리스트를 문자열로 변환 -----------------------------------------
title("4. 정수 리스트를 문자열로 변환")

numbers = [1, 2, 3]

# join()은 문자열만 연결할 수 있으므로 각 정수를 str로 변환해야 한다.
joined_text = "".join(map(str, numbers))
print(joined_text)  # 123

# 구분 문자를 넣어 연결할 수도 있다.
spaced_text = " ".join(map(str, numbers))
print(spaced_text)  # 1 2 3


# 5. 참과 거짓으로 변환 ----------------------------------------------------
title("5. bool 변환")

# 0, 빈 문자열, 빈 리스트, 빈 튜플, 빈 집합, None은 False가 된다.
print("bool(0) =", bool(0))
print('bool("") =', bool(""))
print("bool([]) =", bool([]))
print("bool(None) =", bool(None))

# 0이 아닌 숫자와 값이 들어 있는 자료형은 True가 된다.
print("bool(10) =", bool(10))
print('bool("False") =', bool("False"))  # 문자열에 값이 있으므로 True
print("bool([0]) =", bool([0]))          # 리스트가 비어 있지 않으므로 True


# 6. 진법 변환 -------------------------------------------------------------
title("6. 진법 변환")

# int(문자열, 진법)을 사용하면 다른 진법의 문자열을 10진수로 변환할 수 있다.
binary_to_decimal = int("1010", 2)
octal_to_decimal = int("12", 8)
hex_to_decimal = int("A", 16)

print(binary_to_decimal)  # 10
print(octal_to_decimal)   # 10
print(hex_to_decimal)     # 10

# 10진수를 2진수, 8진수, 16진수 문자열로 변환한다.
print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(10))  # 0xa

# 접두사 없이 숫자 부분만 출력하려면 format()을 사용할 수 있다.
print(format(10, "b"))  # 1010
print(format(10, "o"))  # 12
print(format(10, "x"))  # a


# 7. 형변환 시 주의할 점 --------------------------------------------------
title("7. 형변환 시 주의할 점")

# int()는 정수 형태의 문자열을 변환할 수 있다.
print(int("-10"))
print(int("+20"))

# float()는 소수와 지수 형태의 문자열도 변환할 수 있다.
print(float("-3.14"))
print(float("1e3"))  # 1000.0

# int("3.14")처럼 정수 형태가 아닌 문자열은 바로 int로 변환할 수 없다.
# 필요한 경우 먼저 float로 변환한 뒤 int로 변환한다.
print(int(float("3.14")))  # 3

# float를 int로 변환하면 소수점 아래를 버린다. 반올림이 아니다.
print(int(3.9))   # 3
print(int(-3.9))  # -3


# 8. 코딩 테스트에서 자주 사용하는 입력 + 형변환 -------------------------
title("8. 코딩 테스트 입력 + 형변환")

# 아래 예제들은 실제 입력이 필요하므로 연습할 때 주석을 해제하여 사용한다.

# 공백으로 구분된 정수들을 리스트로 입력 받기
# 입력 예시: 10 20 30
# numbers = list(map(int, input().split()))
# print(numbers)  # [10, 20, 30]

# 정수 여러 개를 각각의 변수로 입력 받기
# 입력 예시: 10 20
# a, b = map(int, input().split())
# print(a, b)

# 공백 없이 붙어 있는 숫자를 한 자리씩 정수 리스트로 입력 받기
# 입력 예시: 12345
# digits = list(map(int, input()))
# print(digits)  # [1, 2, 3, 4, 5]

# 2차원 정수 리스트 입력 받기
# 첫 줄에 행의 개수 n을 입력하고, 다음 n줄에 정수들을 입력한다.
# 입력 예시:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)

# 핵심 입력 패턴
# 숫자 여러 개가 공백으로 구분되어 있다면 아래 형태를 가장 많이 사용한다.
# numbers = list(map(int, input().split()))
