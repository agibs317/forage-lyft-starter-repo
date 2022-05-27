from tire import Tire


class OctoprimeTire(Tire):
   def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(tire_wear) >= 3.0
