# smart_home.py

class Appliance:
    def status(self):
        print("Appliance is in standby mode.")

class Fan(Appliance):
    def status(self):
        print("Fan is running at medium speed.")

class Light(Appliance):
    def status(self):
        print("Light is turned on with warm white mode.")

class AC(Appliance):
    def status(self):
        print("AC is cooling at 22°C.")

# Test the code
if __name__ == "__main__":
    devices = [Fan(), Light(), AC()]

    for device in devices:
        device.status()
