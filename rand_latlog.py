import random
import sys
import math

def rand_latlog():
    
    x0 = 12.967267
    y0 = 80.219465

    dec_lat = random.random()/100
    dec_lon = random.random()/100
      
    xLat  = dec_lat + x0
    yLong = dec_lon + y0

    return xLat,yLong



