import assets/index as assets
import simplegui
import math

def get_asset(name):
  return assets.get(name)


BULLET_SPEED=0

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
  
  
  
  
  
  
  
  
  
  
  
    
  
