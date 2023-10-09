class GameObject:
    def __init__(self, pos):
        self.position = pos
        self.components = []
        
    def update(self):
        for component in self.components:
            component.update()
            
    def GetComponent(self, name):
        for component in self.components:
            if component.name == name:
                return component
        return
    
    def AddComponent(self, component):
        self.components.append(component)