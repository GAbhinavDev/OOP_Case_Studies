# drone_management.py

class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def info(self):
        print(f"Device ID: {self.device_id}")

class Flyer:
    def fly(self):
        print("Drone is flying...")

class Drone(Device, Flyer):
    def __init__(self, device_id, camera_quality):
        Device.__init__(self, device_id)
        self.camera_quality = camera_quality

    def capture_image(self):
        print(f"Capturing image with {self.camera_quality} camera.")

# Demonstration
drone = Drone("D123", "4K")
drone.info()
drone.fly()
drone.capture_image()
