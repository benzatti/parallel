The Parallel library will expose three methods that closely correspond with the functional goals:

- Parallel.invoke: Invokes multiple functions or coroutines in parallel.
- Parallel.for_range: Executes a 'for' loop in which iterations run in parallel.
- Parallel.for_each: Executes a 'for each' in which items are processed in parallel.

Per functional requirements, these functions need to work with synchronous, asynchronous and lambda functions. 

In order to support executing synchronous methods asynchronously, the library must take a function pointer and spawn a thread to execute the function concurrently with other tasks. Similarly, for lambda functions, which are inherently synchronous, a thread must also be scheduled. However, for asynchronous methods, the task is simply scheduled with the default thread pool.

The decision to schedule a thread or a task is based on inspecting the function passed to Parallel by the application as a parameter. The ‘inspect’ library (https://docs.python.org/3/library/inspect.html) is used to evaluate if the specified function is a regular function pointer, or if it is an awaitable or a coroutine (async function).

Internally, Parallel defines a single component, called ThreadManager, which is responsible for keeping track all the pending tasks, scheduling these tasks with the thread pool, and awaiting their execution until the end.

Upon each call to the Parallel library, a new ThreadManager instance is created and tasks are scheduled for each unit of work that needs to be executed in parallel. Once the tasks are running, the ThreadManager awaits their execution and returns to the main thread once all tasks completed.

By keeping track of the tasks, the ThreadManager also has access to the result of each task (or return value from the corresponding function). This is important because it will allow new functionality to be added to the Parallel package without breaking backwards compatibility. 