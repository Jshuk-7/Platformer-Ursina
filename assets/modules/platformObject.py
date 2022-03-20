from ursina import *

class PlatformObject(Entity):
  def __init__(self, texture, position=(Vec3), color=()):
      super().__init__(
        model='cube',
        collider='box',
        parent=scene,
        texture=texture,
        position=position,
        color=color
      )