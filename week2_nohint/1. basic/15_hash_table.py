"""
[해시 테이블 - 학생 성적 관리]

참고:
- 파이썬의 딕셔너리(dict)는 내부적으로 해시 테이블로 구현되어 있습니다.
- 따라서 딕셔너리를 사용하면 해시 테이블의 특성을 그대로 활용할 수 있습니다.
- week1의 01번 문제를 복기 해 보세요.

문제 설명:
- 해시 테이블(딕셔너리)을 사용하여 학생 성적을 관리합니다.
- Key-Value 쌍으로 빠른 검색, 삽입, 삭제가 가능합니다.

입력:
- 학생 이름과 점수

출력:
- 평균 점수
- 최고 점수 학생
- 특정 학생 점수 조회

예제:
입력: {"Alice": 85, "Bob": 92, "Charlie": 78}
출력:
평균 점수: 85.0
최고 점수: Bob (92점)
"""

def manage_grades(students):
    """
    학생 성적 관리 시스템
    
    Args:
        students: {이름: 점수} 딕셔너리
    
    Returns:
        평균, 최고점 학생 이름, 최고점
    """
    pass

def find_student_score(students, name):
    """
    특정 학생의 점수 조회
    
    Args:
        students: 학생 딕셔너리
        name: 찾을 학생 이름
    
    Returns:
        점수 (없으면 None)
    """
    pass
if __name__ == '__main__':
    students1 = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
    print('=== 학생 성적 관리 ===')
    avg, top_name, top_score = manage_grades(students1)
    print(f'평균 점수: {avg}')
    print(f'최고 점수: {top_name} ({top_score}점)')
    print()
    print('=== 학생 점수 조회 ===')
    search_name = 'Alice'
    score = find_student_score(students1, search_name)
    print(f'{search_name}의 점수: {score}')
    print()
    search_name2 = 'Eve'
    score2 = find_student_score(students1, search_name2)
    print(f'{search_name2}의 점수: {score2}')
