from ursina import *
from math import sin, cos, radians     

app = Ursina()

# --- Environment ---
ground = Entity(
    model='plane',
    scale=(1000, 1, 1000),
    color=color.lime.tint(-.5),
    texture='white_cube',
    texture_scale=(1000, 1000),
    collider='box'
)

Sky()

# --- Car ---
car = Entity(
    model='cube',
    color=color.red,
    scale=(2, 1, 3.5),
    position=(0, 1, 0),
    collider='box'
)

speed = 20
turn_speed = 100

def update():
    # Steering
    rotation_input = held_keys['d'] - held_keys['a']
    car.rotation_y += rotation_input * turn_speed * time.dt

    # Movement
    direction = held_keys['w'] - held_keys['s']
    if direction != 0:
        car.position += car.forward * direction * speed * time.dt

    # ------- Camera Logic Fix ---------
    # Stable backward direction (no tilt)
    back_vector = Vec3(
        -sin(radians(car.rotation_y)),
        0,
        -cos(radians(car.rotation_y))
    )

    target_pos = car.position + (back_vector * 12) + Vec3(0, 6, 0)
    camera.position = lerp(camera.position, target_pos, time.dt * 5)

    # Prevent camera going under ground
    camera.y = max(camera.y, 2)

    camera.look_at(car)

app.run()
