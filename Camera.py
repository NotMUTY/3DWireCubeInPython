
#Camera.pu
import FOV as f

class Camera():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.fov = f.FOV(x, y, z, 2)
