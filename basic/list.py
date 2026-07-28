"""코딩 테스트에서 자주 사용하는 파이썬 리스트 문법과 함수."""


def title(text):
    print(f"\n{'=' * 10} {text} {'=' * 10}")


# 1. 생성과 조회 -----------------------------------------------------------
title("1. 리스트 생성과 조회")

numbers = [10, 20, 30, 40, 50]
empty = []
repeated = [0] * 5

print(numbers)
print(empty)
print(repeated)
print(numbers[0], numbers[-1])  # 첫 번째, 마지막 값
print("길이:", len(numbers))


# 2. 슬라이싱 --------------------------------------------------------------
title("2. 슬라이싱")

print(numbers[1:4])   # 인덱스 1부터 3까지
print(numbers[:3])    # 처음부터 인덱스 2까지
print(numbers[2:])    # 인덱스 2부터 끝까지
print(numbers[::2])   # 두 칸씩
print(numbers[::-1])  # 역순

# 슬라이싱은 새로운 리스트를 만든다.
copied = numbers[:]
copied[0] = 100
print("원본:", numbers)
print("복사:", copied)


# 3. 값 추가 ---------------------------------------------------------------
title("3. 값 추가")

data = [1, 2]
data.append(3)          # 마지막에 값 하나 추가
print(data)

data.extend([4, 5])     # 여러 값을 마지막에 추가
print(data)

data.insert(1, 100)     # 지정한 인덱스에 값 추가
print(data)

# append([6, 7])은 리스트 자체를 하나의 값으로 넣는다는 점에 주의한다.
example = [1, 2]
example.append([3, 4])
print(example)          # [1, 2, [3, 4]]


# 4. 값 수정과 삭제 --------------------------------------------------------
title("4. 값 수정과 삭제")

data = [10, 20, 30, 20]
data[0] = 100
print(data)

data.remove(20)         # 처음 발견한 값 하나를 삭제
print(data)

removed = data.pop()    # 마지막 값을 삭제하고 반환
print("삭제한 값:", removed, "남은 값:", data)

removed = data.pop(0)   # 지정한 인덱스의 값을 삭제하고 반환
print("삭제한 값:", removed, "남은 값:", data)

data = [1, 2, 3]
del data[1]
print(data)

data.clear()            # 모든 값 삭제
print(data)


# 5. 검색과 개수 -----------------------------------------------------------
title("5. 검색과 개수")

data = [10, 20, 10, 30]

print(20 in data)
print(40 not in data)
print(data.index(20))    # 값이 처음 등장한 인덱스
print(data.count(10))    # 값이 등장한 횟수

# index()는 값이 없으면 ValueError가 발생하므로 필요하면 in으로 확인한다.
target = 40
if target in data:
    print(data.index(target))


# 6. 리스트 연산과 기본 함수 ----------------------------------------------
title("6. 리스트 연산과 기본 함수")

left = [1, 2]
right = [3, 4]
numbers = [5, 2, 8, 1]

print(left + right)
print(left * 3)
print("합:", sum(numbers))
print("최솟값:", min(numbers))
print("최댓값:", max(numbers))


# 7. 정렬과 뒤집기 ---------------------------------------------------------
title("7. 정렬과 뒤집기")

numbers = [3, 1, 4, 2]
numbers.sort()                   # 원본을 오름차순으로 정렬
print(numbers)

numbers.sort(reverse=True)       # 원본을 내림차순으로 정렬
print(numbers)

original = [3, 1, 4, 2]
new_list = sorted(original)      # 정렬된 새 리스트 반환
print("원본:", original)
print("새 리스트:", new_list)

original.reverse()               # 현재 순서를 반대로 변경
print(original)


# 8. 리스트 순회 -----------------------------------------------------------
title("8. 리스트 순회")

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# 9. 리스트 컴프리헨션 -----------------------------------------------------
title("9. 리스트 컴프리헨션")

squares = [number ** 2 for number in range(1, 6)]
evens = [number for number in range(1, 11) if number % 2 == 0]
converted = [int(text) for text in ["10", "20", "30"]]

print(squares)
print(evens)
print(converted)


# 10. 2차원 리스트 ---------------------------------------------------------
title("10. 2차원 리스트")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[1][2])  # 두 번째 행, 세 번째 열: 6

for row in matrix:
    print(*row)

# 서로 독립된 행을 만들 때는 컴프리헨션을 사용한다.
board = [[0] * 3 for _ in range(2)]
board[0][0] = 1
board2 = [[0] * 3] * 2
print(board)
print(board2)

# 아래 방식은 모든 행이 같은 리스트를 가리키므로 피해야 한다.
wrong_board = [[0] * 3] * 2
wrong_board[0][0] = 1
print(wrong_board)  # 두 행이 함께 변경된다.


# 11. 언패킹과 zip() -------------------------------------------------------
title("11. 언패킹과 zip()")

first, second, third = [10, 20, 30]
print(first, second, third)

head, *middle, tail = [1, 2, 3, 4, 5]
print(head, middle, tail)

names = ["Kim", "Lee", "Park"]
scores = [90, 80, 100]

for name, score in zip(names, scores):
    print(name, score)


# 12. 코딩 테스트 입력 -----------------------------------------------------
title("12. 코딩 테스트 입력")

# numbers = list(map(int, input().split()))
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# board = [list(input().strip()) for _ in range(n)]

print("핵심 패턴: list(map(int, input().split()))")
