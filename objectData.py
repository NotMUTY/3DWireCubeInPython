
#objectData.py

import Vertex as ve

table = [
    ve.Vertex(-1, -1, 1), #sol on alt 0
    ve.Vertex(1, -1, 1),  #sağ on alt 1
    ve.Vertex(-1, -1, 3), #sol arka alt 2
    ve.Vertex(1, -1, 3),  #sağ arka alt 3
    ve.Vertex(-1, 1, 1),  #sol on ust 4
    ve.Vertex(1, 1, 1),   #sağ on ust 5
    ve.Vertex(-1, 1, 3),  #sol arka ust 6
    ve.Vertex(1, 1, 3)    #sağ arka ust 7
]

lineTable = [
    [0, 1],     
    [1, 3],
    [3, 2],
    [2, 0],

    [4, 5],
    [5, 7],
    [7, 6],
    [6, 4],
    
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]


