from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ground import Ground
from obstacle import Obstacle
from platformObject import PlatformObject

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

def awake():
  Cursor.enabled = False

def start():
  global player, title
  player = PlatformerController2d(position=(-16, 10, 0), color=color.blue)
  title = Text(text='Welcome To My Game', position=(-0.15, 0.4, 0), color=color.blue)
  invoke(toggle_title, delay=3.5)

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
  on_player_land()
  check_for_collision()
  check_for_win()

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

def on_player_land():
  hit_info = player.intersects()

  if hit_info.entity == platforms[3]: return

  for platform in platforms:
    if hit_info.entity == platform:
      player.grounded = True

def check_for_out_of_bounds():
  if player.x < -16.5:
    player.x = -16.5
  if player.x > 16.5:
    player.x = 16.5

def check_for_collision():
  hit_info = player.intersects()

  for obstacle in obstacles:
    if hit_info.entity == obstacle:
      end_game('You Lost The Game!')

def check_for_win():
  hit_info = player.intersects()

  if hit_info.entity == platforms[3]:
    end_game('You Won The Game!')

def end_game(text):
  toggle_title()
  title.text = text
  player.y += .25
  player.walk_speed = 0

  global isAlive
  isAlive = False

#endregion

if __name__ == '__main__':
  player = None
  isRunning = False
  isAlive = True
  obstacle = Obstacle('brick', (-2,1,0))
  obstacle2 = Obstacle('brick', (3,1,0))
  obstacle3 = Obstacle('brick', (9,1,0))
  obstacles = [obstacle, obstacle2, obstacle3]
  platform = PlatformObject('white_cube', (-5,3,0), color.red)
  platform2 = PlatformObject('white_cube', (0,6,0), color.red)
  platform3 = PlatformObject('white_cube', (5,9,0), color.red)
  final_platform = PlatformObject('white_cube', (10,12,0), color.lime)
  platforms = [platform, platform2, platform3, final_platform]
  Sky()
  awake()
  start()
  app.run()