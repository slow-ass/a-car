from ursina import *

class CarModel(Entity):
    """
    A procedurally-generated 3D car model using Ursina primitives.
    """
    def __init__(self, car_color=color.red, **kwargs):
        super().__init__(**kwargs)
        
        # Car Body (Chassis)
        self.chassis = Entity(parent=self, model='cube', color=car_color, scale=(1.5, 0.5, 3), y=0.5)
        
        # Cabin (Top part)
        self.cabin = Entity(parent=self.chassis, model='cube', color=car_color, scale=(0.8, 1.2, 0.6), y=0.5, z=-0.2)
        
        # Windows
        self.windshield = Entity(parent=self.cabin, model='cube', color=color.rgb(0, 180, 180), scale=(0.85, 0.75, 1.05), position=(0, 0.1, 0))
        
        # Wheels
        wheel_scale = (0.4, 0.4, 0.4)
        wheel_color = color.black
        
        self.wheels = []
        # Front Left
        self.wheels.append(Entity(parent=self, model='cube', color=wheel_color, scale=wheel_scale, position=(-0.8, 0.2, 1.0), rotation=(0, 0, 90)))
        # Front Right
        self.wheels.append(Entity(parent=self, model='cube', color=wheel_color, scale=wheel_scale, position=(0.8, 0.2, 1.0), rotation=(0, 0, 90)))
        # Back Left
        self.wheels.append(Entity(parent=self, model='cube', color=wheel_color, scale=wheel_scale, position=(-0.8, 0.2, -1.0), rotation=(0, 0, 90)))
        # Back Right
        self.wheels.append(Entity(parent=self, model='cube', color=wheel_color, scale=wheel_scale, position=(0.8, 0.2, -1.0), rotation=(0, 0, 90)))
        
        # Headlights
        self.headlights = []
        self.headlights.append(Entity(parent=self.chassis, model='cube', color=color.yellow, scale=(0.2, 0.2, 0.1), position=(-0.3, 0.0, 1.51)))
        self.headlights.append(Entity(parent=self.chassis, model='cube', color=color.yellow, scale=(0.2, 0.2, 0.1), position=(0.3, 0.0, 1.51)))
        
        # Taillights
        self.taillights = []
        self.taillights.append(Entity(parent=self.chassis, model='cube', color=color.red, scale=(0.2, 0.2, 0.1), position=(-0.3, 0.0, -1.51)))
        self.taillights.append(Entity(parent=self.chassis, model='cube', color=color.red, scale=(0.2, 0.2, 0.1), position=(0.3, 0.0, -1.51)))

    def animate_wheels(self, velocity):
        """
        Simple rotation animation based on velocity.
        """
        for wheel in self.wheels:
            wheel.rotation_z += velocity * 10
