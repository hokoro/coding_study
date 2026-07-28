"""코딩 테스트에서 자주 사용하는 정렬 방법과 key 함수."""


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. sort()와 sorted() -----------------------------------------------------
title("1. sort()와 sorted()")

numbers = [4, 2, 5, 1, 3]

# list.sort()는 원본 리스트를 변경하고 None을 반환한다.
returned = numbers.sort()
print(numbers)
print(returned)  # None

# sorted()는 정렬된 새 리스트를 반환하며 원본을 변경하지 않는다.
original = [4, 2, 5, 1, 3]
sorted_numbers = sorted(original)
print("원본:", original)
print("결과:", sorted_numbers)

# 문자열, 튜플, 집합 등에도 sorted()를 사용할 수 있으며 결과는 리스트이다.
print(sorted("python"))
print(sorted((3, 1, 2)))
print(sorted({3, 1, 2}))


# 2. 내림차순 --------------------------------------------------------------
title("2. 내림차순")

numbers = [4, 2, 5, 1, 3]
print(sorted(numbers, reverse=True))

numbers.sort(reverse=True)
print(numbers)


# 3. 문자열 정렬 -----------------------------------------------------------
title("3. 문자열 정렬")

words = ["banana", "apple", "Cherry", "kiwi"]

# 기본 정렬은 유니코드 값을 기준으로 비교하므로 대문자가 먼저 올 수 있다.
print(sorted(words))

# 대소문자를 무시하고 정렬한다.
print(sorted(words, key=str.lower))

# 문자열 길이를 기준으로 정렬한다.
print(sorted(words, key=len))

# 길이가 같으면 문자열 오름차순으로 정렬한다.
print(sorted(words, key=lambda word: (len(word), word.lower())))


# 4. 튜플과 리스트 정렬 ----------------------------------------------------
title("4. 여러 기준 정렬")

# 별도의 key가 없으면 첫 번째 값, 두 번째 값 순서로 비교한다.
points = [(2, 3), (1, 5), (1, 2), (2, 1)]
print(sorted(points))

# x는 오름차순, y는 내림차순
print(sorted(points, key=lambda point: (point[0], -point[1])))

students = [
    ["Kim", 90, 20],
    ["Lee", 90, 19],
    ["Park", 100, 21],
    ["Choi", 80, 19],
]

# 점수 내림차순, 나이 오름차순, 이름 오름차순
students_sorted = sorted(
    students,
    key=lambda student: (-student[1], student[2], student[0]),
)

for student in students_sorted:
    print(student)


# 5. 딕셔너리 정렬 ---------------------------------------------------------
title("5. 딕셔너리 정렬")

scores = {"Kim": 90, "Lee": 80, "Park": 100}

print(sorted(scores))  # key만 정렬
print(sorted(scores.items()))  # key 기준
print(sorted(scores.items(), key=lambda item: item[1]))  # value 기준
print(sorted(scores.items(), key=lambda item: item[1], reverse=True))


# 6. key 함수 --------------------------------------------------------------
title("6. key 함수")

# key에는 각 원소를 받아서 "정렬할 기준값"을 반환하는 함수를 전달한다.
# sorted()는 원소 자체가 아니라 key 함수가 반환한 값을 서로 비교한다.
#
#              key 함수
# 원소 --------> 비교 기준값
# "apple" -----> 5
# "kiwi"  -----> 4
#
# 따라서 sorted(words, key=len)은 단어가 아니라 단어 길이를 비교한다.

numbers = [-10, 3, -2, 5, 1]

# 절댓값을 기준으로 정렬
print(sorted(numbers, key=abs))

# 나머지를 기준으로 정렬하고 같으면 원래 숫자를 기준으로 정렬
print(sorted(numbers, key=lambda number: (number % 3, number)))


# 7. lambda 함수 -----------------------------------------------------------
title("7. lambda 함수")

# lambda 매개변수: 반환할 식
# 이름 없이 짧게 만드는 함수이며 정렬 기준을 작성할 때 자주 사용한다.
#
# 아래 두 함수는 같은 역할을 한다.
def get_second(item):
    return item[1]


get_second_lambda = lambda item: item[1]

sample = ("Kim", 90)
print(get_second(sample))
print(get_second_lambda(sample))

records = [("Kim", 90), ("Lee", 80), ("Park", 100)]

# 각 튜플의 두 번째 값인 점수를 기준으로 정렬한다.
print(sorted(records, key=lambda item: item[1]))

# lambda의 item에는 records의 원소가 하나씩 들어온다.
# item = ("Kim", 90) -> item[1] = 90
# item = ("Lee", 80) -> item[1] = 80
# item = ("Park", 100) -> item[1] = 100


# 8. 다중 정렬 기준 --------------------------------------------------------
title("8. 다중 정렬 기준")

records = [
    ("Kim", 90, 20),
    ("Lee", 90, 19),
    ("Park", 100, 21),
    ("Choi", 90, 19),
]

# key가 튜플이면 첫 번째 기준이 같을 때 두 번째, 세 번째 기준을 비교한다.
# 점수 오름차순 -> 나이 오름차순 -> 이름 오름차순
print(sorted(records, key=lambda item: (item[1], item[2], item[0])))

# 숫자에 -를 붙이면 해당 숫자 기준만 내림차순으로 만들 수 있다.
# 점수 내림차순 -> 나이 오름차순 -> 이름 오름차순
mixed_order = sorted(
    records,
    key=lambda item: (-item[1], item[2], item[0]),
)
print(mixed_order)

# reverse=True는 모든 기준의 방향을 한꺼번에 반대로 바꾼다.
# 기준별로 방향이 다르면 key 튜플에서 숫자에 -를 붙이는 방법을 사용한다.


# 9. 안정 정렬 -------------------------------------------------------------
title("9. 안정 정렬")

# 파이썬 정렬은 key 값이 같으면 기존 순서를 유지하는 안정 정렬이다.
records = [
    ("Kim", "A"),
    ("Lee", "B"),
    ("Park", "A"),
    ("Choi", "B"),
]

print(sorted(records, key=lambda record: record[1]))


# 10. 역순과 내림차순의 차이 -----------------------------------------------
title("10. reverse()와 내림차순")

numbers = [3, 1, 4, 2]

reversed_order = numbers[::-1]            # 현재 순서만 반대로
descending = sorted(numbers, reverse=True)  # 값 기준 내림차순

print(reversed_order)  # [2, 4, 1, 3]
print(descending)      # [4, 3, 2, 1]


# 11. 최솟값과 최댓값 일부만 필요할 때 --------------------------------------
title("11. 일부 값 선택")

numbers = [7, 2, 9, 1, 5]
print(sorted(numbers)[:3])   # 가장 작은 값 3개
print(sorted(numbers)[-3:])  # 가장 큰 값 3개

# 데이터가 매우 많고 일부만 필요하다면 heapq의 nsmallest, nlargest도 사용한다.
from heapq import nlargest, nsmallest

print(nsmallest(3, numbers))
print(nlargest(3, numbers))


# 12. 코딩 테스트 입력 예제 ------------------------------------------------
title("12. 코딩 테스트 입력")

# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# numbers.sort()
# print(*numbers, sep="\n")

# n = int(input())
# records = [tuple(map(int, input().split())) for _ in range(n)]
# records.sort(key=lambda item: (item[0], item[1]))

title("연습 문제")
print("학생 정보를 점수 내림차순, 점수가 같으면 이름 오름차순으로 정렬해 보세요.")
