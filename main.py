from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ground import Ground
from obstacle import Obstacle

app = Ursina()

#region Window & Camera

window.fullscreen = True

camera.y += 30
camera.z -= 30
camera.rotation_x = 25

#endregion

#region Ground

pos = (0,0,0)
rot = (0,0,0)
scale = (35, 1, 7)

groundInfo = [pos, rot, scale]

Ground(groundInfo[0], groundInfo[1], groundInfo[2])

#endregion

#region Gameloop

def start():
  Cursor.enabled = False
  global player, title
  player = PlatformerController2d(position=(-16, 10, 0), color=color.blue)
  title = Text(text='Welcome To My Game', position=(-0.15, 0.4, 0), color=color.blue)
  invoke(toggle_title, delay=5)

def input(key):
  if key == Keys.escape:
    quit()

  global isRunning
  if key == Keys.left_shift:
    isRunning = True
  if key == Keys.left_shift_up:
    isRunning = False

  if isAlive: return
  if key == 'space':
    player.grounded = False

def update():
  if not isAlive: return
  check_for_out_of_bounds()
  set_player_speed()
  check_for_collision()

#endregion

#region Helper Methods

def toggle_title():
  if title.enabled:
    title.enabled = False
  elif not title.enabled:
    title.enabled = True

def set_player_speed():
  global isRunning
  if isRunning:
    player.walk_speed = 12
  elif not isRunning:
    player.walk_speed = 8

def check_for_out_of_bounds():
  if player.x < -16.5:
    player.x = -16.5
  if player.x > 16.5:
    player.x = 16.5

def check_for_collision():
  hit_info = player.intersects()

  for obstacle in obstacles:
    if hit_info.entity == obstacle:
      toggle_title()
      title.text = 'You Lost The Game!'
      player.y += .25
      player.walk_speed = 0

      global isAlive
      isAlive = False

#endregion

if __name__ == '__main__':
  player = None
  isRunning = False
  isAlive = True
  obstacle = Obstacle('brick', (0,1,0))
  obstacle2 = Obstacle('brick', (8,1,0))
  obstacles = [obstacle, obstacle2]
  Sky()
  start()
  app.run()