
#Renderer.py

from tracemalloc import start
from pygame.draw import line
import settings as st
import Camera as cam
import FOV as fov
import pygame as pg

halfOfWidth = st.width / 2
halfOfHeight = st.height / 2

cam = cam.Camera(0, 0, -1)
#fov = fov.FOV(0, 0, 0, 2)

def RenderVertex(screen, vertex):
    xDistanceToCamera = None
    zDistanceToCamera = None
    yDistanceToCamera = None
    vertexOnScreenRatioX = None
    vertexOnScreenRatioY = None
    vertexXPositionOnScreen = None
    vertexYPositionOnScreen = None
    

    xDistanceToCamera = abs(cam.x) + abs(vertex.x)
    yDistanceToCamera = abs(cam.y) + abs(vertex.y)
    zDistanceToCamera = abs(cam.z) + abs(vertex.z)

    vertexOnScreenRatioX = xDistanceToCamera / zDistanceToCamera
    vertexOnScreenRatioY = yDistanceToCamera / zDistanceToCamera   

    if vertex.x >= 0:       
        vertexXPositionOnScreen = halfOfWidth - (halfOfWidth * vertexOnScreenRatioX)
    else:
        vertexXPositionOnScreen = halfOfWidth + (halfOfWidth * vertexOnScreenRatioX)
    
    if vertex.y >= 0:
        vertexYPositionOnScreen = halfOfHeight - (halfOfHeight * vertexOnScreenRatioY)
    else:
        vertexYPositionOnScreen = halfOfHeight + (halfOfHeight * vertexOnScreenRatioY)


    pg.draw.rect(screen, (255, 255, 255), (vertexXPositionOnScreen - 1, vertexYPositionOnScreen - 1, 3, 3))
    
    vertex.screenXPosition = vertexXPositionOnScreen
    vertex.screenYPosition = vertexYPositionOnScreen
    
def RenderLine(screen, lineCoorInfo, VertexTable):
    startVertexIndex = lineCoorInfo[0]
    endVertexIndex = lineCoorInfo[1]    
    startXPosition = VertexTable[startVertexIndex].screenXPosition
    startYPosition = VertexTable[startVertexIndex].screenYPosition
    endXPosition = VertexTable[endVertexIndex].screenXPosition
    endYPosition = VertexTable[endVertexIndex].screenYPosition
    startPosition = (startXPosition, startYPosition)
    endPosition = (endXPosition, endYPosition)

    pg.draw.line(screen, (255, 255, 255), startPosition, endPosition)
   