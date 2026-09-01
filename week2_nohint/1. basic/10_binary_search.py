"""
[이분 탐색 - Binary Search]

문제 설명:
- 정렬된 배열에서 특정 값을 찾는 이분 탐색 알고리즘을 구현합니다.
- 배열을 반으로 나누어 탐색 범위를 절반씩 줄여갑니다.

입력:
- arr: 정렬된 정수 배열
- target: 찾고자 하는 값

출력:
- target이 있는 인덱스 (없으면 -1)

예제:
입력: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
출력: 3
"""


def binary_search(arr, target):
    """
    이분 탐색 구현

    Args:
        arr: 정렬된 배열
        target: 찾을 값

    Returns:
        target의 인덱스 (없으면 -1)
    """
    '''
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        mid_v=arr[mid]
        if mid_v==target:
            return mid
        if mid_v<target:
            left=mid+1
        if mid_v>target:
            right=mid-1

    return -1
    '''
def binary_search_recursive(arr,target,left=0,right=None):
    if right is None:
        right=len(arr)-1

    if left>right:
        return -1

    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    if arr[mid]<target:
        return binary_search(arr,target,mid+1,right)
    return binary_search(arr,target,left,mid-1)


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"배열: {arr1}")
    print(f"찾는 값: {target1}")
    print(f"결과: 인덱스 {result1}")
    print()
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target2 = 14
    result2 = binary_search(arr2, target2)
    print(f"배열: {arr2}")
    print(f"찾는 값: {target2}")
    print(f"결과: 인덱스 {result2}")
    print()
    arr3 = [1, 3, 5, 7, 9]
    target3 = 6
    result3 = binary_search(arr3, target3)
    print(f"배열: {arr3}")
    print(f"찾는 값: {target3}")
    print(f"결과: 인덱스 {result3}")
