# ctest

> CMake test driver program.
> More information: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

- Run all tests defined in the CMake project, executing 4 [j]obs at a time in parallel:

`ctest {{[-j|--parallel]}} {{4}} --output-on-failure`

- List available tests:

`ctest {{[-N|--show-only]}}`

- Run a single test based on its name, or filter on a regular expression:

`ctest --output-on-failure {{[-R|--tests-regex]}} '^{{test_name}}$'`
