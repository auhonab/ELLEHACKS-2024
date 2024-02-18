import random
import time

class VitalSignMonitor:
    def __init__(self):
        self.heart_rate = 0
        self.breathing_rate = 0
        self.water_pressure = 0

    def measure_vital_signs(self):
        # Simulate measuring heart rate, breathing rate, and water pressure
        self.heart_rate = random.randint(60, 120)
        self.breathing_rate = random.randint(12, 20)
        self.water_pressure = random.randint(0, 100)  # Simulate pressure in meters of water depth

    def detect_drowning(self):
        # Simulate detecting drowning based on abnormal vital signs and submersion
        if self.heart_rate < 70 or self.breathing_rate < 10 or self.water_pressure > 50:
            return True
        else:
            return False

class AlertSystem:
    def send_alert(self, message):
        print("ALERT:", message)

def main():
    monitor = VitalSignMonitor()
    alert_system = AlertSystem()

    while True:
        # Simulate measuring vital signs every 5 seconds
        monitor.measure_vital_signs()
        time.sleep(5)

        # Check for drowning and send alert if necessary
        if monitor.detect_drowning():
            alert_system.send_alert("Potential drowning detected!")

if __name__ == "__main__":
    main()