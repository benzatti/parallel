import inspect
import asyncio


class Parallel:
    """
    This class provides methods to help developers quickly create
     parallelism in their applications, making it simple to partition
     work through multiple parallel calls or through parallel 'for'
     and 'foreach'.
    """

    class ThreadManager:
        """
        Internally manages the scheduling and completion of tasks.
        """

        def __init__(self):
            self.tasks = []
            self.loop = asyncio.get_event_loop()

        @staticmethod
        async def _run_pending_tasks(pending_tasks):
            """
            Awaits all pending tasks.
            :param pending_tasks: A list of pending tasks.
            """
            await asyncio.wait(pending_tasks)

        def _run_until_complete(self):
            """
            Executes all pending tasks are executed until finished.
            """
            self.loop.run_until_complete(self._run_pending_tasks(self.tasks))

        def invoke(self, *functions):
            """
            Invokes the specified functions or coroutines in parallel. Lambda
             expressions and synchronous functions will be queued with a thread
             while coroutines will be scheduled as tasks.
            :param functions: One or more functions to be invoked.
            """
            for function in functions:
                if inspect.isawaitable(function):
                    self.tasks.append(self.loop.create_task(function))
                else:
                    self.tasks.append(asyncio.to_thread(function))

            self._run_until_complete()

        def invoke_for_range(self, start, stop, invoke):
            """
            Executes a 'for' loop in which iterations run in parallel. Lambda
             expressions and synchronous functions will be queued with a thread
             while coroutines will be scheduled as tasks.
            :param start: Start of the range (inclusive).
            :param stop: Stop condition of the range (exclusive).
            :param invoke: The function or coroutine to be executed for each index.
            """
            for i in range(start, stop):
                if inspect.iscoroutinefunction(invoke):
                    self.tasks.append(self.loop.create_task(invoke(i)))
                else:
                    self.tasks.append(asyncio.to_thread(invoke, i))

            self._run_until_complete()

        def invoke_for_each(self, items, invoke):
            """
            Executes the specified function or coroutine in parallel for each of
             the specified items. Lambda expressions and synchronous functions will
             be queued with a thread while coroutines will be scheduled as tasks.
            :param items: Items to be processed.
            :param invoke: The function or coroutine to be executed for each index.
            """
            for item in items:
                if inspect.iscoroutinefunction(invoke):
                    self.tasks.append(invoke(item))
                else:
                    self.tasks.append(asyncio.to_thread(invoke, item))

            self._run_until_complete()

    @staticmethod
    def invoke(*tasks):
        """
        Invokes the specified functions or coroutines in parallel.
        :param tasks: The functions or coroutines to be invoked.
        """
        thread_manager = Parallel.ThreadManager()
        thread_manager.invoke(*tasks)

    @staticmethod
    def for_range(start, stop, invoke):
        """
        Executes a 'for' loop in which iterations run in parallel.
        :param start: Start of the range (inclusive).
        :param stop: Stop condition of the range (exclusive).
        :param invoke: The function or coroutine to be executed for each index.
        """
        thread_manager = Parallel.ThreadManager()
        thread_manager.invoke_for_range(start, stop, invoke)

    @staticmethod
    def for_each(items, invoke):
        """
        Executes the specified function or coroutine in parallel for each of the specified items.
        :param items: Items to be processed.
        :param invoke: The function or coroutine to be executed for each index.
        """
        thread_manager = Parallel.ThreadManager()
        thread_manager.invoke_for_each(items, invoke)
