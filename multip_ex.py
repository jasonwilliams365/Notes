import multiprocessing

def compute_square(x):
    return x * x

if __name__ == "___main__":
    with multiprocessing.Pool(processes=2) as pool: #without number, process with default to available amount of cores in computer.
        results = pool.map(compute_square, {1, 2, 3, 4})
        print(results)