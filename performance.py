
import time


def measure_performance(function, *args):
    start = time.perf_counter()
    result = function(*args)
    end = time.perf_counter()

    runtime = (end - start) * 1000

    return result, runtime


def display_performance(results):
    print("\n--- PERFORMANCE ANALYSIS ---")

    for name, runtime in results.items():
        print(f"{name}: {runtime:.6f} ms")
