import assets/index as assets
import simplegui
import math
import random

def get_asset(name):
  return assets.get(name)


BULLET_SPEED=0
asteroid_list=[]
bullet_list=[]

class ship:
  def __init__(self, pos):
    self.pos=pos
    self.vel=[0, 0]
    
  def get_pos(self):
    return self.pos
 
  def get_vel(self):
    return self.vel

  def move(self):
    self.pos[0]+=self.vel[0]
    self.pos[1]+=self.vel[1]

   def accelerate(self, new_vel):
    self.vel=new_vel
        
class asteroid:
  def __init__(self, pos, size, speed):
    self.pos=pos
    self.size=size
    self.speed=speed
   
  def get_pos(self):
    return self.pos
  
  def get_size(self):
    return self.size
  
  def get_speed(self):
    return self.speed
  
  def update(self):
    self.size+=self.speed

    
class bullet:
  def __init__(self, pos, size):
    self.pos=pos
    self.size=size
  
  def get_pos(self):
    return self.pos
  
  def get_size(self):
    return self.size
  
  def update(self):
    self.size-=BULLET_SPEED
  
  
def create_asteroid():
  pos0=random.randint(1, 500)
  pos1=random.randint(1, 500)
  pos=[pos0, pos1]
  size=random.randint(10, 100)
  speed=random.randint(1, 10)
  a=asteroid(pos, size, speed)
  asteroid_list.append(a)

def shoot(pos):
  b=bullet(pos, 5)
  bullet_list.append(b)
  
def player_asteroid_collision(player):
  pos=player.get_pos()
  for a in asteroid_list:
    if a.get_pos==pos:
      return True
  return False

def bullet_asteroid_collision():
  global asteroid_list
  global bullet_list
  shot_asteroids=[]
  used_bullets=[]
  for a in asteroid_list:
    for b in bullet_list:
      if a.get_pos()=b.get_pos():
        shot_asteroid.append(a)
        used_bullets.append(b)
   for x in shot_asteroids:
    asteroid_list.remove(x)
   for y in used_bullets:
    bullet_list.remove(y)
  
  
  
  
  
  
  
  
    
  
