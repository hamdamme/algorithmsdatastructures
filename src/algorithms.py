"""Core algorithms with explicit input contracts and complexity notes."""

from __future__ import annotations

from collections import deque
from typing import TypeVar

T = TypeVar("T")


def binary_search(values: list[T], target: T) -> int | None:
    """Return an index of target in sorted values, or None.

    Time: O(log n). Space: O(1). Values must support a total ordering.
    """
    low, high = 0, len(values)
    while low < high:
        middle = (low + high) // 2
        if values[middle] < target:
            low = middle + 1
        elif target < values[middle]:
            high = middle
        else:
            return middle
    return None


def merge_sort(values: list[T]) -> list[T]:
    """Return a stable sorted copy.

    Time: O(n log n). Extra space: O(n).
    """
    width = len(values)
    if width < 2:
        return values.copy()

    middle = width // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged: list[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


class DisjointSet:
    """Maintain a partition of integer elements from 0 through size minus one."""

    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("size cannot be negative")
        self._parent = list(range(size))
        self._size = [1] * size

    def _check(self, item: int) -> None:
        if not 0 <= item < len(self._parent):
            raise IndexError("item is outside the set")

    def find(self, item: int) -> int:
        """Return the representative, compressing the traversed path."""
        self._check(item)
        root = item
        while root != self._parent[root]:
            root = self._parent[root]
        while item != root:
            parent = self._parent[item]
            self._parent[item] = root
            item = parent
        return root

    def union(self, first: int, second: int) -> bool:
        """Join two components; return True when a merge occurred."""
        root_a = self.find(first)
        root_b = self.find(second)
        if root_a == root_b:
            return False
        if self._size[root_a] < self._size[root_b]:
            root_a, root_b = root_b, root_a
        self._parent[root_b] = root_a
        self._size[root_a] += self._size[root_b]
        return True

    def connected(self, first: int, second: int) -> bool:
        """Return whether two elements have the same representative."""
        return self.find(first) == self.find(second)


def topological_order(
    vertex_count: int,
    edges: list[tuple[int, int]],
) -> list[int]:
    """Return a topological order or raise ValueError when a cycle exists.

    Edges are directed pairs (source, destination). Time: O(V + E).
    """
    if vertex_count < 0:
        raise ValueError("vertex_count cannot be negative")
    adjacency: list[list[int]] = [[] for _ in range(vertex_count)]
    indegree = [0] * vertex_count
    for source, destination in edges:
        if not (0 <= source < vertex_count and 0 <= destination < vertex_count):
            raise IndexError("edge endpoint is outside the graph")
        adjacency[source].append(destination)
        indegree[destination] += 1

    ready = deque(vertex for vertex, degree in enumerate(indegree) if degree == 0)
    order: list[int] = []
    while ready:
        vertex = ready.popleft()
        order.append(vertex)
        for neighbor in adjacency[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)
    if len(order) != vertex_count:
        raise ValueError("graph contains a directed cycle")
    return order
