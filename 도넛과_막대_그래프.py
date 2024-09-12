edges = [[2, 3], [4, 3], [1, 1], [2, 1]]

def solution(edges):

    N = max(max(edge[0] for edge in edges), max(edge[1] for edge in edges))    # 정점의 개수
    adjL = [[] for _ in range(N+1)]    # 인덱스 번호 맞추기    # 인접리스트

    # 인접리스트 만들기
    for edge in edges:
        v1, v2 = edge[0], edge[1]
        adjL[v1].append(v2)

    # 모든 정점을 출발점으로 해서 DFS를 돌고 그 경로가 어떤 그래프를 이루는지 확인하자
    for i in range(1, N+1):
        nodes = []    # 경로를 담는 리스트
        lines = [0]
        visited = [0]*(N+1)    # 방문 리스트

        def DFS(start):
            nodes.append(start)
            visited[start] = 1
            for next in adjL[start]:
                if visited[next]:
                    continue
                lines[0] += 1
                DFS(next)

        DFS(i)

        print(i)
        print(lines)
        print(nodes)

solution(edges)