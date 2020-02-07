import pygame
import sys
import random
import time


class Game:
    def __init__(self):
        self.w = 1200
        self.h = 800
        self.white = pygame.Color("white")
        self.red = pygame.Color("red")
        self.black = pygame.Color("black")
        self.sl = 0
        self.sd1 = 1
        self.sd2 = 1
        self.l1 = 1
        self.l2 = 1
        self.r = 99
        self.r1 = 233
        pygame.init()
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Отбитие')
        self.nach()

    def ris(self, *spisok):
        self.display.fill(self.black)
        for x in spisok:
            x.ris(self.display)
        pygame.display.flip()

    def ism(self, *spisok):
        for x in spisok:
            x.ism()

    def check(self, *spisok):
        for x in spisok:
            x.check()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    doska1.n = -(self.sd2 / 10 + 0.8)
                if event.key == ord('w'):
                    doska.n = -(self.sd1 / 10 + 0.8)
                if event.key == pygame.K_DOWN:
                    doska1.n = self.sd2 / 10 + 0.8
                if event.key == ord('s'):
                    doska.n = (self.sd1 / 10 + 0.8)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and doska1.n < 0:
                    doska1.n = 0
                if event.key == pygame.K_DOWN and doska1.n > 0:
                    doska1.n = 0
                if event.key == ord('w') and doska.n < 0:
                    doska.n = 0
                if event.key == ord('s') and doska.n > 0:
                    doska.n = 0

    def game_over(self, a):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 556 <= event.pos[0] <= (556 + 150):
                        if 380 <= event.pos[1] <= 420:
                            self.obnov()
                            self.nach()
                            self.r1 = 10
                            self.r = 0
                            while True:
                                self.cikle()
                        elif 430 <= event.pos[1] <= 470:
                            pygame.quit()
                            sys.exit()
            self.display.fill(self.black)
            win = pygame.font.SysFont('arial', 50)
            shrift = pygame.font.SysFont('arial', 36)
            menu = shrift.render("Menu", True, self.red)
            ex = shrift.render("Exit", True, self.red)
            p = "Score: " + str(ball.s)
            self.r = 1
            score = shrift.render(p, True, self.red)
            pygame.draw.rect(self.display, self.white, (556, 380, 150, 40), 1)
            pygame.draw.rect(self.display, self.white, (556, 430, 150, 40), 1)
            st = "Win " + str(a)
            win1 = win.render(st, True, self.red)
            self.display.blit(win1, (582, 250))
            self.display.blit(menu, (559, 380))
            self.display.blit(ex, (559, 430))
            self.display.blit(score, (582, 310))
            pygame.display.flip()

    def cikle(self):
        game.events()
        game.ism(doska, doska1, ball)
        game.check(doska, doska1, ball)
        game.ris(kosmos, doska, doska1, ball)

    def nach(self):
        kos = Kosmos(self.w, self.h)
        fl = 1
        while fl:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 540 <= event.pos[0] <= 660:
                            if 320 <= event.pos[1] <= 360:
                                fl = 0
                                self.r = 234
                            elif 370 <= event.pos[1] <= 410:
                                self.sl = (self.sl + 1) % 3
                                self.r1 = 234
                            elif 420 <= event.pos[1] <= 460:
                                pygame.quit()
                                sys.exit()
                        elif 230 <= event.pos[0] <= 285 and 30 <= event.pos[1] <= 69:
                            self.sd1 += 1
                            self.r1 = 343
                            if self.sd1 > 9:
                                self.sd1 = 1
                        elif 1122 <= event.pos[0] <= 1177 and 30 <= event.pos[1] <= 69:
                            self.sd2 += 1
                            if self.sd2 > 9:
                                self.sd2 = 1
                        elif 230 <= event.pos[0] <= 285 and 100 <= event.pos[1] <= 139:
                            self.l1 += 1
                            if self.l1 > 9:
                                self.l1 = 1
                        elif 1122 <= event.pos[0] <= 1177 and 100 <= event.pos[1] <= 139:
                            self.l2 += 1
                            if self.l2 > 9:
                                self.l2 = 1
            self.display.fill(self.black)
            kos.ris(self.display)
            for x in range(320, 421, 50):
                pygame.draw.rect(self.display, self.white, (540, x, 120, 40), 1)
            pygame.draw.rect(self.display, self.white, (20, 30, 265, 40), 1)
            pygame.draw.rect(self.display, self.white, (912, 30, 265, 40), 1)
            pygame.draw.line(self.display, self.white, (230, 30), (230, 69))
            pygame.draw.line(self.display, self.white, (1122, 30), (1122, 69))
            pygame.draw.line(self.display, self.white, (230, 100), (230, 139))
            pygame.draw.line(self.display, self.white, (1122, 100), (1122, 139))
            pygame.draw.rect(self.display, self.white, (20, 100, 265, 40), 1)
            pygame.draw.rect(self.display, self.white, (912, 100, 265, 40), 1)
            shrift = pygame.font.SysFont('arial', 36)
            play = shrift.render("Play", True, self.red)
            ex = shrift.render("Exit", True, self.red)
            boardspeed = shrift.render("Board_Speed", True, self.red)
            s1 = shrift.render(str(self.sd1), True, self.red)
            s2 = shrift.render(str(self.sd2), True, self.red)
            life = shrift.render("Number of lives", True, self.red)
            l1 = shrift.render(str(self.l1), True, self.red)
            l2 = shrift.render(str(self.l2), True, self.red)
            if self.sl == 0:
                text = "Easy"
            elif self.sl == 1:
                text = "Normal"
            else:
                text = "Hard"
            slo = shrift.render(text, True, self.red)
            self.display.blit(play, (545, 317))
            self.display.blit(slo, (545, 367))
            self.display.blit(ex, (545, 417))
            self.display.blit(boardspeed, (23, 28))
            self.display.blit(boardspeed, (915, 28))
            self.display.blit(s2, (1125, 28))
            self.display.blit(s1, (235, 28))
            self.display.blit(life, (23, 100))
            self.display.blit(life, (915, 100))
            self.display.blit(l1, (235, 98))
            self.display.blit(l2, (1125, 98))
            pygame.display.flip()

    def obnov(self):
        ball.x = 38
        ball.y = 300
        doska.x = 20
        doska.y = 350
        doska1.x = 1170
        doska1.y = 350
        self.sl = 0
        self.sd1 = 1
        self.sd2 = 1
        self.l1 = 1
        self.l2 = 1
        ball.s = 0


class Doska:
    def __init__(self, x, y):
        self.dlina = 100
        self.shirina = 10
        self.x = x
        self.non = 33
        self.non21 = 32
        self.pope = 1
        self.y = y
        self.n = 0
        self.life = None
        self.white = pygame.Color("white")

    def ris(self, display):
        pygame.draw.rect(display, self.white, (self.x, int(self.y), self.shirina, self.dlina))

    def ism(self):
        self.y += self.n

    def check(self):
        if self.y + self.dlina > game.h:
            self.y = game.h - self.dlina
        elif self.y < 0:
            self.y = 0


class Kosmos:
    def __init__(self, w, h):
        self.kosmos = []
        self.white = pygame.Color("white")
        for x in range(150):
            self.kosmos.append([random.randint(0, w - 1), random.randint(0, h - 1)])

    def ris(self, display):
        for x in self.kosmos:
            pygame.draw.rect(display, self.white, (x[0], x[1], 1, 1))


class Ball:
    def __init__(self):
        self.x = 38
        self.y = 300
        self.r = 8
        self.s = 0
        self.red = pygame.Color("red")
        if game.sl == 0:
            self.skorost = 15
        elif game.sl == 1:
            self.skorost = 11
        else:
            self.skorost = 7
        self.sx = random.randint(4, 10) / self.skorost
        self.sy = random.choice([1, -1]) * random.randint(4, 10) / self.skorost
        self.white = pygame.Color("white")

    def ris(self, display):
        pygame.draw.circle(display, self.white, (int(self.x), int(self.y)), self.r)
        shrift = pygame.font.SysFont('arial', 36)
        score = str(self.s)
        text = shrift.render("Score: " + score, True, self.red)
        display.blit(text, (580, 20))

    def check(self):
        d = [doska.x, doska.y, doska.dlina]
        d1 = [doska1.x, doska1.y, doska1.dlina]
        if int(self.y) + self.r == game.h or int(self.y) - self.r == 0:
            self.sy = -self.sy
        elif int(self.x) + self.r in (d1[0] - 1, d1[0], d1[0] + 1) and d1[1] - 3 <= self.y <= d1[1] + d1[2] + 3:
            self.sx = -random.randint(5, 10) / self.skorost
            self.s += 1
        elif int(self.x) - self.r in (d[0] - 1, d[0], d[0] + 1) and d[1] - 3 <= self.y <= d[1] + d[2] + 3:
            self.sx = random.randint(5, 10) / self.skorost
            self.s += 1
        elif int(self.x) + self.r in (game.w, game.w + 1, game.w - 1, game.w + 2):
            if game.l2 == 1:
                game.game_over(1)
            else:
                game.l2 -= 1
                time.sleep(1)
                self.x = 392
                self.y = 592
        elif int(self.x) - self.r in (-1, 0, 1, -2):
            if game.l1 == 1:
                game.game_over(2)
            else:
                game.l1 -= 1
                time.sleep(1)
                self.x = 392
                self.y = 592

    def ism(self):
        self.x += self.sx
        self.y += self.sy


game = Game()
kosmos = Kosmos(game.w, game.h)
doska = Doska(20, 350)
doska1 = Doska(1170, 350)
ball = Ball()
while True:
    game.cikle()
