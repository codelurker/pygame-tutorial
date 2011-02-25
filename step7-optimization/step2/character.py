import pygame
from animation import Animation, Frame
from time import time

class Character(pygame.sprite.Sprite):

  def __init__(self, screen_w, screen_h, unit):
    super(Character, self).__init__()
    self.unit = unit
    self.layer = 1
    self.create_animations()
    self.current_animation = self.left_animation
    image_rect = self.current_animation.get_current_frame().image.get_rect()
    self.center = image_rect.width/2
    self.position = [(screen_w - image_rect.width)/2, screen_h - image_rect.height]
    self.current_animation.update_sprite(self, self.position)
    size_reduction = 10*unit
    self.collision_rect = pygame.Rect(image_rect.left + size_reduction, image_rect.top + size_reduction,
                                      image_rect.width - 2*size_reduction, 
                                      image_rect.height - 4*size_reduction)
    self.screen_w = screen_w
    self.direction = [0, 0]
    self.start_time = time()
    
  def create_animations(self):
    left = pygame.image.load("assets/character.png").convert_alpha()
    right = pygame.transform.flip(left, True, False)
    self.left_animation = Animation([
      Frame(left, [0, 4*self.unit], 4), 
      Frame(left, [0, 0], 4) 
      ])
    self.right_animation = Animation([
      Frame(right, [0, 4*self.unit], 4),
      Frame(right, [0, 0], 4)
      ])
    
  def input(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        self.direction[0] = -1
        self.current_animation = self.left_animation
      elif event.key == pygame.K_RIGHT:
        self.direction[0] = 1
        self.current_animation = self.right_animation
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT and self.direction[0] == -1) or\
        (event.key == pygame.K_RIGHT and self.direction[0] == 1):
        self.direction[0] = 0
  
  def update(self):
    if self.direction[0] != 0:
      self.current_animation.update()  
    self.position[0] = (self.position[0] + self.direction[0]*8*self.unit + self.center)%self.screen_w - self.center
    self.current_animation.update_sprite(self, self.position)
   
  def collides_with(self, other):
    return self.get_absolute_rect().colliderect(other.get_absolute_rect())
  
  def get_absolute_rect(self):
    return self.collision_rect.move(self.position)
