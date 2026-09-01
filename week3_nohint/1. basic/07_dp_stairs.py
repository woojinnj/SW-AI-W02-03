"""
[동적 프로그래밍 - 계단 오르기 (상향식 / Bottom-up)]

문제 설명:
- 상향식 DP로 계단을 오르는 방법의 수를 계산합니다.
- 한 번에 1칸 또는 2칸을 오를 수 있습니다.
- n번째 계단까지 오르는 경우의 수를 구합니다.

입력:
- n: 계단의 수

출력:
- n번째 계단까지 오르는 방법의 수

예제:
입력: n = 4
출력: 5
설명: 
  1. 1+1+1+1
  2. 1+1+2
  3. 1+2+1
  4. 2+1+1
  5. 2+2
"""

def climb_stairs(n):
    """
    계단 오르기 (상향식 DP)
    
    Args:
        n: 계단의 수
    
    Returns:
        n번째 계단까지 오르는 방법의 수
    """
    pass
if __name__ == '__main__':
    print('=== 계단 오르기 ===')
    for i in range(1, 11):
        result = climb_stairs(i)
        print(f'{i}번 계단: {result}가지')
    print()
    n = 20
    result = climb_stairs(n)
    print(f'{n}번 계단: {result}가지')
    print()
    print('=== 4번 계단의 경로 ===')
    print('1. 1+1+1+1')
    print('2. 1+1+2')
    print('3. 1+2+1')
    print('4. 2+1+1')
    print('5. 2+2')
