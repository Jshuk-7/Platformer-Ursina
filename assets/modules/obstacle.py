from ursina import *

class Obstacle(Entity):
  def __init__(self, texture, position=(Vec3)):
      super().__init__(
        model='cube',
        collider='box',
        parent=scene,
        texture=texture,
        position=position,
        scale=1.5
      )