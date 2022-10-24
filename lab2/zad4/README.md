Mamy trzy liczby całkowite, x, y, z reprezentujące wymiary prostopadłościanu, oraz pewną liczbę naturalną
n. Wypisz listę wszystkich możliwych współrzędnych (i, j, k) na trójwymiarowej siatce, gdzie i+j+k nie jest
równe n. 
```
Warunki: 0 <= i <= x, 0 <= j <= y, 0 <= k <= z. 
```
Rozwiązanie zapisz w postaci list składanych (list
comprehesion), ale można zacząć od zagnieżdżonych pętli. Przykład. 
```python
Niech x = 1, y = 1, z = 2, n = 3. 
```
Lista wszystkich permutacji trójek [i, j, k] w tym przykładzie: 
```python
[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]].
```
Elementy, które nie sumują się do 3 to: 
```python
[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]].
```
Parametry x, y, z, n wczytać na początku za pomocą funkcji input().
