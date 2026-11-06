
import random
from time import perf_counter
from sorting import merge_sort
from knapsack import knapsack


def generate_parcels(n):
    return [
        {
            "id": i,
            "name": f"Parcel_{i}",
            "weight": random.randint(1, 10),
            "value": random.randint(10, 100),
            "priority": random.randint(1, 5)
        }
        for i in range(n)
    ]


def benchmark():
    print("\n--- DATASET PERFORMANCE COMPARISON ---")

    for size in [10, 100, 500, 1000]:
        parcels = generate_parcels(size)

        start = perf_counter()
        merge_sort(parcels)
        sort_time = (perf_counter() - start) * 1000

        start = perf_counter()
        knapsack(parcels, 50)
        pack_time = (perf_counter() - start) * 1000

        print(f"\nDataset size: {size}")
        print(f"Merge Sort: {sort_time:.4f} ms")
        print(f"Knapsack: {pack_time:.4f} ms")


if __name__ == "__main__":
    benchmark()

