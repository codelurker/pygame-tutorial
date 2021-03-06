import pygame
from random import randint

fallers_size = 6
fallers = ["assets/faller_%03d.png" % faller_number for faller_number in xrange(1, fallers_size + 1) ]

class FallingObject(pygame.sprite.Sprite):

  def __init__(self, screen_w, screen_h, unit):
    super(FallingObject, self).__init__()
    self.unit = unit
    self.layer = 2
    self.image = pygame.image.load(fallers[randint(0, fallers_size - 1)]).convert_alpha()
    image_rect = self.image.get_rect()
    # This collision object will be positioned relative to the position
    # of the object
    size_reduction = 20*unit
    self.collision_rect = pygame.Rect(image_rect.left + size_reduction, image_rect.top + size_reduction,
                                      image_rect.width - 2*size_reduction, image_rect.height - 2*size_reduction)
    # Begin with a random horizontal position and at the top
    self.position = [randint(0, screen_w - image_rect.width), -image_rect.height]
    self.screen_h = screen_h
    self.rect = image_rect.move(self.position)
    
  def update(self):
    self.position[1] += 4*self.unit;
    self.rect = self.image.get_rect().move(self.position)
  
  def died(self):
    return self.position[1] > self.screen_h
  
  def get_absolute_rect(self):
    return self.collision_rect.move(self.position)
