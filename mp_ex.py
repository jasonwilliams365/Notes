import multiprocessing
import time


def compute_square(x):
     time.sleep(1) # Simulate a time-consuming computation
     return x * x

if __name__ == "__main__":
     input_data = list(range(1, 11))

     # Creating a pool with 4 worker processes
     with multiprocessing.Pool(processes=4) as pool:
         start_time = time.time()

          # Using pool.map to compute squares
         results = pool.map(compute_square, input_data)

         end_time = time.time()

         print(f"Input Data: {input_data}")
         print(f"Squared Results: {results}")
         print(f"TIme Taken: {end_time - start_time} seconds")

