# drone_management.py

class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def device_info(self):
        print(f"Device ID: {self.device_id}, Model: {self.model}")

class Flyer:
    def fly(self):
        print("The drone is flying.")

class Drone(Device, Flyer):
    def capture_image(self):
        print("Drone captured an image.")

# Testing all functionalities
if __name__ == "__main__":
    drone1 = Drone("D001", "Phantom-X")
    drone1.device_info()
    drone1.fly()
    drone1.capture_image()
