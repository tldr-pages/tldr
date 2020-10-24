# valgrind

> Wrapper for a set of expert tools for profiling, optimizing and debugging programs.
> Commonly used tools include `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind`, and `drd`.
> More information: <http://www.valgrind.org>.

- Use the (default) Memcheck tool to show a diagnostic of memory usage by `program`:

`valgrind {{program}}`

- Use Memcheck to report all possible memory leaks of `program` in full detail:

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- Use the Cachegrind tool to profile and log CPU cache operations of `program`:

`valgrind --tool=cachegrind {{program}}`

- Use the Massif tool to profile and log heap memory and stack usage of `program`:

`valgrind --tool=massif --stacks=yes {{program}}`
