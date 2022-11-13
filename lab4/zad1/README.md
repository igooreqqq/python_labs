Zadanie ma na celu sprawdzenie jak wygląda tworzenie obiektów dla typów z wielokrotnym dziedziczeniem,
jakie funkcje __new__ oraz __init__ są lub nie są wywoływane. Wychodzimy od dwóch klas bazowych
(identycznych, różnią się tylko nazwą), class Baza(object) oraz class A(object) – patrz plik zadanie1.py. Posiadają
one napisane __new__, __init__, __str__ oraz funkcję id(). Proszę przestudiować kilka różnych wariantów klas
potomnych (B, C, D...) oraz tworzenia odpowiednich obiektów. Proponowane scenariusze są zapisane w pliku,
klasy potomne powinny mieć zawartość zbliżoną, w celach studyjnych, do klas bazowych. W programie
uruchomieniowym prezentować (oraz potrafić przedyskutować co się dzieje) różne scenariusze, włączając
zagadnienie MRO (Method Resolution Order).
