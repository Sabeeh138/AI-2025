import random

class Environment:
    def __init__(self):
        self.locations = ["Corridor", "Patient Room 101", "Patient Room 102", "Nurse Station", "Medicine Storage"]
        self.patients = {
            "101": {"name": "John Doe", "medicine": "Aspirin", "schedule": "Morning"},
            "102": {"name": "Jane Smith", "medicine": "Ibuprofen", "schedule": "Afternoon"}
        }
        self.staff_available = random.choice([True, False])

class HospitalDeliveryRobot:
    def __init__(self, environment):
        self.environment = environment
        self.current_location = "Corridor"
        self.carrying_medicine = None

    def move_to(self, location):
        print(f"Moving to {location}...")
        self.current_location = location

    def pick_up_medicine(self, room_number):
        patient = self.environment.patients[room_number]
        print(f"Picking up {patient['medicine']} for {patient['name']}.")
        self.carrying_medicine = patient['medicine']

    def scan_patient_id(self, room_number):
        print(f"Scanning patient ID in Room {room_number}...")
        return True  # Assuming the scan is always successful for simplicity

    def deliver_medicine(self, room_number):
        if self.scan_patient_id(room_number):
            print(f"Delivering {self.carrying_medicine} to {self.environment.patients[room_number]['name']} in Room {room_number}.")
            self.carrying_medicine = None
        else:
            print("Patient ID verification failed. Alerting staff.")
            self.alert_staff()

    def alert_staff(self):
        if self.environment.staff_available:
            print("Alerting available staff for assistance.")
        else:
            print("No staff available to assist at the moment.")

    def perform_delivery_cycle(self):
        for room_number in self.environment.patients:
            self.move_to("Medicine Storage")
            self.pick_up_medicine(room_number)
            self.move_to(f"Patient Room {room_number}")
            self.deliver_medicine(room_number)
            self.move_to("Corridor")

# Initialize the environment and agent
environment = Environment()
robot = HospitalDeliveryRobot(environment)

# Perform the delivery cycle
robot.perform_delivery_cycle()
