"""
[동적 프로그래밍 - 피보나치 수열 (하향식 / Top-down)]

문제 설명:
- 메모이제이션(Memoization)을 사용한 하향식 DP로 피보나치 수를 계산합니다.
- 이미 계산한 값을 저장하여 중복 계산을 방지합니다.

입력:
- n: 구하고자 하는 피보나치 수의 인덱스

출력:
- n번째 피보나치 수

예제:
입력: n = 10
출력: 55
"""

def fibonacci_memo(n, memo=None):
    """
    메모이제이션을 사용한 피보나치 (하향식 DP)
    
    Args:
        n: 피보나치 인덱스
        memo: 계산 결과를 저장할 딕셔너리
    
    Returns:
        n번째 피보나치 수
    """
    pass
if __name__ == '__main__':
    print('=== 피보나치 수열 (메모이제이션) ===')
    for i in range(11):
        result = fibonacci_memo(i)
        print(f'fib({i}) = {result}')
    print()
    print('=== 큰 수 계산 ===')
    n = 50
    result = fibonacci_memo(n)
    print(f'fib({n}) = {result}')
    print()
    print('참고: 일반 재귀는 fib(40)도 몇 초 걸리지만')
    print('메모이제이션은 fib(100)도 순식간에 계산!')
