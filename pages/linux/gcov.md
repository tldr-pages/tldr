# gcov

> Code coverage analysis and profiling tool that discovers untested parts of a program.
> Also displays a copy of source code annotated with execution frequencies of code segments.
> More information: <https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>.

- Generate a coverage report named `file.cpp.gcov`:

`gcov {{path/to/file.cpp}}`

- Write individual execution counts for every basic block:

`gcov --all-blocks {{path/to/file.cpp}}`

- Write branch frequencies to the output file and print summary information to `stdout` as a percentage:

`gcov --branch-probabilities {{path/to/file.cpp}}`

- Write branch frequencies as the number of branches taken, rather than the percentage:

`gcov --branch-counts {{path/to/file.cpp}}`

- Do not create a `gcov` output file:

`gcov --no-output {{path/to/file.cpp}}`

- Write file level as well as function level summaries:

`gcov --function-summaries {{path/to/file.cpp}}`
