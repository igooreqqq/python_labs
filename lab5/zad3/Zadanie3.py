import sys

import pygame
from random import randint

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 600:
           self.rect.x = 600



class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(-8, 8), randint(4, 8)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self, score):
        self.velocity[0] = 5 * score
        self.velocity[1] = -self.velocity[1]



# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
record = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            sys.exit()
    rakietkaA = Rakietka(BIALY, 100, 10)
    rakietkaA.rect.x = 300
    rakietkaA.rect.y = 450


    pileczka = Pilka(BIALY,10,10)
    pileczka.rect.x = randint(10, 680)
    pileczka.rect.y = 0

    # lista wszystkich widzalnych obiektów potomnych z klasy Sprite
    all_sprites_list = pygame.sprite.Group()

    # dodanie obu rakietek i piłeczki do listy
    all_sprites_list.add(rakietkaA)
    all_sprites_list.add(pileczka)

    # służy do kontroli liczby klatek na sekudnę (fps)
    clock = pygame.time.Clock()

    # Początkowe wyniki graczy
    scoreA = 0

    # -------- GLÓWNA PĘTLA PROGRAMU -----------
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # zamknięcie okienka
                sys.exit()

        # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rakietkaA.moveLeft(10)
        if keys[pygame.K_RIGHT]:
            rakietkaA.moveRight(10)

        # aktualizacja listy duszków
        all_sprites_list.update()

        # sprawdzenie czy piłeczka nie uderza w którąś ścianę
        # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
        if pileczka.rect.x>=690:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.x<=0:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.y>495:
            break
        if pileczka.rect.y<0:
            pileczka.velocity[1] = -pileczka.velocity[1]

        # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
        if pygame.sprite.collide_mask(pileczka, rakietkaA):
            pileczka.bounce(scoreA)
            scoreA += 1

        # RYSOWANIE
        # czarny ekran
        screen.fill(CZARNY)
        # cienka linia przez środek boiska

        # narysowanie obiektów
        all_sprites_list.draw(screen)

        # wyświetlanie wyników
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, BIALY)
        screen.blit(text, (250,10))

        # odświeżenie / przerysowanie całego ekranu
        pygame.display.flip()

        # 60 klatek na sekundę
        clock.tick(60)

    f = open("wynik.txt")
    recordStr = f.read()
    record = int(recordStr)
    f.close()

    if record < scoreA:
        record = scoreA
        f = open("wynik.txt", mode='w')
        f.write(str(record))
        f.close()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # zamknięcie okienka
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            break
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        screen.fill(CZARNY)

        font = pygame.font.Font(None, 50)
        text = font.render("Obecny wynik: " + str(scoreA), 1, BIALY)
        screen.blit(text, (10, 80))

        font = pygame.font.Font(None, 50)
        text = font.render("Obecny rekord: " + str(record), 1, BIALY)
        screen.blit(text, (10, 140))

        font = pygame.font.Font(None, 50)
        text = font.render("Wciśnij 'r' by zacząć ponownie", 1, BIALY)
        screen.blit(text, (10, 220))

        font = pygame.font.Font(None, 50)
        text = font.render("Wciśnij 'esc' by wyjść z gry", 1, BIALY)
        screen.blit(text, (10, 280))

        # odświeżenie / przerysowanie całego ekranu
        pygame.display.flip()

        # 60 klatek na sekundę
        clock.tick(60)