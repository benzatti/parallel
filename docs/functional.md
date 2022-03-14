The Parallel library must provide developers with an interface that facilitates executing multiple tasks in parallel and also partition an otherwise sequential list of work into tasks that can be executed in parallel.

For this purpose, the following capabilities must be provided:

- Invoke multiple functions in parallel
- Execute a ‘for’ loop in which iterations run in parallel
- Execute a ‘for each’ in which each item is processed in parallel

Application code is often expressed in the form of a function or method (def), an asynchronous function or method (async def), or even a lambda function.

As a library that aims to facilitate development of concurrent execution in applications, Parallel must support all of these approaches.

*Synchronous functions and methods*

These are functions and methods defined with the ‘def’ keyword and they execute synchronously wherever they are called.

*Asynchronous functions and methods*

An asynchronous method or function is one that returns a task (sometimes referred as promise or future) that can be awaited. These methods and functions are defined with the ‘async def’ keywords.

*Lambda functions*

Lambda function can be declared inline in the code but are essentially synchronous function which often define a single operation. There is currently no support for asynchronous lambdas in Python (https://bugs.python.org/issue33447).

The library should support these different programming approaches while keeping the same interface regardless of whether the application code is expressed as an asynchronous function, synchronous function, or lambda function. 

*Other goals and requirements*

The Parallel library should be available as an easy to integrate package that can be download, cloned or forked by other applications. The repository must be maintained with a minimum of 90% code coverage, PEP8 coding standards, examples, documentation and a continuous integration pipeline.