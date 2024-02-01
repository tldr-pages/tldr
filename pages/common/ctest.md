# ctest

> CMake test driver program.
> More information: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

- Run all tests defined in the CMake project, executing 4 jobs at a time in parallel:

`ctest -j{{4}} --output-on-failure`

- List available tests:

`ctest -N`

- Run a single test based on its name, or filter on a regular expression:

`ctest --output-on-failure -R '^{{test_name}}$'`
