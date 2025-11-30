from ursina import *
from physics import CarPhysics
from assets.car_model import CarModel
from level_manager import LevelManager

class GameController(Entity):
    def __init__(self, car, car_physics, speed_text, **kwargs):
        super().__init__(**kwargs)
        self.car = car
        self.car_physics = car_physics
        self.speed_text = speed_text

    def update(self):
        dt = time.dt
        
        # Input
        throttle = held_keys['w'] or held_keys['up arrow']
        brake = held_keys['s'] or held_keys['down arrow']
        steer = held_keys['d'] - held_keys['a']
        if steer == 0:
            steer = held_keys['right arrow'] - held_keys['left arrow']

        # Physics Update
        velocity, steering_angle = self.car_physics.update(dt, throttle, brake, steer)
        
        # Apply movement
        # Move forward based on rotation
        self.car.position += self.car.forward * velocity * dt
        
        # Rotate car
        self.car.rotation_y += steering_angle
        
        # Wheel animation
        self.car.animate_wheels(velocity)
        
        # Collision check (Simple bounds)
        hit_info = self.car.intersects()
        if hit_info.hit:
            # Bounce back simple
            self.car.position -= self.car.forward * velocity * dt
            self.car_physics.velocity = -self.car_physics.velocity * 0.5

        # Update UI
        self.speed_text.text = f'Speed: {int(self.car_physics.velocity * 10)}'

        # Exit
        if held_keys['escape']:
            application.quit()

def start_game(level='City', car_color='red'):
    """
    Main game function that initializes and runs the Ursina game.
    """
    
    # Initialize Ursina app
    app = Ursina()

    # Window setup
    window.title = "3D Racing Game"
    window.borderless = False
    window.fullscreen = False
    window.exit_button.visible = False

    # Level
    level_manager = LevelManager()
    level_manager.load_level(level)

    # Car color mapping
    car_color_map = {
        'red': color.red,
        'blue': color.blue,
        'green': color.green,
        'yellow': color.yellow,
        'black': color.black,
        'white': color.white
    }
    selected_color = car_color_map.get(car_color, color.red)

    # Car
    car = CarModel(car_color=selected_color)
    car.position = (0, 1, 0)
    car.collider = 'box'  # Simple box collider for the car

    # Physics
    car_physics = CarPhysics()

    # Camera
    camera.parent = car
    camera.position = (0, 10, -20)
    camera.rotation_x = 20

    # UI Overlay
    speed_text = Text(text='Speed: 0', position=(-0.8, 0.45), scale=2, color=color.white)

    # Game Controller (Handles Update Loop)
    game_controller = GameController(car, car_physics, speed_text)

    # Run the game
    app.run()

if __name__ == "__main__":
    # Allow running directly from command line with arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--level', type=str, default='City')
    parser.add_argument('--car_color', type=str, default='red')
    args, unknown = parser.parse_known_args()
    
    start_game(level=args.level, car_color=args.car_color)
