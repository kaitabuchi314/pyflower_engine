class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        self.x += other.x
        self.y += other.y
        
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
    
    def div(self, other):
        self.x /= other.x
        self.y /= other.y
    
    def mult(self, other):
        self.x *= other.x
        self.y *= other.y