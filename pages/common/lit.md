# lit

> LLVM integrated tester for executing LLVM and Clang style test suites, summarizing results.
> Part of LLVM.
> More information: <https://www.llvm.org/docs/CommandGuide/lit.html>.

- Run a specified test case:

`lit {{path/to/test_file.test}}`

- Run all test cases in a specified directory:

`lit {{path/to/test_suite}}`

- Run all test cases and check the wall time for each cases, then report to summary output:

`lit {{path/to/test_suite}} --time-tests`

- Run individual tests with Valgrind (memory check and memory leak test):

`lit {{path/to/test_file.test}} --vg --vg-leak --vg-args={{args_to_valgrind}}`
