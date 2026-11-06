
import csv

from sorting import merge_sort
from knapsack import knapsack
from graph import dijkstra, create_graph
from route_optimizer import nearest_neighbour
from performance import measure_performance, display_performance


def load_parcels():
    with open("parcels.csv", newline="") as file:
        return list(csv.DictReader(file))


def main():
    print("=" * 55)
    print("       SMART COURIER PLANNING SYSTEM")
    print("=" * 55)

    parcels = load_parcels()

    for parcel in parcels:
        for key in ["id", "weight", "value", "priority"]:
            parcel[key] = int(parcel[key])

    print("\n1. TOTAL PARCELS:", len(parcels))

    # Merge Sort
    sorted_parcels, sort_time = measure_performance(
        merge_sort, parcels
    )

    print("\n2. PARCEL PRIORITIZATION")
    for p in sorted_parcels:
        print(p["name"], "- Priority:", p["priority"])

    # Knapsack
    capacity = 10

    (selected, total_value), packing_time = measure_performance(
        knapsack, sorted_parcels, capacity
    )

    print("\n3. OPTIMAL PACKING PLAN")
    print("Vehicle Capacity:", capacity, "kg")

    for p in selected:
        print(p["name"], "-", p["weight"], "kg")

    print("Total Weight:", sum(p["weight"] for p in selected))
    print("Maximum Parcel Value:", total_value)

    # Graph and Dijkstra
    graph = create_graph()

    (distances, previous), dijkstra_time = measure_performance(
        dijkstra, graph, "Warehouse"
    )

    print("\n4. SHORTEST PATHS FROM WAREHOUSE")

    for location, distance in distances.items():
        print(location, ":", distance)

    # Nearest Neighbour
    (route, route_distance), route_time = measure_performance(
        nearest_neighbour, graph, "Warehouse"
    )

    print("\n5. DELIVERY ROUTE")
    print(" -> ".join(route))
    print("Route Distance:", route_distance)

    # Performance
    results = {
        "Merge Sort": sort_time,
        "Knapsack": packing_time,
        "Dijkstra": dijkstra_time,
        "Nearest Neighbour": route_time
    }

    display_performance(results)

    print("\n6. PROJECT COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
