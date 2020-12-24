import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('C:\\Users\\alinc\\Desktop\\Alien\\ship.bmp')
        self.song_load = pygame.mixer.music.load('C:\\Users\\alinc\\Desktop\\Alien\\song.wav')
        self.song = pygame.mixer.music.play()
        # self.image = pygame.image.load('C:\\Users\\alinc\\Desktop\\yoda.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
