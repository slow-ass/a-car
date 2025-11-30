from ursina import *

class LevelManager:
    def __init__(self):
        self.ground = None
        self.walls = []
        self.finish_line = None

    def load_level(self, level_name):
        self.clear_level()
        
        if level_name == "City":
            self.create_city_level()
        elif level_name == "Desert":
            self.create_desert_level()
        elif level_name == "Night":
            self.create_night_level()
        else:
            self.create_city_level()  # Default

    def clear_level(self):
        if self.ground:
            destroy(self.ground)
        for wall in self.walls:
            destroy(wall)
        self.walls = []
        if self.finish_line:
            destroy(self.finish_line)

    def create_city_level(self):
        # Simple City: Gray road, buildings around
        self.ground = Entity(model='plane', scale=(100, 1, 100), color=color.gray, texture='white_cube', texture_scale=(10,10), collider='box')
        
        # Buildings (Walls)
        # Outer walls
        self.walls.append(Entity(model='cube', scale=(100, 10, 1), position=(0, 5, 50), color=color.dark_gray, collider='box'))
        self.walls.append(Entity(model='cube', scale=(100, 10, 1), position=(0, 5, -50), color=color.dark_gray, collider='box'))
        self.walls.append(Entity(model='cube', scale=(1, 10, 100), position=(50, 5, 0), color=color.dark_gray, collider='box'))
        self.walls.append(Entity(model='cube', scale=(1, 10, 100), position=(-50, 5, 0), color=color.dark_gray, collider='box'))
        
        # Obstacles (Buildings)
        self.walls.append(Entity(model='cube', scale=(10, 5, 10), position=(20, 2.5, 20), color=color.brown, collider='box'))
        self.walls.append(Entity(model='cube', scale=(10, 5, 10), position=(-20, 2.5, -20), color=color.orange, collider='box'))
        self.walls.append(Entity(model='cube', scale=(8, 7, 8), position=(30, 3.5, -25), color=color.gray, collider='box'))
        self.walls.append(Entity(model='cube', scale=(12, 6, 12), position=(-30, 3, 15), color=color.dark_gray, collider='box'))

        # Sky
        Sky()

    def create_desert_level(self):
        # Desert: Orange ground, few rocks
        self.ground = Entity(model='plane', scale=(200, 1, 200), color=color.orange, texture='white_cube', texture_scale=(20,20), collider='box')
        
        # Rocks
        import random
        random.seed(42)  # For consistency
        for i in range(15):
            x = random.randint(-80, 80)
            z = random.randint(-80, 80)
            s = random.randint(2, 5)
            self.walls.append(Entity(model='sphere', scale=s, position=(x, s/2, z), color=color.brown, collider='box'))
            
        Sky(texture='sky_sunset')

    def create_night_level(self):
        # Night: Dark ground, neon walls
        self.ground = Entity(model='plane', scale=(100, 1, 100), color=color.rgb(20, 20, 30), collider='box')
        
        # Neon Walls
        self.walls.append(Entity(model='cube', scale=(100, 2, 1), position=(0, 1, 50), color=color.rgb(0, 255, 255), collider='box'))
        self.walls.append(Entity(model='cube', scale=(100, 2, 1), position=(0, 1, -50), color=color.rgb(255, 0, 255), collider='box'))
        self.walls.append(Entity(model='cube', scale=(1, 2, 100), position=(50, 1, 0), color=color.rgb(0, 255, 0), collider='box'))
        self.walls.append(Entity(model='cube', scale=(1, 2, 100), position=(-50, 1, 0), color=color.yellow, collider='box'))
        
        # Obstacles in neon colors
        self.walls.append(Entity(model='cube', scale=(8, 3, 8), position=(15, 1.5, 15), color=color.rgb(255, 192, 203), collider='box'))
        self.walls.append(Entity(model='cube', scale=(8, 3, 8), position=(-15, 1.5, -15), color=color.rgb(238, 130, 238), collider='box'))
        
        Sky(color=color.rgb(10, 10, 20))
