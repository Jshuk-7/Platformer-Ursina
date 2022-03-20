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

pos1 = (0,0,0)
rot1 = (0,0,0)
scale1 = (35, 1, 7)

begging_floor = Ground(pos1, rot1, scale1)

pos2 = (35,0,0)
rot2 = (0,0,0)
scale2 = (35, 1, 7)

second_floor = Ground(pos2, rot2, scale2)

# left edge
PlatformObject('brick', (-18,0,-4), color.white)
PlatformObject('brick', (-18,0,-3), color.white)
PlatformObject('brick', (-18,0,-2), color.white)
PlatformObject('brick', (-18,0,-1), color.white)
PlatformObject('brick', (-18,0,0), color.white)
PlatformObject('brick', (-18,0,1), color.white)
PlatformObject('brick', (-18,0,2), color.white)
PlatformObject('brick', (-18,0,3), color.white)
PlatformObject('brick', (-18,0,4), color.white)

# right edge
PlatformObject('brick', (53,0,-4), color.white)
PlatformObject('brick', (53,0,-3), color.white)
PlatformObject('brick', (53,0,-2), color.white)
PlatformObject('brick', (53,0,-1), color.white)
PlatformObject('brick', (53,0,0), color.white)
PlatformObject('brick', (53,0,1), color.white)
PlatformObject('brick', (53,0,2), color.white)
PlatformObject('brick', (53,0,3), color.white)
PlatformObject('brick', (53,0,4), color.white)

# front edge
PlatformObject('brick', (-17,0,-4), color.white)
PlatformObject('brick', (-16,0,-4), color.white)
PlatformObject('brick', (-15,0,-4), color.white)
PlatformObject('brick', (-14,0,-4), color.white)
PlatformObject('brick', (-13,0,-4), color.white)
PlatformObject('brick', (-12,0,-4), color.white)
PlatformObject('brick', (-11,0,-4), color.white)
PlatformObject('brick', (-10,0,-4), color.white)
PlatformObject('brick', (-9,0,-4), color.white)
PlatformObject('brick', (-8,0,-4), color.white)
PlatformObject('brick', (-7,0,-4), color.white)
PlatformObject('brick', (-6,0,-4), color.white)
PlatformObject('brick', (-5,0,-4), color.white)
PlatformObject('brick', (-4,0,-4), color.white)
PlatformObject('brick', (-3,0,-4), color.white)
PlatformObject('brick', (-2,0,-4), color.white)
PlatformObject('brick', (-1,0,-4), color.white)
PlatformObject('brick', (0,0,-4), color.white)
PlatformObject('brick', (1,0,-4), color.white)
PlatformObject('brick', (2,0,-4), color.white)
PlatformObject('brick', (3,0,-4), color.white)
PlatformObject('brick', (4,0,-4), color.white)
PlatformObject('brick', (5,0,-4), color.white)
PlatformObject('brick', (6,0,-4), color.white)
PlatformObject('brick', (7,0,-4), color.white)
PlatformObject('brick', (8,0,-4), color.white)
PlatformObject('brick', (9,0,-4), color.white)
PlatformObject('brick', (10,0,-4), color.white)
PlatformObject('brick', (11,0,-4), color.white)
PlatformObject('brick', (12,0,-4), color.white)
PlatformObject('brick', (13,0,-4), color.white)
PlatformObject('brick', (14,0,-4), color.white)
PlatformObject('brick', (15,0,-4), color.white)
PlatformObject('brick', (16,0,-4), color.white)
PlatformObject('brick', (17,0,-4), color.white)
PlatformObject('brick', (18,0,-4), color.white)
PlatformObject('brick', (19,0,-4), color.white)
PlatformObject('brick', (20,0,-4), color.white)
PlatformObject('brick', (21,0,-4), color.white)
PlatformObject('brick', (22,0,-4), color.white)
PlatformObject('brick', (23,0,-4), color.white)
PlatformObject('brick', (24,0,-4), color.white)
PlatformObject('brick', (25,0,-4), color.white)
PlatformObject('brick', (26,0,-4), color.white)
PlatformObject('brick', (27,0,-4), color.white)
PlatformObject('brick', (28,0,-4), color.white)
PlatformObject('brick', (29,0,-4), color.white)
PlatformObject('brick', (30,0,-4), color.white)
PlatformObject('brick', (31,0,-4), color.white)
PlatformObject('brick', (32,0,-4), color.white)
PlatformObject('brick', (33,0,-4), color.white)
PlatformObject('brick', (34,0,-4), color.white)
PlatformObject('brick', (35,0,-4), color.white)
PlatformObject('brick', (36,0,-4), color.white)
PlatformObject('brick', (37,0,-4), color.white)
PlatformObject('brick', (38,0,-4), color.white)
PlatformObject('brick', (39,0,-4), color.white)
PlatformObject('brick', (40,0,-4), color.white)
PlatformObject('brick', (41,0,-4), color.white)
PlatformObject('brick', (42,0,-4), color.white)
PlatformObject('brick', (43,0,-4), color.white)
PlatformObject('brick', (44,0,-4), color.white)
PlatformObject('brick', (45,0,-4), color.white)
PlatformObject('brick', (46,0,-4), color.white)
PlatformObject('brick', (47,0,-4), color.white)
PlatformObject('brick', (48,0,-4), color.white)
PlatformObject('brick', (49,0,-4), color.white)
PlatformObject('brick', (50,0,-4), color.white)
PlatformObject('brick', (51,0,-4), color.white)
PlatformObject('brick', (52,0,-4), color.white)

# back edge
PlatformObject('brick', (-17,0,4), color.white)
PlatformObject('brick', (-16,0,4), color.white)
PlatformObject('brick', (-15,0,4), color.white)
PlatformObject('brick', (-14,0,4), color.white)
PlatformObject('brick', (-13,0,4), color.white)
PlatformObject('brick', (-12,0,4), color.white)
PlatformObject('brick', (-11,0,4), color.white)
PlatformObject('brick', (-10,0,4), color.white)
PlatformObject('brick', (-9,0,4), color.white)
PlatformObject('brick', (-8,0,4), color.white)
PlatformObject('brick', (-7,0,4), color.white)
PlatformObject('brick', (-6,0,4), color.white)
PlatformObject('brick', (-5,0,4), color.white)
PlatformObject('brick', (-4,0,4), color.white)
PlatformObject('brick', (-3,0,4), color.white)
PlatformObject('brick', (-2,0,4), color.white)
PlatformObject('brick', (-1,0,4), color.white)
PlatformObject('brick', (0,0,4), color.white)
PlatformObject('brick', (1,0,4), color.white)
PlatformObject('brick', (2,0,4), color.white)
PlatformObject('brick', (3,0,4), color.white)
PlatformObject('brick', (4,0,4), color.white)
PlatformObject('brick', (5,0,4), color.white)
PlatformObject('brick', (6,0,4), color.white)
PlatformObject('brick', (7,0,4), color.white)
PlatformObject('brick', (8,0,4), color.white)
PlatformObject('brick', (9,0,4), color.white)
PlatformObject('brick', (10,0,4), color.white)
PlatformObject('brick', (11,0,4), color.white)
PlatformObject('brick', (12,0,4), color.white)
PlatformObject('brick', (13,0,4), color.white)
PlatformObject('brick', (14,0,4), color.white)
PlatformObject('brick', (15,0,4), color.white)
PlatformObject('brick', (16,0,4), color.white)
PlatformObject('brick', (17,0,4), color.white)
PlatformObject('brick', (18,0,4), color.white)
PlatformObject('brick', (19,0,4), color.white)
PlatformObject('brick', (20,0,4), color.white)
PlatformObject('brick', (21,0,4), color.white)
PlatformObject('brick', (22,0,4), color.white)
PlatformObject('brick', (23,0,4), color.white)
PlatformObject('brick', (24,0,4), color.white)
PlatformObject('brick', (25,0,4), color.white)
PlatformObject('brick', (26,0,4), color.white)
PlatformObject('brick', (27,0,4), color.white)
PlatformObject('brick', (28,0,4), color.white)
PlatformObject('brick', (29,0,4), color.white)
PlatformObject('brick', (30,0,4), color.white)
PlatformObject('brick', (31,0,4), color.white)
PlatformObject('brick', (32,0,4), color.white)
PlatformObject('brick', (33,0,4), color.white)
PlatformObject('brick', (34,0,4), color.white)
PlatformObject('brick', (35,0,4), color.white)
PlatformObject('brick', (36,0,4), color.white)
PlatformObject('brick', (37,0,4), color.white)
PlatformObject('brick', (38,0,4), color.white)
PlatformObject('brick', (39,0,4), color.white)
PlatformObject('brick', (40,0,4), color.white)
PlatformObject('brick', (41,0,4), color.white)
PlatformObject('brick', (42,0,4), color.white)
PlatformObject('brick', (43,0,4), color.white)
PlatformObject('brick', (44,0,4), color.white)
PlatformObject('brick', (45,0,4), color.white)
PlatformObject('brick', (46,0,4), color.white)
PlatformObject('brick', (47,0,4), color.white)
PlatformObject('brick', (48,0,4), color.white)
PlatformObject('brick', (49,0,4), color.white)
PlatformObject('brick', (50,0,4), color.white)
PlatformObject('brick', (51,0,4), color.white)
PlatformObject('brick', (52,0,4), color.white)

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
  camera.x = player.x
  camera.y = player.y + 30

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

  if hit_info.entity == platforms[-1]: return

  for platform in platforms:
    if hit_info.entity == platform:
      player.grounded = True

def check_for_out_of_bounds():
  if player.x < -16.5:
    player.x = -16.5
  if player.x > 51.5:
    player.x = 51.5

def check_for_collision():
  hit_info = player.intersects()

  for obstacle in obstacles:
    if hit_info.entity == obstacle:
      end_game('You Lost The Game!')

def check_for_win():
  hit_info = player.intersects()

  if hit_info.entity == platforms[-1]:
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
  obstacle4 = Obstacle('brick', (15,1,0))
  obstacles = [obstacle, obstacle2, obstacle3, obstacle4]
  platform = PlatformObject('white_cube', (-5,3,0), color.red)
  platform2 = PlatformObject('white_cube', (0,6,0), color.red)
  platform3 = PlatformObject('white_cube', (5,9,0), color.red)
  platform4 = PlatformObject('white_cube', (10,12,0), color.red)
  platform5 = PlatformObject('white_cube', (15,15,0), color.red)
  platform6 = PlatformObject('white_cube', (20,18,0), color.red)
  platform7 = PlatformObject('white_cube', (25,21,0), color.red)
  platform8 = PlatformObject('white_cube', (30,24,0), color.red)
  platform9 = PlatformObject('white_cube', (35,27,0), color.red)
  platform10 = PlatformObject('white_cube', (40,30,0), color.red)
  final_platform = PlatformObject('white_cube', (45,33,0), color.lime)
  platforms = [platform, platform2, platform3, platform4, platform5, platform6, platform7, platform8, platform9, platform10, final_platform]
  Sky()
  awake()
  start()
  app.run()