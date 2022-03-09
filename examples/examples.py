import time
import asyncio
from parallel import Parallel


# #########################################
# Examples
# #########################################

print("Example 01 - Invoking multiple lambda expressions in parallel.")
start_time = time.perf_counter()

(
    Parallel.invoke(
        lambda: print("Task A"),
        lambda: print("Task B"),
        lambda: print("Task C")
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")

# #######################################################################################

print("Example 02 - Invoking multiple synchronous functions in parallel.")

def operation1():
    print("Starting operation 01")
    time.sleep(3)
    print("Finished operation 01")

def operation2():
    print("Starting operation 02")
    time.sleep(2)
    print("Finished operation 02")

def operation3():
    print("Starting operation 03")
    time.sleep(1)
    print("Finished operation 03")

start_time = time.perf_counter()
(
    Parallel.invoke(
        operation1,
        operation2,
        operation3
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")

# #######################################################################################

print("Example 03 - Invoking multiple asynchronous functions in parallel.")

async def download_file(name, duration):
    print(f"Downloading {name} started.")
    await asyncio.sleep(duration)
    print(f"Downloading {name} completed.")

start_time = time.perf_counter()
(
    Parallel.invoke(
        download_file("X", duration=1),
        download_file("Y", duration=2),
        download_file("Z", duration=1)
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")

# #######################################################################################

print("Example 04 - Executing a parallel 'for' loop using a synchronous function.")

start_time = time.perf_counter()
(
    Parallel.for_range(
        start=0,
        stop=10,
        invoke=lambda i: print(f"Processing partition {i}")
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")

# #######################################################################################

print("Example 05 - Executing a parallel 'for' loop using an asynchronous function.")

async def do_some_work(i):
    await asyncio.sleep(1)
    print(f"Item {i}")

start_time = time.perf_counter()
(
    Parallel.for_range(
        start=0,
        stop=10,
        invoke=do_some_work
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")

# #######################################################################################

print("Example 06 - Executing a parallel 'for each' loop using a synchronous function.")

start_time = time.perf_counter()
(
    Parallel.for_each(
        items=[f"Item {i}" for i in range(10)],
        invoke=lambda i: print(f"Executing {i}")
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")

# #######################################################################################

print("Example 07 - Executing a parallel 'for each' loop using an asynchronous function.")

async def process_item(item):
    await asyncio.sleep(1)
    print(f"Processing {item}")

start_time = time.perf_counter()
(
    Parallel.for_each(
        items=[f"Item {i}" for i in range(10)],
        invoke=process_item
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")
