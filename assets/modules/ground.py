from ursina import *

class Ground(Entity):
  def __init__(self, position=(Vec3), rotation=(Vec3), scale=(Vec3)):
      super().__init__(
        model='cube',
        parent=scene,
        position=position,
        rotation=rotation,
        scale=scale,
        collider='mesh',
        texture='grass'
      )