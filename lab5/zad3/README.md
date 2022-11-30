Najpierw należy przestudiować załączony kod (main.py wszystko w jednym pliku), jest to klasyczna gra w ping-
ponga, napisana z użyciem znanej nam biblioteki pygame. Proszę po kolei przestudiować kod, który jest
komentowany i choć (ewentualnie) zawiera rzeczy nowe, to można się domyślić o co chodzi. W szczególności
na początku są definicje dwóch klas Rakietka i Pilka, które zapisane są jako dziedziczące z klasy
pygame.sprite.Sprite (proszę zobaczyć w kodzie jak to wygląda). Klasy są dość proste, ich metody dbają
o zmianę i sprawdzenie położeń granicznych oraz ustalanie (np. losowanie w pewnym zakresie) wartości
prędkości piłki. Program zaczyna się od narysowania ekranu, rakietek, piłki (piłka jest o rozmiarze 10x10
punktów), utworzeniu listy widzialnych w grze obiektów (właśnie odziedziczonych z klasy Sprite). Sama
mechanika ruchów rakietek powinna być już znana z poprzednich zadań, ciekawa jest metoda collide_mask
sprawdzająca czy dane dwa obiekty nie są ze sobą w styczności / kolizji, jeśli tak jest, to na rzecz piłeczki
wołamy metodę bounce(), która zmienia (i trochę losuje) składową prędkości piłki po odbiciu. Zadanie: po
przestudiowaniu i uruchomieniu kodu zadanie będzie polegać na takim jego zmodyfikowaniu, żeby:
(a) rakietka była tylko jedna, poruszająca się w poziomie na dole ekranu (w lewo i prawo, strzałkami),
(b) piłeczka uruchamiana losowo z góry, punkty mają być naliczane za poprawne odbicie od rakietki, (c) gra ma
się zakończyć jeśli piłeczka minie rakietkę i zderzy się ze ścianą – wtedy powinien się wyświetlić wynik końcowy
oraz dotychczasowy najwyższy wynik. Najlepszy wynik zapisywać do i odczytywać z pliku. Oczywiście pionowa
linia jest teraz zbędna. Innymi słowy – przerobić to na grę „jednoosobową”.
