# smart_home.py

class Appliance:
    def status(self):
        print("Status: Appliance is functioning.")

class Fan(Appliance):
    def status(self):
        print("Status: Fan is spinning.")

class Light(Appliance):
    def status(self):
        print("Status: Light is turned on.")

class AC(Appliance):
    def status(self):
        print("Status: AC is cooling.")

# Polymorphism demonstration
devices = [Fan(), Light(), AC()]

for device in devices:
    device.status()
