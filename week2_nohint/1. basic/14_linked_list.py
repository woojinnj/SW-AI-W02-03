"""
[연결 리스트 - Linked List 기본 구현]

문제 설명:
- 단순 연결 리스트(Singly Linked List)를 구현합니다.
- 노드는 값(data)과 다음 노드를 가리키는 포인터(next)를 가집니다.

입력:
- 연결 리스트에 추가할 값들

출력:
- 연결 리스트의 모든 값 출력

예제:
입력: 1 -> 2 -> 3
출력: [1, 2, 3]
"""


class Node:
    """연결 리스트의 노드"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """단순 연결 리스트"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """리스트 끝에 노드를 추가합니다."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        """리스트의 모든 값을 앞에서부터 차례로 반환합니다."""
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next
        return values


if __name__ == "__main__":
    print("=== 연결 리스트 테스트 ===")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    result = ll.print_list()
    print(f"리스트: {result}")
    print()

    print("=== 연결 리스트 테스트 2 ===")
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)
    result2 = ll2.print_list()
    print(f"리스트: {result2}")
