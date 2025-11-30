import math

class CarPhysics:
    def __init__(self, max_speed=30, acceleration=10, friction=0.5, turn_speed=2):
        self.velocity = 0
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.friction = friction
        self.turn_speed = turn_speed
        self.steering_angle = 0
        self.drift_factor = 0.9  # 1.0 = no drift, lower = more drift

    def update(self, dt, throttle, brake, steer_input):
        # Acceleration
        if throttle:
            self.velocity += self.acceleration * dt
        elif brake:
            self.velocity -= self.acceleration * 1.5 * dt
        else:
            # Friction
            if abs(self.velocity) < 0.1:
                self.velocity = 0
            else:
                self.velocity -= math.copysign(self.friction * dt, self.velocity)

        # Cap speed
        self.velocity = max(min(self.velocity, self.max_speed), -self.max_speed / 2)

        # Steering
        # Steering is more effective when moving, but not at 0 speed
        if self.velocity != 0:
            turn_amount = steer_input * self.turn_speed * dt * (self.velocity / self.max_speed)
            # Reverse steering when going backward
            if self.velocity < 0:
                turn_amount = -turn_amount
            self.steering_angle += turn_amount
        
        # Return the movement vector (forward) and rotation change
        # In a real physics engine, we'd calculate force vectors.
        # Here we return simple scalar updates for the Entity to apply.
        return self.velocity, self.steering_angle
