import pygame

class Character():

    def __init__(self):
        self.avatar = pygame.image.load(r'./assets/racecar.png')
        self.avatar = pygame.transform.scale(self.avatar, (10, 10))
        self.car_width = 8
        self.car_length = 8
        self.crashed = False
        self.experience_points = 0
        # add the init x and init y attributes into this class

    def get_avatar(self):
        return self.avatar

    def transform_avatar(self,tile_size):
        self.avatar = pygame.transform.scale(self.avatar, (tile_size, tile_size))
        self.car_length = tile_size - 3
        self.car_width = tile_size - 3

    def get_avatar_dim(self):
        return (self.car_length,self.car_width)

    def get_state(self):
        return self.crashed

    def set_state(self, crashed):
        self.crashed = crashed

    def reward(self):
        self.experience_points += 1

    def penalize(self):
        self.experience_points -= 5

    def get_exp_points(self):
        return self.experience_points
