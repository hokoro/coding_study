"""
파이썬 함수와 코딩 테스트에서 자주 사용하는 내장 함수 및 표준 라이브러리.

주요 모듈: math, itertools, collections
"""

import math
from collections import Counter, defaultdict, deque
from itertools import (
    accumulate,
    combinations,
    combinations_with_replacement,
    permutations,
    product,
)


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 함수 정의와 호출 -------------------------------------------------------
title("1. 함수 정의와 호출")


def add(a, b):
    """두 값을 더해 반환한다."""
    return a + b


print(add(3, 5))
print(add(a=3, b=5))  # 키워드 인수


# 2. 매개변수와 기본값 -----------------------------------------------------
title("2. 매개변수와 기본값")


def greet(name, message="안녕하세요"):
    return f"{message}, {name}"


print(greet("Kim"))
print(greet("Kim", "반갑습니다"))


# 3. 여러 값 반환과 가변 인수 ---------------------------------------------
title("3. 반환값과 가변 인수")


def calculate(a, b):
    return a + b, a * b  # 여러 값은 튜플로 반환된다.


total, product_value = calculate(3, 4)
print(total, product_value)


def add_all(*numbers):
    return sum(numbers)


print(add_all(1, 2, 3, 4))


def print_information(**information):
    print(information)


print_information(name="Kim", score=100)


# 4. 지역 변수와 전역 변수 -------------------------------------------------
title("4. 변수의 범위")

value = 10


def show_scope():
    value = 20  # 함수 안의 지역 변수
    print("함수 내부:", value)


show_scope()
print("함수 외부:", value)

# 가능하면 global에 의존하기보다 값을 매개변수로 받고 return하는 편이 좋다.


# 5. 자주 사용하는 내장 함수 ----------------------------------------------
title("5. 내장 함수")

numbers = [3, -5, 2, 8, 1]

print("len:", len(numbers))
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("abs:", abs(-10))
print("round:", round(3.14159, 2))
print("divmod:", divmod(17, 5))
print("pow:", pow(2, 10))
print("sorted:", sorted(numbers))

# any(): 하나라도 True이면 True
# all(): 모든 값이 True이면 True
print("any:", any(number < 0 for number in numbers))
print("all:", all(number > 0 for number in numbers))

# enumerate(): 인덱스와 값
print(list(enumerate(["a", "b", "c"])))

# zip(): 여러 반복 가능한 자료의 같은 위치 값을 묶음
print(list(zip(["Kim", "Lee"], [90, 100])))


# 6. lambda, map, filter ---------------------------------------------------
title("6. lambda, map, filter")

# lambda 매개변수: 반환할 식
square = lambda number: number ** 2
print(square(5))

numbers = [1, 2, 3, 4]
print(list(map(lambda number: number ** 2, numbers)))
print(list(filter(lambda number: number % 2 == 0, numbers)))

# 코딩 테스트 입력에서 가장 자주 사용하는 map 패턴
texts = ["10", "20", "30"]
print(list(map(int, texts)))


# 7. 재귀 함수 -------------------------------------------------------------
title("7. 재귀 함수")


def factorial_recursive(number):
    # 종료 조건이 없으면 무한히 호출되므로 반드시 작성한다.
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)


print(factorial_recursive(5))

# 재귀 깊이가 큰 문제는 반복문이나 명시적인 스택 사용도 고려한다.


# 8. math ------------------------------------------------------------------
title("8. math 모듈")

print("올림:", math.ceil(3.14))
print("내림:", math.floor(3.99))
print("제곱근:", math.sqrt(16))       # float 반환
print("정수 제곱근:", math.isqrt(17)) # 4
print("팩토리얼:", math.factorial(5))
print("최대공약수:", math.gcd(12, 18))
print("최소공배수:", math.lcm(12, 18))
print("원주율:", math.pi)
print("무한대:", math.inf)

# 여러 수의 최대공약수와 최소공배수도 계산할 수 있다.
print(math.gcd(12, 18, 24))
print(math.lcm(4, 6, 8))

# 제곱수 판별에서 실수 sqrt보다 isqrt가 안전하다.
number = 49
root = math.isqrt(number)
print("완전제곱수:", root * root == number)


# 9. itertools: 순열 -------------------------------------------------------
title("9. itertools.permutations")

data = [1, 2, 3]

# permutations(반복 가능한 객체, 선택 개수): 순서가 중요하며 중복 선택하지 않음
permutation_result = list(permutations(data, 2))
print(permutation_result)
print("개수:", len(permutation_result))


# 10. itertools: 조합 ------------------------------------------------------
title("10. itertools.combinations")

# combinations(): 순서가 중요하지 않으며 중복 선택하지 않음
combination_result = list(combinations(data, 2))
print(combination_result)

# combinations_with_replacement(): 순서가 중요하지 않으며 중복 선택 가능
replacement_result = list(combinations_with_replacement(data, 2))
print(replacement_result)


# 11. itertools: product ---------------------------------------------------
title("11. itertools.product")

# product(): 여러 그룹에서 하나씩 선택하는 데카르트 곱
print(list(product(["A", "B"], [1, 2])))

# repeat을 사용하면 중복 순열처럼 활용할 수 있다.
print(list(product([0, 1], repeat=3)))


# 12. itertools: accumulate ------------------------------------------------
title("12. itertools.accumulate")

# 누적합을 차례대로 반환한다.
numbers = [1, 2, 3, 4]
prefix_sum = list(accumulate(numbers))
print(prefix_sum)  # [1, 3, 6, 10]

# 구간 left부터 right까지의 합:
# prefix_sum[right] - prefix_sum[left - 1]

# initial=0을 사용하면 앞에 0이 포함되어 구간 합 계산이 편리하다.
prefix_sum_with_zero = list(accumulate(numbers, initial=0))
print(prefix_sum_with_zero)  # [0, 1, 3, 6, 10]


# 13. collections: Counter -------------------------------------------------
title("13. collections.Counter")

# 각 값의 등장 횟수를 딕셔너리처럼 저장한다.
counter = Counter("banana")
print(counter)
print(counter["a"])
print(counter["없는 값"])  # 없는 값은 0
print(counter.most_common())
print(counter.most_common(2))

left = Counter("aabbc")
right = Counter("abbdd")
print("교집합:", left & right)
print("합집합:", left | right)


# 14. collections: defaultdict --------------------------------------------
title("14. collections.defaultdict")

count = defaultdict(int)
for character in "banana":
    count[character] += 1
print(dict(count))

groups = defaultdict(list)
for key, value in [("odd", 1), ("even", 2), ("odd", 3)]:
    groups[key].append(value)
print(dict(groups))


# 15. collections: deque ---------------------------------------------------
title("15. collections.deque")

# 양쪽 끝에서 추가와 삭제가 빠르므로 큐와 BFS에서 자주 사용한다.
queue = deque([1, 2, 3])
queue.append(4)       # 오른쪽 추가
queue.appendleft(0)   # 왼쪽 추가
print(queue)

print(queue.popleft())  # 왼쪽 삭제: 큐
print(queue.pop())      # 오른쪽 삭제
print(queue)

queue.rotate(1)         # 오른쪽으로 한 칸 회전
print(queue)
queue.rotate(-1)        # 왼쪽으로 한 칸 회전
print(queue)


# 16. 선택 기준 ------------------------------------------------------------
title("16. 어떤 도구를 사용할까?")

print(
    """
빈도 계산                 -> Counter 또는 defaultdict(int)
그룹별 리스트 저장        -> defaultdict(list)
BFS, 큐, 양방향 삽입/삭제 -> deque
순서가 다른 경우 나열     -> permutations
순서 없이 선택            -> combinations
각 그룹에서 하나씩 선택   -> product
누적합                     -> accumulate
최대공약수/최소공배수      -> math.gcd(), math.lcm()
정확한 정수 제곱근        -> math.isqrt()
"""
)


title("연습 문제")
print(
    """
1. Counter로 문자열에서 가장 많이 등장한 문자를 구해 보세요.
2. combinations로 숫자 5개 중 3개를 고르는 모든 경우를 만들어 보세요.
3. deque를 사용해 간단한 큐의 삽입과 삭제를 구현해 보세요.
4. accumulate를 사용해 구간 합을 계산해 보세요.
"""
)
