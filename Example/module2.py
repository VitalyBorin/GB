class Auto:

    count = 0

    def __init__(self, color, engine, doors, clearance, weight, max_speed):
        self.color = color
        self.engine = engine
        self.doors = doors
        self.clearance = clearance
        self.weight = weight
        self.max_speed = max_speed
        self.engine_status = 'stop'
        self.door_status = 'closed'

    def start_engine(self):
        self.engine_status = 'start'

    def stop_engine(self):
        self.engine_status = 'stop'

    def open_doors(self):
        self.door_status = 'open'

    def close_door(self):
        self.door_status = 'close'

lamborghini = Auto('yellow', 700, 2, 'low', 'low', 320)
zaz = Auto('blue', 40, 2, 'middle', 'middle', 70)

print(lamborghini.color)
print(zaz.color)
print(lamborghini.door_status)
print(zaz.door_status)
zaz.open_doors()

print(lamborghini.door_status)
print(zaz.door_status)

