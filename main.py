
#Main.py

import pygame as pg
import settings as st
import Renderer as rd
import objectData as vt

pg.init()

screen = pg.display.set_mode(st.res)
font = pg.font.SysFont("consolas", 16)

FPS = 360
frameCount = 0
Clock = pg.time.Clock()

while True:

    if frameCount == 0:
        fpsText = font.render(f"Fps: {round(Clock.get_fps(), 1)}", True, (100, 100, 100))
        
    screen.blit(fpsText, (15, 10))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break

    speed = 1.2 * st.deltatime
    keys = pg.key.get_pressed()
    for vertex in vt.table:
        if keys[pg.K_w]:
            vertex.y += speed
        
        if keys[pg.K_s]:
            vertex.y -= speed
        
        if keys[pg.K_a]:
            vertex.x += speed           

        if keys[pg.K_d]:
            vertex.x -= speed
        
        if keys[pg.K_UP]:
            rd.cam.y += speed
        
        if keys[pg.K_DOWN]:
            rd.cam.y -= speed
            
        if keys[pg.K_LEFT]:
            rd.cam.x -= speed

        if keys[pg.K_RIGHT]:
            rd.cam.x += speed


    anyFps = Clock.get_fps()

    if anyFps:
        st.deltatime = 1 / anyFps

    Clock.tick(FPS) 

    pg.display.set_caption(str(anyFps))
    screen.fill((0, 0, 0))   

    frameCount += 1

    if frameCount == 360:
        frameCount = 0

    for vertex in vt.table:
        rd.RenderVertex(screen=screen, vertex=vertex)

    for line in vt.lineTable:
        rd.RenderLine(screen=screen, lineCoorInfo=line, VertexTable=vt.table)

    pg.display.update()
    