#1. Define the North boundary
#2. Define the South boundary
#3. Define the West Boundar
#4. Define the East Boundary

# Boundaries defined using an imaginary integer but the same principle of the cartesian plane

NORTH_BOUNDARY = 100
SOUTH_BOUNDARY = -100
WEST_BOUNDARY = -100
EAST_BOUNDARY = 100
direction = None
BULLETS = 'infinite'
TARGETS = 3
DIRECTIONS = ['N', 'S', 'E', 'W', 'NORTH', 'SOUTH', 'EAST', 'WEST']
GAME_ENDS = False


#Define a player class

class Player:
  def __init__(self, name, position, action):
    self.name = name 
    self.lives = lives
    self.position = position
    self.action = action

  #move Player
  def move(self):
    direction = print('Which direction do you want to go to?')
    if direction.lower() == 'North':
      self.position += 10
      # more contro;l flow here

  #shoot
  def shoot(self):
    if NORTH_BOUNDARY != '':
      #there is a target there
      self.action = 'shoot'
      #one target down
      TARGETS = TARGETS - 1
    else:
      #no target there
      movement = print('Where do you want to move? N, S, W ,E')
      if movement.lower() in DIRECTIONS:
       if movement.lower() == 'N':
         self.position += 10
         NORTH_BOUNDARY -= 10
         SOUTH_BOUNDARY += 10
       elif movement.lower() == 'S':
        #player is going down and player can only go down max of 3 steps - need to write this logic
         self.position -= 10
         NORTH_BOUNDARY += 10
         SOUTH_BOUNDARY -= 10
       else:
         print('Please enter a valid direction')
    
  #action method
  def get_action(self):
    if self.position < NORTH_BOUNDARY and self.position > SOUTH_BOUNDARY:
      direction = self.move()
    elif self.position > NORTH_BOUNDARY:
      #impossible
      GAME_ENDS = True
    else:
      direction


lare = Player('Lare', 20, 'shoot')