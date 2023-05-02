import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32) # 背景色
BG_COLOR = (24, 89, 117)

SPRITE_DIR_PATH = 'sprites'

FONT_PATH = 'font/SFPixelateShaded-Bold.ttf'

ANIM_TIME_INTERVAL = 200 # milliseconds 
FAST_ANIM_TIME_INTERVAL = 15

TILE_SIZE = 40 # 每格長度
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20 # 長、寬幾格
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0) #設定初始位置
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINO = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

COLORS = {
    'black': (0,0,0),
    'red': (255,0,0),
    'blue': (0,0,255),
    'green': (0,255,0),
    'yellow': (0, 255, 255),
    'orange': (255, 255, 0),
    'sliver': (192, 192, 192)
}