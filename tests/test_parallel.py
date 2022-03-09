from parallel import Parallel
import threading
import pytest


class Counter:
    def __init__(self, initial_value):
        self.lock = threading.RLock()
        self.counter = initial_value

    def increment(self):
        with self.lock:
            self.counter += 1

    def add(self, x):
        with self.lock:
            self.counter += x

    def get_value(self):
        return self.counter


def test_parallel_invoke():
    # Arrange
    counter = Counter(0)

    # Act
    Parallel.invoke(
        lambda: counter.increment(),
        lambda: counter.increment(),
        lambda: counter.increment(),
    )

    # Assert
    assert 3 == counter.get_value()


def test_parallel_for_range():
    # Arrange
    counter = Counter(0)

    # Act
    Parallel.for_range(
        start=0,
        stop=10,
        invoke=lambda x: counter.add(x),
    )

    # Assert
    assert 45 == counter.get_value()


def test_parallel_for_each():
    # Arrange
    counter = Counter(0)

    # Act
    Parallel.for_each(
        items=[1, 2, 3, 4],
        invoke=lambda x: counter.add(x),
    )

    # Assert
    assert 10 == counter.get_value()


def test_parallel_tasks():
    # Arrange
    resume_task_two = threading.Event()
    resume_task_three = threading.Event()
    end_of_test = threading.Event()
    results = []

    def task_one():
        results.append("one")
        resume_task_three.set()

    def task_two():
        resume_task_two.wait()
        results.append("two")
        end_of_test.set()

    def task_three():
        resume_task_three.wait()
        results.append("three")
        resume_task_two.set()

    # Act
    Parallel.invoke(
        task_one,
        task_two,
        task_three,
    )

    end_of_test.wait()

    # Assert
    assert ["one", "three", "two"] == results


def test_parallel_invoke_empty_arguments():
    with pytest.raises(ValueError):
        Parallel.invoke()


def test_parallel_for_each_with_wrong_type():
    with pytest.raises(TypeError):
        Parallel.for_each()


def test_parallel_for_each_with_empty_function():
    with pytest.raises(TypeError):
        Parallel.for_each([1, 2, 3])


def test_parallel_for_range_with_empty_function():
    with pytest.raises(TypeError):
        Parallel.for_range(start=0, stop=3)


def test_parallel_for_range_with_no_arguments():
    with pytest.raises(TypeError):
        Parallel.for_range()
