# 알고리즘 재활

## 멤버

| 이름 | GitHub |
| --- | --- |
| 천영성 | [@hokoro](https://github.com/hokoro) |
| 이정훈 | [@kinghoon](https://github.com/kinghoon) |

## 재활 항목

| 번호 | 항목         | 상태 | 비고 |
|---:|------------| --- | --- |
|  0 | 자료구조       | 예정 |  |
|  1 | DFS/BFS    | 예정 |  |
|  2 | 그리드        | 예정 |  |
|  3 | 정렬         | 예정 |  |
|  4 | 이진탐색       | 예정 |  |
|  5 | 다이나믹 프로그래밍 | 예정 |  |
|  6 | 최단 경로      | 예정 |  |
|  7 | 그래프        | 예정 |  |

## Git 사용 규칙

### 브랜치 규칙

문제 풀이는 `main` 브랜치에서 바로 작업하지 않고, 개인 브랜치를 만들어서 작업합니다.

브랜치 이름 규칙:

```text
solution/자기네이밍/문제정보
```

예시:

```text
solution/hokoro/dfs-bfs-001
solution/kinghoon/dfs-bfs-001
solution/hokoro/binary-search-001
solution/kinghoon/dp-001
```

| 이름 | 자기네이밍 |
| --- | --- |
| 천영성 | `hokoro` |
| 이정훈 | `kinghoon` |

### 작업 시작할 때

항상 최신 `main`을 먼저 가져온 뒤 새 브랜치를 만듭니다.

```bash
git checkout main
git pull origin main
git checkout -b solution/hokoro/dfs-bfs-001
```

### 작업 상태 확인

```bash
git status
```

### 풀이 저장하기

```bash
git add .
git commit -m "Solve DFS/BFS 001"
```

### GitHub에 브랜치 올리기

```bash
git push origin solution/hokoro/dfs-bfs-001
```

그 다음 GitHub에서 Pull Request를 만들고, 서로 확인한 뒤 `main`에 merge합니다.

### 작업 끝난 뒤 main 최신화

PR이 merge되면 로컬에서도 `main`을 최신 상태로 맞춥니다.

```bash
git checkout main
git pull origin main
```

### 자주 쓰는 명령어

| 상황 | 명령어 |
| --- | --- |
| 현재 상태 확인 | `git status` |
| 브랜치 목록 보기 | `git branch` |
| 새 브랜치 만들고 이동 | `git checkout -b 브랜치명` |
| 브랜치 이동 | `git checkout 브랜치명` |
| 최신 main 가져오기 | `git pull origin main` |
| 변경 파일 추가 | `git add .` |
| 커밋 만들기 | `git commit -m "메시지"` |
| 브랜치 GitHub에 올리기 | `git push origin 브랜치명` |

### 충돌 줄이는 규칙

- 각자 자기 폴더에만 풀이를 올립니다.
- `main`에는 직접 push하지 않습니다.
- README 같은 공용 파일은 동시에 수정하지 않도록 합니다.
- 작업 시작 전에는 항상 `git pull origin main`을 먼저 합니다.

