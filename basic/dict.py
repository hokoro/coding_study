"""
파이썬 딕셔너리(dict) 학습 자료

코딩 테스트에서 자주 사용하는 딕셔너리 함수와
collections.defaultdict 활용법을 실행 가능한 예제로 정리한 파일입니다.
"""

from collections import defaultdict


def title(text):
    """실행 결과에서 단원을 구분하기 위한 함수입니다."""
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 딕셔너리 생성 ---------------------------------------------------------
title("1. 딕셔너리 생성")

# 딕셔너리는 key와 value를 한 쌍으로 저장한다.
student = {
    "name": "Kim",
    "age": 20,
    "score": 95,
}

print(student)
print(type(student))

# dict()를 이용해서 만들 수도 있다.
point = dict(x=10, y=20)
print(point)

# 빈 딕셔너리
empty_dictionary = {}
print(empty_dictionary)

# key는 중복될 수 없다. 같은 key를 다시 저장하면 value가 변경된다.
data = {"a": 1, "a": 2}
print(data)  # {'a': 2}

# 리스트처럼 변경 가능한 자료형은 key로 사용할 수 없다.
# 튜플처럼 변경 불가능한 자료형은 key로 사용할 수 있다.
coordinates = {(0, 0): "시작점", (1, 2): "도착점"}
print(coordinates[(1, 2)])


# 2. 값 조회 ---------------------------------------------------------------
title("2. 값 조회")

student = {"name": "Kim", "score": 95}

# dictionary[key]로 value를 조회한다.
print(student["name"])

# 존재하지 않는 key를 []로 조회하면 KeyError가 발생한다.
# print(student["grade"])

# get(key)는 key가 없으면 None을 반환한다.
print(student.get("grade"))  # None

# get(key, 기본값)은 key가 없으면 지정한 기본값을 반환한다.
print(student.get("grade", "등급 없음"))

# key가 존재하는지 먼저 확인할 수도 있다.
print("score" in student)      # True
print("grade" not in student)  # True


# 3. 값 추가와 수정 --------------------------------------------------------
title("3. 값 추가와 수정")

student = {"name": "Kim"}

# 존재하지 않는 key에 값을 넣으면 추가된다.
student["score"] = 90
print(student)

# 이미 존재하는 key에 값을 넣으면 수정된다.
student["score"] = 100
print(student)

# update()로 하나 이상의 값을 추가하거나 수정한다.
student.update({"age": 20, "grade": "A"})
print(student)

# 키워드 인수 형태로도 사용할 수 있다.
student.update(score=95, city="Seoul")
print(student)


# 4. setdefault() ----------------------------------------------------------
title("4. setdefault()")

student = {"name": "Kim"}

# key가 없으면 기본값을 저장하고 그 값을 반환한다.
returned_value = student.setdefault("score", 0)
print(returned_value)  # 0
print(student)         # {'name': 'Kim', 'score': 0}

# key가 이미 있으면 기존 값을 유지하고 기존 값을 반환한다.
student.setdefault("score", 100)
print(student["score"])  # 0
student["score"] = student.setdefault("score", 0) + 1
print(student.get("score"))
# 같은 그룹의 값을 리스트에 모을 때 사용할 수 있다.
groups = {}
groups.setdefault("fruit", []).append("apple")
groups.setdefault("fruit", []).append("banana")
groups.setdefault("vegetable", []).append("carrot")
print(groups)


# 5. 값 삭제 ---------------------------------------------------------------
title("5. 값 삭제")

data = {"a": 1, "b": 2, "c": 3}

# del은 지정한 key와 value를 삭제한다.
del data["a"]
print(data)

# pop(key)는 값을 삭제하면서 반환한다.
removed_value = data.pop("b")
print("삭제한 값:", removed_value)
print(data)

# 없는 key를 pop하면 KeyError가 발생하므로 기본값을 지정할 수 있다.
print(data.pop("없는 키", None))  # None

# popitem()은 마지막에 추가된 key-value 쌍을 삭제하고 튜플로 반환한다.
key_value = data.popitem()
print("삭제한 항목:", key_value)
print(data)

# clear()는 모든 항목을 삭제한다.
data = {"a": 1, "b": 2}
data.clear()
print(data)  # {}


# 6. keys(), values(), items() ---------------------------------------------
title("6. keys(), values(), items()")

scores = {"Kim": 90, "Lee": 85, "Park": 100}

print(scores.keys())    # 모든 key
print(scores.values())  # 모든 value
print(scores.items())   # 모든 (key, value) 쌍

# 필요하다면 list로 변환한다.
print(list(scores.keys()))
print(list(scores.values()))
print(list(scores.items()))


# 7. 딕셔너리 순회 ---------------------------------------------------------
title("7. 딕셔너리 순회")

scores = {"Kim": 90, "Lee": 85, "Park": 100}

# 딕셔너리를 순회하면 기본적으로 key가 나온다.
for name in scores:
    print(name, scores[name])

# items()를 사용하면 key와 value를 동시에 받을 수 있다.
for name, score in scores.items():
    print(f"{name}: {score}")

# value만 필요하다면 values()를 사용한다.
total = 0
for score in scores.values():
    total += score

print("점수 합계:", total)


# 8. 딕셔너리 길이와 복사 --------------------------------------------------
title("8. 길이와 복사")

original = {"a": 1, "b": 2}

print("항목 개수:", len(original))

# 단순 대입은 같은 딕셔너리를 가리킨다.
same_dictionary = original
same_dictionary["a"] = 100
print(original)  # original도 변경된다.

# copy()는 얕은 복사본을 만든다.
copied_dictionary = original.copy()
copied_dictionary["b"] = 200

print("원본:", original)
print("복사본:", copied_dictionary)


# 9. 딕셔너리 컴프리헨션 ---------------------------------------------------
title("9. 딕셔너리 컴프리헨션")

# {key: value for 값 in 반복 가능한 객체}
squares = {number: number ** 2 for number in range(1, 6)}
print(squares)

# 조건을 추가할 수 있다.
even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}
print(even_squares)

# 두 리스트를 zip()으로 묶어 딕셔너리로 만들기
names = ["Kim", "Lee", "Park"]
scores = [90, 85, 100]
score_dictionary = dict(zip(names, scores))
print(score_dictionary)


# 10. 딕셔너리 정렬 --------------------------------------------------------
title("10. 딕셔너리 정렬")

scores = {"Kim": 90, "Lee": 85, "Park": 100}

# key를 기준으로 정렬한다.
sorted_by_key = sorted(scores.items())
print(sorted_by_key)

# value를 기준으로 오름차순 정렬한다.
sorted_by_value = sorted(scores.items(), key=lambda item: item[1])
print(sorted_by_value)

# value를 기준으로 내림차순 정렬한다.
sorted_by_value_descending = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True,
)
print(sorted_by_value_descending)

# sorted()의 결과는 (key, value) 튜플을 담은 리스트이다.
# 다시 딕셔너리로 만들고 싶다면 dict()를 사용한다.
sorted_dictionary = dict(sorted_by_value_descending)
print(sorted_dictionary)


# 11. defaultdict 기본 사용법 ---------------------------------------------
title("11. defaultdict 기본 사용법")

# defaultdict(기본값 생성 함수)
# 존재하지 않는 key를 조회하면 지정된 함수로 기본값을 자동 생성한다.

# int()의 기본값은 0이다.
count_dictionary = defaultdict(int)
count_dictionary["apple"] += 1
count_dictionary["apple"] += 1
count_dictionary["banana"] += 1

print(count_dictionary)
print(count_dictionary["orange"])  # 없는 key이므로 0을 생성하고 반환
print(dict(count_dictionary))       # 일반 dict 형태로 출력

# list()의 기본값은 빈 리스트 []이다.
group_dictionary = defaultdict(list)
group_dictionary["fruit"].append("apple")
group_dictionary["fruit"].append("banana")
group_dictionary["vegetable"].append("carrot")

print(dict(group_dictionary))

# set()의 기본값은 빈 집합 set()이다.
unique_group = defaultdict(set)
unique_group["fruit"].add("apple")
unique_group["fruit"].add("apple")
unique_group["fruit"].add("banana")

print(dict(unique_group))


# 12. defaultdict로 문자 개수 세기 ----------------------------------------
title("12. defaultdict로 빈도 계산")

word = "banana"
character_count = defaultdict(int)

for character in word:
    character_count[character] += 1

print(dict(character_count))  # {'b': 1, 'a': 3, 'n': 2}


# 13. defaultdict로 값 그룹화 ---------------------------------------------
title("13. defaultdict로 값 그룹화")

students = [
    ("A반", "Kim"),
    ("B반", "Lee"),
    ("A반", "Park"),
    ("B반", "Choi"),
]

classroom = defaultdict(list)

for class_name, student_name in students:
    classroom[class_name].append(student_name)

print(dict(classroom))
# {'A반': ['Kim', 'Park'], 'B반': ['Lee', 'Choi']}


# 14. defaultdict로 그래프 만들기 -----------------------------------------
title("14. defaultdict로 그래프 만들기")

# 인접 리스트 방식의 그래프를 만들 때 defaultdict(list)를 자주 사용한다.
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
]

graph = defaultdict(list)

for start, end in edges:
    graph[start].append(end)
    graph[end].append(start)  # 무방향 그래프이므로 반대 방향도 추가

print(dict(graph))


# 15. 중첩 defaultdict -----------------------------------------------------
title("15. 중첩 defaultdict")

# key가 두 단계 이상 필요한 경우 lambda로 내부 defaultdict를 만든다.
record = defaultdict(lambda: defaultdict(int))

record["Kim"]["math"] = 90
record["Kim"]["english"] = 85
record["Lee"]["math"] = 100

print(record["Kim"]["math"])
print(record["Park"]["math"])  # 존재하지 않아도 기본값 0

# 출력할 때 일반 딕셔너리 형태로 바꾸면 내용을 확인하기 쉽다.
normal_record = {
    name: dict(subjects)
    for name, subjects in record.items()
}
print(normal_record)


# 16. 일반 dict와 defaultdict 선택 기준 -----------------------------------
title("16. dict와 defaultdict 선택")

# 일반 dict + get()
word = "apple"
normal_count = {}

for character in word:
    normal_count[character] = normal_count.get(character, 0) + 1

print(normal_count)

# defaultdict
default_count = defaultdict(int)

for character in word:
    default_count[character] += 1

print(dict(default_count))

# key가 없을 때 조회만 해도 항목이 만들어지는 점은 주의해야 한다.
example = defaultdict(int)
print("조회 전:", dict(example))
print(example["new_key"])
print("조회 후:", dict(example))


# 17. 코딩 테스트 입력 예제 ------------------------------------------------
title("17. 코딩 테스트 입력 예제")

# 아래 예제들은 실제 입력이 필요하므로 연습할 때 주석을 해제하여 사용한다.

# 이름과 점수를 여러 줄 입력받아 딕셔너리에 저장하기
# n = int(input())
# scores = {}
#
# for _ in range(n):
#     name, score = input().split()
#     scores[name] = int(score)

# 숫자들의 등장 횟수 세기
# numbers = list(map(int, input().split()))
# number_count = defaultdict(int)
#
# for number in numbers:
#     number_count[number] += 1


# 연습 문제 ---------------------------------------------------------------
title("연습 문제")

print(
    """
1. 문자열 "mississippi"에 각 문자가 몇 번 등장하는지 구해 보세요.
2. 학생 이름과 점수를 딕셔너리에 저장하고 가장 높은 점수를 찾아보세요.
3. defaultdict(list)를 사용해 홀수와 짝수를 각각 그룹화해 보세요.
4. 주어진 간선 목록으로 무방향 그래프의 인접 리스트를 만들어 보세요.
5. 딕셔너리를 value 기준 내림차순으로 정렬해 보세요.
"""
)
