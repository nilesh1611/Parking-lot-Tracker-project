class ParkingLot:
    def __init__(self):
        self.spots = {}
        for i in range(1, 40):
            if i <= 20:
                level = "A"
            else:
                level = "B"
            self.spots[i] = (level, None)

    def assign_spot(self, vehicle):
        for spot, (level, parked_vehicle) in self.spots.items():
            if parked_vehicle is None:
                self.spots[spot] = (level, vehicle)
                return {"level": level, "spot": spot}
        return None

    def retrieve_spot(self, vehicle):
        for spot, (level, parked_vehicle) in self.spots.items():
            if parked_vehicle == vehicle:
                return {"level": level, "spot": spot}
        return None