# Parallel

This library provides methods to help developers quickly create parallelism in their applications, making it simple to partition work through multiple parallel calls or through parallel 'for' and 'foreach'.

[![Python package](https://github.com/benzatti/parallel/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/benzatti/parallel/actions/workflows/python-package.yml)

[![Code Coverage](https://img.shields.io/codecov/c/github/benzatti/parallel/master?logo=codecov)](https://github.com/benzatti/parallel/actions/workflows/cc.yml)

## Key Features

- Parallel.invoke: Invokes multiple functions or coroutines in parallel.
- Parallel.for_range: Executes a 'for' loop in which iterations run in parallel. 
- Parallel.for_each: Executes a 'for each' in parallel.

Check out some examples by running main.py.

```python
from parallel import Parallel
```

```python
(
    Parallel.for_range(
        start=0,
        stop=10,
        invoke=lambda i: print(f"Processing partition {i}")
    )
)
```

Output:

```
Processing Item 8
Processing Item 1
Processing Item 3
Processing Item 9
Processing Item 0
Processing Item 4
Processing Item 5
Processing Item 7
Processing Item 6
Processing Item 2
```

Parallel also works with async functions.

```python
async def download_file(name, duration):
    print(f"Downloading {name} started.")
    await asyncio.sleep(duration)
    print(f"Downloading {name} completed.")

(
    Parallel.invoke(
        download_file("X", duration=1),
        download_file("Y", duration=2),
        download_file("Z", duration=1)
    )
)
```

Output:

```
Downloading X started.
Downloading Y started.
Downloading Z started.
Downloading X completed.
Downloading Z completed.
Downloading Y completed.
```

With 'for each', a task is assigned to each item to process all items in parallel.

```python
async def process_item(item):
    await asyncio.sleep(1)
    print(f"Processing {item}")

start_time = time.perf_counter()
(
    Parallel.for_each(
        items=["Item X", "Item Y", "Item Z"],
        invoke=process_item
    )
)
print(f"Elapsed {time.perf_counter() - start_time}")
```

Output:

```
Processing Item Y
Processing Item X
Processing Item Z
Elapsed 1.0021614760626107
```

## Install
While Parallel is not yet a package, it can be installed by copying/cloning this repository and running the following: 

    python setup.py install

## References
Inspired by C#'s [Parallel library](https://docs.microsoft.com/en-us/dotnet/standard/parallel-programming/task-parallel-library-tpl).

## License
Released under MIT license. Improvements, fixes, forks are all welcome.
