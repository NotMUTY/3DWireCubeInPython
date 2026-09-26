import pygame as pg
import settings as st
import sys

screen = pg.display.set_mode(st.res)
    

clock = pg.time.Clock()
while True:
    screen.fill((255, 255, 255))    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            pg.quit
            break
    
    pg.display.set_caption(str(round(clock.get_fps(), 2)))
    clock.tick(24)
    pg.display.update()
