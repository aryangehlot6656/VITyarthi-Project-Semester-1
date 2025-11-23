
def get_emission_factor():
    print("Select your vehicle type:")
    print("1. CNG (Carbon dioxide emission: 0.12 kg/km)")
    print("2. Petrol (Carbon dioxide emission: 0.21 kg/km)")
    print("3. Diesel (Carbon dioxide emission: 0.24 kg/km)")

    choice = int(input("Enter choice (1/2/3): "))

    if choice == 1:
        return 0.12
    elif choice == 2:
        return 0.21
    elif choice == 3:
        return 0.24
    else:
        print("Invalid choice! Defaulting to Petrol.")
        return 0.21

def get_route_data():
    distances = []
    traffic_levels = []

    print("\nEnter details for 3 routes:")

    for i in range(1, 4):
        d = float(input(f"\nEnter distance for Route {i} (km): "))
        print("Select traffic level for this route:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        t = int(input("Enter choice (1/2/3): "))

        distances.append(d)
        traffic_levels.append(t)

    return distances, traffic_levels

def get_traffic_multiplier(level):
    if level == 1:
        return 1.0
    elif level == 2:
        return 1.2
    elif level == 3:
        return 1.5
    else:
        return 1.0  

def calculate_emission(distance, emission_factor, traffic_level):
    multiplier = get_traffic_multiplier(traffic_level)
    return distance * emission_factor * multiplier


def find_best_route(distances, traffic_levels, emissions):
    
    if emissions[0] == emissions[1] == emissions[2]:
        print("\nAll routes have the SAME carbon emissions.")

       
        preferred_traffic = 2
        preferred_routes = []

        for i in range(3):
            if traffic_levels[i] == preferred_traffic:
                preferred_routes.append(i)

        if preferred_routes:
            best = min(preferred_routes, key=lambda idx: distances[idx])
            print("System suggestion based on moderate traffic + moderate distance:")
            return best + 1

        print("No moderate-traffic route found. Choosing the shortest route.")
        best = distances.index(min(distances))
        return best + 1

    best_index = emissions.index(min(emissions))
    return best_index + 1

def display_summary(distances, traffic_levels, emissions, best_route):
    print("\n---- ROUTE ANALYSIS SUMMARY ----\n")
    for i in range(3):
        print(f"Route {i+1}:")
        print(f"  Distance: {distances[i]} km")
        print(f"  Traffic Level: {traffic_levels[i]}")
        print(f"  Total Emissions: {emissions[i]:.2f} kg CO2\n")

    print(f" Most Eco-Friendly Route: ROUTE {best_route}")

def main():
    print("\n---- ECO-ROUTE EMISSION TRACKER ----\n")

    ef = get_emission_factor()
    distances, traffic = get_route_data()

    emissions = []
    for i in range(3):
        e = calculate_emission(distances[i], ef, traffic[i])
        emissions.append(e)

    best_route = find_best_route(distances, traffic, emissions)
    display_summary(distances, traffic, emissions, best_route)
main()
