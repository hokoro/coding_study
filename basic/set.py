"""중복 제거와 빠른 포함 확인에 사용하는 집합(set) 학습 자료."""


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 생성 ------------------------------------------------------------------
title("1. 집합 생성")

numbers = {1, 2, 3}
from_list = set([1, 1, 2, 2, 3])
empty = set()  # {}는 빈 딕셔너리이므로 빈 집합은 set()으로 만든다.

print(numbers)
print(from_list)
print(empty, type(empty))
print({}, type({}))

# 집합은 중복을 허용하지 않으며 인덱스와 순서를 사용하지 않는다.
# print(numbers[0])  # TypeError 발생


# 2. 추가와 삭제 -----------------------------------------------------------
title("2. 추가와 삭제")

data = {1, 2}
data.add(3)             # 값 하나 추가
print(data)

data.update([3, 4, 5])  # 여러 값 추가
print(data)

data.remove(3)          # 없는 값을 삭제하면 KeyError
print(data)

data.discard(100)       # 없는 값을 삭제해도 오류가 발생하지 않음
print(data)

removed = data.pop()    # 임의의 원소를 삭제하고 반환
print("삭제한 값:", removed)

data.clear()
print(data)


# 3. 포함 여부와 길이 ------------------------------------------------------
title("3. 포함 여부")

visited = {1, 3, 5, 7}

print(3 in visited)
print(2 not in visited)
print(len(visited))

# 코딩 테스트에서 set은 특정 값의 존재 여부를 빠르게 확인할 때 유용하다.
numbers = [1, 2, 3, 4, 5]
number_set = set(numbers)
print(4 in number_set)


# 4. 집합 연산 -------------------------------------------------------------
title("4. 집합 연산")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("합집합:", a | b)
print("합집합:", a.union(b))
print("교집합:", a & b)
print("교집합:", a.intersection(b))
print("차집합:", a - b)
print("차집합:", a.difference(b))
print("대칭 차집합:", a ^ b)  # 한쪽에만 있는 값
print("대칭 차집합:", a.symmetric_difference(b))


# 5. 원본을 변경하는 집합 연산 --------------------------------------------
title("5. 원본 변경 연산")

data = {1, 2, 3}
data |= {3, 4}  # 합집합 결과를 원본에 저장
print(data)

data &= {2, 3, 4}  # 교집합 결과를 원본에 저장
print(data)

data -= {3}  # 차집합 결과를 원본에 저장
print(data)


# 6. 부분집합과 서로소 -----------------------------------------------------
title("6. 부분집합과 서로소")

a = {1, 2}
b = {1, 2, 3}
c = {4, 5}

print(a <= b)              # 부분집합
print(a < b)               # 진부분집합
print(b >= a)              # 상위집합
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(c))     # 공통 원소가 없으면 True


# 7. 중복 제거 -------------------------------------------------------------
title("7. 중복 제거")

numbers = [3, 1, 2, 3, 2, 1]

# 집합으로 변환하면 중복이 제거되지만 기존 순서는 보장하지 않는다.
unique = list(set(numbers))
print(unique)

# 정렬된 중복 제거 결과
sorted_unique = sorted(set(numbers))
print(sorted_unique)

# 입력 순서를 유지하면서 중복 제거
ordered_unique = list(dict.fromkeys(numbers))
print(ordered_unique)


# 8. 집합 컴프리헨션 -------------------------------------------------------
title("8. 집합 컴프리헨션")

squares = {number ** 2 for number in range(-3, 4)}
evens = {number for number in range(1, 11) if number % 2 == 0}

print(squares)  # 같은 제곱 결과는 한 번만 저장된다.
print(evens)


# 9. frozenset -------------------------------------------------------------
title("9. frozenset")

# 일반 set은 변경 가능하므로 다른 집합의 원소나 딕셔너리 key가 될 수 없다.
# frozenset은 변경할 수 없는 집합이다.
fixed = frozenset([1, 2, 3])
container = {fixed}
dictionary = {fixed: "값"}

print(container)
print(dictionary[fixed])


# 10. 코딩 테스트 활용 -----------------------------------------------------
title("10. 코딩 테스트 활용")

left = [1, 2, 3, 4]
right = [3, 4, 5]

common = set(left) & set(right)
print("공통 값:", sorted(common))

# 입력 예제
# numbers = set(map(int, input().split()))
# queries = list(map(int, input().split()))
# for query in queries:
#     print(1 if query in numbers else 0)

title("연습 문제")
print("두 숫자 리스트에서 공통으로 등장하는 숫자를 중복 없이 정렬해 보세요.")
