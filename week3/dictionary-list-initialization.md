# Python 딕셔너리 안의 리스트를 먼저 초기화하는 이유

Python에서 딕셔너리는 키와 값을 함께 저장하는 자료형이다.

```python
data = {}
data["A"] = 10
```

결과는 다음과 같다.

```python
{"A": 10}
```

딕셔너리에는 키와 값을 바로 넣을 수 있다. 그렇다면 다음과 같이 빈 리스트를 먼저 넣는 이유는 무엇일까?

```python
data["A"] = []
```

## 딕셔너리에는 `append()`가 없다

`append()`는 리스트에 값을 추가하는 메서드다. 따라서 딕셔너리 자체에는 사용할 수 없다.

```python
data = {}
data.append(1)  # AttributeError
```

하지만 딕셔너리의 값으로 리스트를 저장하면 그 리스트에는 `append()`를 사용할 수 있다.

```python
data = {"A": []}
data["A"].append(1)
```

결과:

```python
{"A": [1]}
```

여기서:

- `data`는 딕셔너리
- `"A"`는 키
- `data["A"]`는 키 `"A"`에 해당하는 리스트
- `append(1)`은 그 리스트에 값을 추가하는 작업

즉, `append()`를 딕셔너리에 사용한 것이 아니라 **딕셔너리 안에 저장된 리스트에 사용한 것**이다.

## 왜 빈 리스트로 먼저 초기화할까?

다음 코드는 오류가 발생한다.

```python
data = {}
data["A"].append(1)  # KeyError
```

딕셔너리에 `"A"`라는 키가 아직 없기 때문에 `data["A"]`를 가져올 수 없기 때문이다.

따라서 먼저 키와 빈 리스트를 추가해야 한다.

```python
data["A"] = []
data["A"].append(1)
```

쉽게 말하면 다음과 같은 순서다.

```python
data["A"] = []       # 값을 담을 리스트 만들기
data["A"].append(1)  # 만들어진 리스트에 값 추가하기
```

## 초기화 없이 바로 넣을 수도 있다

처음부터 값이 정해져 있다면 빈 리스트를 만들지 않고 바로 넣어도 된다.

```python
data = {}
data["A"] = [1]
```

하지만 여러 값을 하나씩 추가하려면 리스트를 미리 만들어 두는 것이 편리하다.

```python
data["A"].append(2)
data["A"].append(3)
```

결과:

```python
{"A": [1, 2, 3]}
```

## 여러 키를 미리 초기화하기

여러 항목에 값을 계속 추가해야 한다면 반복문으로 빈 리스트를 만들 수 있다.

```python
data = {}

for key in ["A", "B", "C"]:
    data[key] = []
```

결과:

```python
{
    "A": [],
    "B": [],
    "C": []
}
```

이제 각각의 리스트에 값을 추가할 수 있다.

```python
data["A"].append(1)
data["B"].append(2)
```

## 자동으로 초기화하는 방법

`defaultdict`를 사용하면 빈 리스트를 직접 만들지 않아도 된다.

```python
from collections import defaultdict

data = defaultdict(list)
data["A"].append(1)
```

존재하지 않는 키를 사용하면 빈 리스트가 자동으로 만들어진다.

## 정리

딕셔너리에는 키와 값을 바로 추가할 수 있다.

```python
data["A"] = [1]
```

다만 `append()`를 사용해 값을 하나씩 추가하려면 해당 키에 리스트가 먼저 존재해야 한다.

```python
data["A"] = []
data["A"].append(1)
```

결국 빈 리스트로 초기화하는 이유는 **딕셔너리의 각 키에 여러 값을 하나씩 안전하게 추가하기 위해서**다.
