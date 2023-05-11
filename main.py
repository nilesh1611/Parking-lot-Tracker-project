from parking import ParkingLot


def main():
    parking_lot = ParkingLot()

    while True:
        command = input("Enter command (assign/retrieve/exit): ")
        if command == "assign":
            vehicle = input("Enter your vehicle number: ")
            result = parking_lot.assign_spot(vehicle)
            if result is None:
                print("Sorry!! Parking lot is full")
            else:
                print(f"Parking spot assigned: {result}")
        elif command == "retrieve":
            vehicle = input("Enter your vehicle number: ")
            result = parking_lot.retrieve_spot(vehicle)
            if result is None:
                print("Vehicle not found in parking lot")
            else:
                print(f"Parking spot retrieved: {result}")
        elif command == "exit":
            break
        else:
            print("Invalid command...please try again ")

if __name__ == "__main__":
    main()