from pyautogui import *
import pyautogui
import keyboard
import win32api, win32con
import time

#Tiles
#black rgb 17
#Y-Corr = 729
#X-Corr diff = 126

# name, x-corr, y-corr
tile_position = [
    [
        'Tile_1', 434, 838
    ],
    [
        'Tile_2', 560, 838
    ],
    [
        'Tile_3', 686, 838
    ],
    [
        'Tile_4', 812, 838
    ]    
]


#click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001) #This is the pause in between clicks
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Fail Safe
while keyboard.is_pressed('down') == False:
    
    if pyautogui.pixel(tile_position[0][1], tile_position[0][2])[0] == 17:
        click(tile_position[0][1], tile_position[0][2])
        
    if pyautogui.pixel(tile_position[1][1], tile_position[1][2])[0] == 17:
        click(tile_position[1][1], tile_position[1][2])
     
    if pyautogui.pixel(tile_position[2][1], tile_position[2][2])[0] == 17:
        click(tile_position[2][1], tile_position[2][2])
     
    if pyautogui.pixel(tile_position[3][1], tile_position[3][2])[0] == 17:
        click(tile_position[3][1], tile_position[3][2])
        
