# ctest

> CMake test driver program.
> More information: <https://gitlab.kitware.com/cmake/community/-/wikis/doc/ctest/Testing-With-CTest>.

- Run all tests in the current CMake build directory:

`ctest`

- Run all tests defined in the CMake build directory, executing 4 [j]obs at a time in parallel:

`ctest {{[-j|--parallel]}} 4`

- Run all tests defined in the CMake build directory and print detailed logs on failed tests:

`ctest --output-on-failure`

- List available tests:

`ctest {{[-N|--show-only]}}`

- Run a single test based on its name, or filter on a `regex`:

`ctest --output-on-failure {{[-R|--tests-regex]}} '^{{test_name}}$'`
