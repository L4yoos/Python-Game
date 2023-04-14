import pygame
import random


def rozpocznijgre():

    pygame.init()
    screen = width, height = 800, 900
    win = pygame.display.set_mode(screen)
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()
    FPS = 20

    CELLSIZE = 20
    ROWS = (height - 120) // CELLSIZE
    COLS = width // CELLSIZE
    print(ROWS, COLS)

    BLACK = (21, 24, 29)
    BLUE = (31, 25, 76)
    RED = (252, 91, 122)
    WHITE = (255, 255, 255)

    img1 = pygame.image.load('Pliki/1.png')
    img2 = pygame.image.load('Pliki/2.png')
    img3 = pygame.image.load('Pliki/3.png')
    img4 = pygame.image.load('Pliki/4.png')

    Pliki = {
        1: img1,
        2: img2,
        3: img3,
        4: img4
    }

    font = pygame.font.Font('Pliki/unlearne.ttf', 50)
    font2 = pygame.font.SysFont('cursive', 25)

    class podsttetris:
        # Matrix
        #  0  1  2  3
        #  4  5  6  7
        #  8  9 10 11
        # 12 13 14 15

        Figury = {
            'I' : [[1, 5, 9, 13], [4, 5, 6, 7]],
            'Z' : [[4, 5, 9, 10], [2, 6, 5, 9]],
            'S' : [[6, 7, 9, 10], [1, 5, 6, 10]],
            'L' : [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
            'J' : [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
            'T' : [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
            'O' : [[1,2, 5, 6]]
        }

        TypyFigur = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.type = random.choice(self.TypyFigur)
            self.shape = self.Figury[self.type]
            self.color = random.randint(1, 4)
            self.rotation = 0

        def image(self):
            return self.shape[self.rotation]

        def rotate(self):
            self.rotation = (self.rotation + 1) % len(self.shape)


    class Tetris:
        def __init__(self, rows, cols):
            self.rows = rows
            self.cols = cols
            self.score = 0
            self.level = 1
            self.autor = "Konrad Dalecki"
            self.board = [[0 for j in range(cols)] for i in range(rows)]
            self.next_shape = None
            self.gameover = False
            self.new_figure()

        def draw_grid(self):
            for i in range(self.rows + 1):
                pygame.draw.line(win, WHITE, (0, CELLSIZE * i), (width, CELLSIZE * i), 1)
            for j in range(self.cols):
                pygame.draw.line(win, WHITE, (CELLSIZE * j, 0), (CELLSIZE * j, height), 1)

        def new_figure(self):
            if not self.next_shape:
                self.next_shape = podsttetris(18, 0)
            self.figure = self.next_shape
            self.next_shape = podsttetris(18, 0)

        def intersects(self):
            intersection = False
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        if i + self.figure.y > self.rows - 1 or \
                            j + self.figure.x > self.cols - 1 or \
                            j + self.figure.x < 0 or \
                            self.board[i + self.figure.y][j + self.figure.x] > 0:
                                intersection = True

            return intersection

        def remove_line(self):
            rerun = False
            for y in range(self.rows-1, 0, -1):
                Ostatnia_Linia = True
                for x in range(0, self.cols):
                    if self.board[y][x] == 0:
                        Ostatnia_Linia = False

                if Ostatnia_Linia:
                    del self.board[y]
                    self.board.insert(0,[0 for i in range(self.cols)])
                    self.score += 1
                    if self.score % 10 == 0:
                        self.level = 1
                    rerun = True

            if rerun:
                self.remove_line()

        def freeze(self):
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        self.board[i + self.figure.y][j + self.figure.x] = self.figure.color
            self.remove_line()
            self.new_figure()
            if self.intersects():
                self.gameover = True

        def go_Space(self):
            while not self.intersects():
                self.figure.y += 1
            self.figure.y -= 1
            self.freeze()

        def go_down(self):
            self.figure.y += 1
            if self.intersects():
                self.figure.y -= 1
                self.freeze()

        def go_side(self, dx):
            self.figure.x += dx
            if self.intersects():
                self.figure.x -= dx

        def rotate(self):
            rotation = self.figure.rotation
            self.figure.rotate()

    counter = 0

    move_down = False
    gra = True
    can_move= True

    tetris = Tetris(ROWS, COLS)

    while gra:
        win.fill(BLACK)

        counter += 1
        if counter >= 10000:
            counter = 0

        if can_move:
            if counter % (FPS // (tetris.level * 2)) == 0 or move_down:
                if not tetris.gameover:
                    tetris.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gra = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    gra = False

                if event.key == pygame.K_m:
                    import menu
                    menu.main_menu()

                if event.key == pygame.K_LEFT:
                    tetris.go_side(-1)

                if event.key == pygame.K_RIGHT:
                    tetris.go_side(1)

                if event.key == pygame.K_UP:
                    tetris.rotate()

                if event.key == pygame.K_DOWN:
                    move_down = True

                if event.key == pygame.K_SPACE:
                    tetris.go_Space()

                if event.key == pygame.K_p:
                    can_move = not can_move

                if event.key == pygame.K_r:
                    tetris.__init__(ROWS, COLS)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    move_down = False

        # tetris.draw_grid()

        for x in range(ROWS):
            for y in range(COLS):
                if tetris.board[x][y] > 0:
                    val = tetris.board[x][y]
                    img = Pliki[val]
                    win.blit(img, (y*CELLSIZE, x*CELLSIZE))
                    pygame.draw.rect(win, WHITE, (y*CELLSIZE, x*CELLSIZE, CELLSIZE, CELLSIZE), 1)

        for i in range(4):
            for j in range(4):
                if i * 4 + j in tetris.figure.image():
                    x = CELLSIZE * (tetris.figure.x + j)
                    y = CELLSIZE * (tetris.figure.y + i)
                    img = Pliki[tetris.figure.color]
                    win.blit(img, (x, y))
                    pygame.draw.rect(win, WHITE, (x, y, CELLSIZE, CELLSIZE), 1)

        if tetris.gameover:
            rect = pygame.Rect(50, 140, width-100, height-350)
            pygame.draw.rect(win, BLACK, rect)
            pygame.draw.rect(win, BLUE, rect, 2)

            over = font2.render('Game Over, Przegrales!', True, WHITE)
            msg1 = font2.render('Nacisnij R aby zrestartowac!', True, WHITE)
            msg2 = font2.render('Nacisnij Q lub ESC aby wyjsc!', True, WHITE)
            msg3 = font2.render('Nacisnij M aby wyjsc do MENU!', True, WHITE)

            win.blit(over, (rect.centerx-over.get_width()//2,  rect.y+20))
            win.blit(msg1, (rect.centerx - msg1.get_width() // 2, rect.y + 80))
            win.blit(msg2, (rect.centerx - msg2.get_width() // 2, rect.y + 100))
            win.blit(msg3, (rect.centerx - msg3.get_width() // 2, rect.y + 120))

        pygame.draw.rect(win, BLUE, (0, height - 120, width, 120))

        if tetris.next_shape:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in tetris.next_shape.image():
                        x = (width + 200) - CELLSIZE * (tetris.next_shape.x + j - 4)
                        y = height - 25 + CELLSIZE * (tetris.next_shape.y + i - 4)
                        img = Pliki[tetris.next_shape.color]
                        win.blit(img, (x, y))

        scoreimg = font.render(f'{tetris.score}', True, WHITE)
        levelimg = font2.render(f'Level: {tetris.level}', True, WHITE)
        autorimg = font2.render(f'Autor: {tetris.autor}', True, WHITE)
        nastepnyimg = font2.render(f'Nastepny Klocek', True, WHITE)
        win.blit(scoreimg, (100 - scoreimg.get_width()//2, height-100))
        win.blit(levelimg, (100 - levelimg.get_width()//2, height-20))
        win.blit(autorimg, (250 - autorimg.get_width() // 2, height - 20))
        win.blit(nastepnyimg, (700 - nastepnyimg.get_width() // 2, height - 20))

        pygame.draw.rect(win, BLUE, (0, 0, width, height), 2)

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()