Mamy zagnieżdżoną listę, na przykład: 
```python
list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]. 
```
Dodaj element o kolejnej wartości w najbardziej zagnieżdżonej liście. W tym przypadku 7 w miejscu 
```python
[1, 2, [3, 4, [5, 6, 7], 5], 3, [4, 5]]
```
Napisz program, który zrobi to uniwersalnie, dla dowolnego zagnieżdżenia, 
```python
np. dla [1 [2, 3] 4]
```
```python
chodzi o [1 [2, 3, 4] 4],
```
```python
dla [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
```
```python
powinno być [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7].
```
Jeżeli największe zagnieżdżenie na danym poziomie się powtórzy, należy dodać w obu zagnieżdżeniach, 
```python
czyli dla [1, [3], [2]]
```
należy uzyskać 
```python
[1, [3, 4], [2, 3]].
```
