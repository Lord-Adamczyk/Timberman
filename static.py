from pgzero.builtins import Actor,keyboard;
from pgzero.screen import Screen;
import pgzrun; 
import pygame
screen:Screen
keys:keyboard

FULLSCREEN =False
WIDTH=800
HEIGHT=600
BASE_WIDTH=1920
BASE_HEIGHT=1080
FULLSCREEN_WIDTH=1920
FULLSCREEN_HEIGHT=1080
def zmienFullscreen():
    global FULLSCREEN
    FULLSCREEN=not FULLSCREEN
def czyFullscreen():
    return FULLSCREEN
tlo=Actor('tlo',pos=(0,0),anchor=(0,0))