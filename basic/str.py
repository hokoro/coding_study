"""
파이썬 문자열(str) 학습 자료

문자열의 기본 사용법과 코딩 테스트에서 자주 사용하는 문자열 함수를
실행 가능한 예제로 정리한 파일입니다.
"""


def title(text):
    """실행 결과에서 단원을 구분하기 위한 함수입니다."""
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 문자열 생성과 기본 특징 ----------------------------------------------
title("1. 문자열 생성")

single_quote = 'Python'
double_quote = "Python"
multiline = """여러 줄의
문자열을 저장할 수 있습니다."""

print(single_quote)
print(double_quote)
print(multiline)

# 문자열의 길이는 len()으로 구한다.
text = "Python"
print("문자열 길이:", len(text))  # 6

# 문자열은 변경할 수 없는 자료형(immutable)이다.
# text[0] = "J"  # TypeError 발생
# 필요한 경우 새로운 문자열을 만들어야 한다.
changed_text = "J" + text[1:]
print(changed_text)  # Jython


# 2. 인덱싱과 슬라이싱 -----------------------------------------------------
title("2. 인덱싱과 슬라이싱")

text = "Python"

# 인덱스는 0부터 시작한다.
print(text[0])   # P
print(text[2])   # t
print(text[-1])  # n: 뒤에서 첫 번째 문자
print(text[-2])  # o: 뒤에서 두 번째 문자

# 문자열[시작:끝]: 시작 인덱스부터 끝 인덱스 직전까지 가져온다.
print(text[0:2])  # Py
print(text[:3])   # Pyt
print(text[2:])   # thon
print(text[:])    # Python

# 문자열[시작:끝:간격]
print(text[::2])   # Pto: 두 칸씩 이동
print(text[::-1])  # nohtyP: 문자열 뒤집기


# 3. 문자열 연결과 반복 ----------------------------------------------------
title("3. 문자열 연결과 반복")

first = "Hello"
second = "Python"

print(first + " " + second)  # 문자열 연결
print("Hi! " * 3)            # 문자열 반복

# 문자열과 정수는 바로 더할 수 없으므로 정수를 str로 변환한다.
score = 100
print("점수: " + str(score))
print(f"점수: {score}")  # f-string을 사용하면 더 편리하다.


# 4. 대소문자 변환 ---------------------------------------------------------
title("4. 대소문자 변환")

text = "hello PYTHON"

print(text.upper())       # 모든 문자를 대문자로
print(text.lower())       # 모든 문자를 소문자로
print(text.capitalize())  # 첫 문자만 대문자로
print(text.title())       # 각 단어의 첫 문자를 대문자로
print(text.swapcase())    # 대문자와 소문자를 서로 변경


# 5. 문자열 검색 -----------------------------------------------------------
title("5. 문자열 검색")

text = "banana"

# count(): 특정 문자열이 등장하는 횟수
print('text.count("a") =', text.count("a"))  # 3

# find(): 처음 등장하는 위치, 찾지 못하면 -1
print('text.find("na") =', text.find("na"))  # 2
print('text.find("z") =', text.find("z"))    # -1

# rfind(): 오른쪽부터 검색하여 처음 발견한 위치
print('text.rfind("na") =', text.rfind("na"))  # 4

# index(): 처음 등장하는 위치
# 찾지 못하면 -1 대신 ValueError가 발생하므로 주의한다.
print('text.index("na") =', text.index("na"))  # 2

# in, not in은 문자열이 포함되어 있는지 확인한다.
print('"nan" in text =', "nan" in text)          # True
print('"apple" not in text =', "apple" not in text)  # True

# startswith(), endswith(): 시작하거나 끝나는 문자열 확인
filename = "solution.py"
print(filename.startswith("sol"))  # True
print(filename.endswith(".py"))    # True


# 6. 공백과 특정 문자 제거 -------------------------------------------------
title("6. 공백과 특정 문자 제거")

text = "   Python   "

print(f"|{text.strip()}|")   # 양쪽 공백 제거
print(f"|{text.lstrip()}|")  # 왼쪽 공백 제거
print(f"|{text.rstrip()}|")  # 오른쪽 공백 제거

# strip("문자들")은 양 끝에서 지정한 문자들을 제거한다.
# 가운데에 있는 문자는 제거하지 않는다.
data = "###Python###"
print(data.strip("#"))  # Python


# 7. 문자열 치환 -----------------------------------------------------------
title("7. 문자열 치환")

text = "I like Java"

# replace(기존 문자열, 새로운 문자열)
replaced = text.replace("Java", "Python")
print(replaced)  # I like Python

# 세 번째 인수로 치환 횟수를 제한할 수 있다.
text = "one one one"
print(text.replace("one", "two", 2))  # two two one

# 문자열은 변경 불가능하므로 replace()는 새로운 문자열을 반환한다.
print(text)  # one one one


# 8. 문자열 분리 -----------------------------------------------------------
title("8. 문자열 분리")

text = "10 20 30"

# split(): 공백을 기준으로 문자열을 나누어 리스트로 반환한다.
print(text.split())  # ['10', '20', '30']

# 원하는 구분 문자를 지정할 수 있다.
date = "2026-07-28"
print(date.split("-"))  # ['2026', '07', '28']

# split()에 인수를 넣지 않으면 연속된 공백을 하나의 구분자로 처리한다.
many_spaces = "10   20  30"
print(many_spaces.split())  # ['10', '20', '30']

# split(" ")처럼 구분자를 직접 지정하면 연속된 구분자 사이에 빈 문자열이 생긴다.
print(many_spaces.split(" "))

# splitlines(): 여러 줄 문자열을 줄 단위로 분리한다.
lines = "apple\nbanana\norange"
print(lines.splitlines())  # ['apple', 'banana', 'orange']


# 9. 문자열 결합 -----------------------------------------------------------
title("9. 문자열 결합")

words = ["Python", "is", "easy"]

# "구분자".join(문자열 목록)
print(" ".join(words))   # Python is easy
print("-".join(words))   # Python-is-easy
print("".join(words))    # Pythoniseasy

# join()은 문자열만 결합할 수 있다.
# 정수 리스트는 각 원소를 str로 변환한 후 결합한다.
numbers = [1, 2, 3, 4]
print(" ".join(map(str, numbers)))  # 1 2 3 4


# 10. 문자열 판별 함수 -----------------------------------------------------
title("10. 문자열 판별 함수")

# 판별 함수는 결과로 True 또는 False를 반환한다.
print('"123".isdigit() =', "123".isdigit())       # 숫자로 구성
print('"abc".isalpha() =', "abc".isalpha())       # 문자로 구성
print('"abc123".isalnum() =', "abc123".isalnum()) # 문자 또는 숫자로 구성
print('"   ".isspace() =', "   ".isspace())       # 공백으로 구성
print('"ABC".isupper() =', "ABC".isupper())       # 모두 대문자
print('"abc".islower() =', "abc".islower())       # 모두 소문자

# 음수 부호와 소수점은 숫자가 아니므로 isdigit() 결과가 False이다.
print('"-10".isdigit() =', "-10".isdigit())  # False
print('"3.14".isdigit() =', "3.14".isdigit()) # False


# 11. 문자와 아스키/유니코드 값 변환 --------------------------------------
title("11. ord()와 chr()")

# ord(문자): 문자를 코드 값으로 변환
print("ord('A') =", ord("A"))  # 65
print("ord('a') =", ord("a"))  # 97

# chr(정수): 코드 값을 문자로 변환
print("chr(65) =", chr(65))    # A
print("chr(97) =", chr(97))    # a

# 알파벳 순서를 구하는 코딩 테스트 예제
alphabet_index = ord("C") - ord("A")
print("C는 0부터 시작하면", alphabet_index, "번째")  # 2번째


# 12. 문자열 정렬과 뒤집기 -------------------------------------------------
title("12. 문자열 정렬과 뒤집기")

text = "dcba"

# sorted()는 정렬된 문자 리스트를 반환한다.
sorted_characters = sorted(text)
print(sorted_characters)  # ['a', 'b', 'c', 'd']

# 문자열로 만들려면 join()을 사용한다.
ascending = "".join(sorted(text))
descending = "".join(sorted(text, reverse=True))

print(ascending)   # abcd
print(descending)  # dcba
print(text[::-1])  # abcd: 슬라이싱으로 뒤집기


# 13. 코딩 테스트 활용 예제 ------------------------------------------------
title("13. 코딩 테스트 활용 예제")

# 회문(palindrome): 앞에서 읽어도 뒤에서 읽어도 같은 문자열
word = "level"
is_palindrome = word == word[::-1]
print(word, "회문 여부:", is_palindrome)

# 문자열에서 숫자만 골라 합하기
data = "a1b2c3"
digit_sum = sum(int(character) for character in data if character.isdigit())
print("숫자의 합:", digit_sum)  # 6

# 각 문자의 등장 횟수 세기
word = "banana"
character_count = {}

for character in word:
    character_count[character] = character_count.get(character, 0) + 1

print(character_count)  # {'b': 1, 'a': 3, 'n': 2}

# 대소문자를 구분하지 않고 비교하기
left = "Python"
right = "PYTHON"
print(left.lower() == right.lower())  # True


# 14. 코딩 테스트 입력 예제 ------------------------------------------------
title("14. 코딩 테스트 문자열 입력")

# 아래 예제들은 실제 입력이 필요하므로 연습할 때 주석을 해제하여 사용한다.

# 공백 없는 문자열 한 줄 입력
# word = input().strip()

# 공백으로 구분된 문자열 여러 개 입력
# words = input().split()

# 문자열을 한 글자씩 리스트에 저장
# characters = list(input().strip())

# 공백 없이 붙어 있는 숫자를 한 자리씩 정수 리스트로 저장
# digits = list(map(int, input().strip()))

# 여러 줄의 문자열을 2차원 리스트로 입력
# n = int(input())
# board = [list(input().strip()) for _ in range(n)]


# 연습 문제 ---------------------------------------------------------------
title("연습 문제")

print(
    """
1. 문자열 "algorithm"을 거꾸로 출력해 보세요.
2. 문자열 "banana"에 문자 "a"가 몇 번 등장하는지 구해 보세요.
3. 입력받은 문자열이 회문인지 확인해 보세요.
4. "2026/07/28"을 "/" 기준으로 나누어 리스트로 만들어 보세요.
5. 문자열에서 알파벳은 제외하고 숫자만 골라 합을 구해 보세요.
"""
)
# 1
text = "algorithm"
print(text[::-1])
#2
banana="banana"
print(banana.count("a"))
#3
# a = input("입력:")
# print(a == a[::-1])
#4
b = "2026/07/28"
print(b.split("/"))

#5
c = "a1b2c3"
d = 0
for j in c : 
    if j.isdigit():
        d += int(j)

print(d)