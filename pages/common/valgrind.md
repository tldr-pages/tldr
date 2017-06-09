# valgrind

> Wrapper for a set of expert tools for profiling, optimizing and debugging programs.

- Test `program` with a specified Valgrind tool:

`valgrind --tool={{tool_name}} {{program}}`

- Use the (default) Memcheck tool to report all possible memory leaks of `program` in detail:

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- Use the Cachegrind tool to profile and log CPU cache operations of `program`:

`valgrind --tool=cachegrind {{program}}`

- Use the Massif tool to profile and log heap memory and stack usage of `program`:

`valgrind --tool=massif --stacks=yes {{program}}`
