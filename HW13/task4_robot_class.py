class Robot:
    def __init__(self, orientation, position_x=0, position_y=0):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "up":
            self.position_y += steps
        elif self.orientation == "down":
            self.position_y -= steps
        elif self.orientation == "left":
            self.position_x -= steps
        elif self.orientation == "right":
            self.position_x += steps

    def turn(self, direction):
        if direction == "left":
            if self.orientation == "up":
                self.orientation = "left"
            elif self.orientation == "left":
                self.orientation = "down"
            elif self.orientation == "down":
                self.orientation = "right"
            elif self.orientation == "right":
                self.orientation = "up"
        elif direction == "right":
            if self.orientation == "up":
                self.orientation = "right"
            elif self.orientation == "right":
                self.orientation = "down"
            elif self.orientation == "down":
                self.orientation = "left"
            elif self.orientation == "left":
                self.orientation = "up"

    def display_position(self):
        print(f"Position: ({self.position_x}, {self.position_y})")


# Example usage:
my_robot = Robot("up")

my_robot.move(5)
my_robot.display_position()  # Output: Position: (0, 5)

my_robot.turn("right")

my_robot.move(3)
my_robot.display_position()  # Output: Position: (3, 5)
