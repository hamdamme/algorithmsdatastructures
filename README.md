# Algorithms and Data Structures

A compact Python collection of core algorithms with clear interfaces and stated complexity.

## Included

- Binary search for sorted sequences
- Stable merge sort
- Disjoint set union with path compression and union by size
- Topological ordering for directed acyclic graphs

Implementations are original work. Each function documents its input assumptions and complexity. Examples use only the Python standard library.

## Run an example

```sh
python3 - <<'PY'
from src.algorithms import DisjointSet, binary_search, merge_sort, topological_order

print(binary_search([2, 4, 7, 9], 7))
print(merge_sort([5, 1, 4, 1]))
sets = DisjointSet(5)
sets.union(0, 1)
print(sets.connected(0, 1))
print(topological_order(4, [(0, 1), (0, 2), (1, 3), (2, 3)]))
PY
```

## Reading

See [SOURCES.md](SOURCES.md). The listed books remain at their original sites. No book chapters or code listings are copied into this repository.

## License

Original code and notes are under the MIT License. Source material retains its own terms.
