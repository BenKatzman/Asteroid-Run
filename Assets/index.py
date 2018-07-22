import sys

def get(img):
  try:
    return open(img, 'r')
  except:
    return open('error.png', 'r')    
    
