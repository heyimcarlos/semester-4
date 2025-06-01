"""DSA Lab 2 - Carlos De La Cruz - 301391100"""


# Recreation of `Exercises.java` in Python.
class Exercises:

    # Exercise 1

    # `example1` has a running time of O(n).
    # O(n) (linear time)
    @staticmethod
    def example1(arr):
        """Returns the sum of the integers in given array."""
        total = 0  # O(1) - constant time
        for j in range(
            len(arr)
        ):  # O(n) - linear time (increases relative to input size)
            total += arr[j]  # O(1) - constant time
        return total

    # `example2` has a running time of O(n/2), because 2 is a constant, we disregard it because
    # it does not affect the underlying growth rate of the algorithm.
    # O(n/2) = O(n) (linear time)
    @staticmethod
    def example2(arr):
        """Returns the sum of the integers with even index in given array."""
        total = 0  # O(1) - constant time
        for j in range(0, len(arr), 2):  # O(n/2) - linear time with step of 2
            total += arr[j]  # O(1) - constant time
        return total

    # `example3` has a running time of O(n^2). Because the inner loop runs j+1 times for each j.
    # n(n+1)/2 = O(n * n) = O(n^2) (quadratic time)
    @staticmethod
    def example3(arr):
        """Returns the sum of the prefix sums of given array."""
        total = 0  # O(1) - constant time
        for j in range(len(arr)):  # Outer
            for k in range(j + 1):  # Inner
                total += arr[j]  # O(1) - constant time
        return total

    # `example4` has a running time of O(n) because it loops through the array once
    # O(n) + O(n) = O(n + n) = O(n) (linear time)
    @staticmethod
    def example4(arr):
        """Returns the sum of the prefix sums of given array."""
        prefix = 0  # O(1) - constant time
        total = 0  # O(1) - constant time
        for j in range(len(arr)):  # O(n) - linear time
            prefix += arr[j]  # O(1) - constant time
            total += prefix  # O(1) - constant time
        return total

    # `example5` has a running time of O(n^3) because it has three nested loops ()
    # O(n) * O(n^2) = O(n * n^2) = O(n^3) (cubic time)
    @staticmethod
    def example5(first, second):
        """Returns the number of times second array stores sum of prefix sums from first."""
        count = 0  # O(1) - constant time
        for i in range(len(first)):  # O(n) - linear time
            total = 0  # O(1) - constant time
            for j in range(len(first)):  # nested O(n) - linear time
                for k in range(j + 1):  # nested O(n) - linear time
                    total += first[k]  # O(1) - constant time
            if second[i] == total:
                count += 1  # O(1) - constant time
        return count


# Recreation of `PrefixAverage.java` in Python.
class PrefixAverage:
    """Class to compute prefix averages of an array."""

    @staticmethod
    def prefix_average1(x):
        """Returns an array a such that, for all j, a[j] equals the average of x[0], ..., x[j]."""
        n = len(x)
        a = [0.0] * n  # filled with zeros by default
        for j in range(n):
            total = 0.0  # begin computing x[0] + ... + x[j]
            for i in range(j + 1):
                total += x[i]
            a[j] = total / (j + 1)  # record the average
        return a

    @staticmethod
    def prefix_average2(x):
        """Returns an array a such that, for all j, a[j] equals the average of x[0], ..., x[j]."""
        n = len(x)
        a = [0.0] * n  # filled with zeros by default
        total = 0.0  # compute prefix sum as x[0] + x[1] + ...
        for j in range(n):
            total += x[j]  # update prefix sum to include x[j]
            a[j] = total / (j + 1)  # compute average based on current sum
        return a


# Exercise 2
# Perform an experimental analysis of the two algorithms prefix_average1 and prefix_average2,
# from lesson examples. Optionally, visualize their running times as a function of the input size
# with a log-log chart. Use either Java or Python graphical capabilities for visualization.
# Hint: Choose representative values of the input size n, similar to StringExperiment.java from
# class examples


def compare_prefix_averages():
    """Compares the running times of prefix_average1 and prefix_average2."""
    import time

    import matplotlib.pyplot as plt
    import numpy as np

    start_n = 1_000
    step_multi = 1.5
    trials = 10

    sizes = []
    times1 = []
    times2 = []
    current_n = start_n
    for _ in range(trials):
        x = list(range(int(current_n)))

        print(f"Testing n = {current_n}")

        avg_run_times1 = []
        for _ in range(int(trials / 2)):
            start_time = time.perf_counter()
            PrefixAverage.prefix_average1(x)
            end_time = time.perf_counter()
            avg_run_times1.append(end_time - start_time)

        avg_times1 = np.mean(avg_run_times1)
        times1.append(avg_times1)

        print(f"prefix_average1 time: {avg_times1:.8f} seconds, ")

        avg_run_times2 = []
        for _ in range(int(trials / 2)):
            start_time = time.perf_counter()
            PrefixAverage.prefix_average2(x)
            end_time = time.perf_counter()
            avg_run_times2.append(end_time - start_time)

        avg_times2 = np.mean(avg_run_times2)
        times2.append(avg_times2)

        print(f"prefix_average2 time: {avg_times2:.8f} seconds")

        sizes.append(current_n)
        current_n *= step_multi  # Double the size for the next trial

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(
        sizes,
        times1,
        label="prefix_average1 ($O(n^2)$)",
        marker="o",
        linestyle="-",
        color="red",
    )
    plt.plot(
        sizes,
        times2,
        label="prefix_average2 ($O(n)$)",
        marker="x",
        linestyle="-",
        color="blue",
    )
    plt.xlabel("Input Size (n)")
    plt.ylabel("Mean time (seconds)")
    plt.title("Comparison of Prefix Average Algorithms")
    plt.legend()
    plt.grid(True, alpha=0.7)
    plt.show()


compare_prefix_averages()


# Exercise 3
# x contains n-1 unique integers in the range [0, n-1], find the missing integer in O(n) time.
def exercise3(x):
    n = len(x) + 1
    range_sum = n * (n - 1) // 2
    actual_sum = sum(x)  # O(n) time complexity
    result = range_sum - actual_sum
    return result


exercise3([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Should return 10
exercise3([1, 2, 3, 4, 5])  # Should return 0 (missing integer in range [0, 5])
exercise3([0, 2, 3, 4])  # Should return 1 (missing integer in range [0, 4])
exercise3([0, 1, 2, 4])  # Should return 3 (missing integer in range [0, 4])
exercise3([0, 1, 3])  # Should return 2 (missing integer in range [0, 3])
