"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]
"""
from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    pass
if __name__ == '__main__':
    vertices = 4
    edges = [(0, 1), (0, 2), (1, 3)]
    print('=== 위상 정렬 ===')
    print('과목 관계:')
    print('  0(기초) → 1(중급) → 3(고급)')
    print('  0(기초) → 2(응용)')
    print()
    result = topological_sort(vertices, edges)
    print(f'수강 순서: {result}')
