from easygopigo3 import EasyGoPiGo3
import time
from math import *

gpg = EasyGoPiGo3()
gpg.init_distance_sensor()
servo = gpg.init_servo()
sensor = gpg.init_distance_sensor()
servo.rotate_servo(90)
print(gpg.volt())
print(gpg.get_speed())

compteur = 0

def avoid_object():
    global compteur
    gpg.orbit(90, 5)
    print("test orbit 1 valide")
    gpg.orbit(-180, 30)
    gpg.orbit(90, 5)
    print("test  orbit 2 valide")
    compteur = 0
    return compteur

def detect_object():
    global compteur,sensor
    if sensor.read_mm() <= 190:
        compteur = 1
        print("test scanner valide")
    else :
        compteur = 0
    return compteur

def avancer():
    global compteur, sensor
    while True:
        if compteur == 0:
            print("test avancement lanc")
            gpg.forward()
            print("test avance valide")
            compteur  = detect_object()
        elif compteur == 1:
            avoid_object()
            print("avitement reussi")


def direction(x,y):
    basse_position_x = 0
    basse_position_y = 0
    delta_x = x - basse_position_x
    delta_y = y - basse_position_y
    angle_radians =  atan2(delta_y ,delta_x)
    degres_angles = angle_radians * 180/pi
    distance = sqrt(delta_x ** 2 + delta_y ** 2)
    print("test rotation vers coodonnes de livraison")
    gpg.turn_degrees(degres_angles)
    print("test rotation vers coodonnees de livraison valide")


if __name__ == "__main__":
    x = 100
    y = 177
    direction(x,y)
    avancer()    