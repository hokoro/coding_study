"""변경할 수 없는 순서형 자료구조인 튜플(tuple) 학습 자료."""


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 생성 ------------------------------------------------------------------
title("1. 튜플 생성")

point = (10, 20)
empty = ()
one_value = (10,)  # 값이 하나인 튜플은 반드시 쉼표가 필요하다.
not_tuple = (10)

print(point, type(point))
print(empty)
print(one_value, type(one_value))
print(not_tuple, type(not_tuple))

# 괄호 없이도 튜플을 만들 수 있다.
coordinate = 3, 5
print(coordinate, type(coordinate))


# 2. 인덱싱과 슬라이싱 -----------------------------------------------------
title("2. 인덱싱과 슬라이싱")

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[-1])
print(numbers[1:3])
print(numbers[::-1])
print(len(numbers))


# 3. 튜플의 불변성 ---------------------------------------------------------
title("3. 튜플의 불변성")

# 튜플은 생성한 후 원소를 추가, 삭제, 수정할 수 없다.
# numbers[0] = 100  # TypeError 발생

# 변경이 필요하면 리스트로 변환한 뒤 다시 튜플로 바꿀 수 있다.
temporary = list(numbers)
temporary[0] = 100
numbers = tuple(temporary)
print(numbers)

# 튜플 자체는 불변이지만 내부에 있는 리스트의 내용은 변경할 수 있다.
mixed = ([1, 2], 3)
mixed[0].append(4)
print(mixed)


# 4. 연산과 함수 -----------------------------------------------------------
title("4. 튜플 연산과 함수")

left = (1, 2)
right = (3, 4)
data = (1, 2, 2, 3)

print(left + right)
print(left * 3)
print(2 in data)
print(data.count(2))
print(data.index(3))
print(min(data), max(data), sum(data))


# 5. 패킹과 언패킹 ---------------------------------------------------------
title("5. 패킹과 언패킹")

packed = 10, 20, 30
a, b, c = packed
print(a, b, c)

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)  # 별표로 받은 값은 리스트가 된다.

# 임시 변수 없이 두 값을 교환할 수 있다.
x = 10
y = 20
x, y = y, x
print(x, y)


# 6. 함수 반환값과 튜플 -----------------------------------------------------
title("6. 함수 반환값")


def calculate(a, b):
    return a + b, a * b


result = calculate(3, 4)
total, product = calculate(3, 4)

print(result, type(result))
print(total, product)

# divmod()도 몫과 나머지를 튜플로 반환한다.
quotient, remainder = divmod(17, 5)
print(quotient, remainder)


# 7. 튜플을 key로 사용 -----------------------------------------------------
title("7. 딕셔너리와 집합에서 활용")

# 변경 불가능한 튜플은 딕셔너리의 key와 집합의 원소로 사용할 수 있다.
board = {
    (0, 0): "start",
    (2, 3): "end",
}
visited = {(0, 0), (0, 1), (1, 1)}

print(board[(2, 3)])
print((0, 1) in visited)


# 8. 정렬에서 활용 ---------------------------------------------------------
title("8. 정렬에서 활용")

# 튜플은 앞 원소부터 차례대로 비교된다.
records = [(2, "Kim"), (1, "Park"), (1, "Lee")]
print(sorted(records))

# 두 번째 값을 우선하여 정렬하기
print(sorted(records, key=lambda item: item[1]))


# 9. enumerate()와 zip() ---------------------------------------------------
title("9. enumerate()와 zip()")

fruits = ["apple", "banana"]

# enumerate()와 zip()에서 얻는 각 항목도 튜플 형태이다.
print(list(enumerate(fruits)))
print(list(zip(["Kim", "Lee"], [90, 100])))

for index, fruit in enumerate(fruits):
    print(index, fruit)


# 코딩 테스트 핵심
# 좌표, 간선, (값, 인덱스)처럼 서로 관련된 값을 묶을 때 자주 사용한다.
title("연습 문제")
print("좌표 목록 [(1, 3), (0, 2), (1, 1)]을 기본 오름차순으로 정렬해 보세요.")
