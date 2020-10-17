# gcov

> Code coverage analysis and profiling tool. Discover untested parts of your program.
> Get copy of source code annotated with execution frequencies of code segments.
> More information: <https://linux.die.net/man/1/gcov>.

- Generate coverage report named `file.cpp.gcov`:

`gcov {{path/to/file.cpp}}`

- Write individual execution counts for every basic block:

`gcov {{-a|--all-blocks}} {{path/to/file.cpp}}`

- Write branch frequencies to output file and summary info to standard output as a percentage:

`gcov {{-b|--branch-probabilities}} {{path/to/file.cpp}}`

- Write branch frequencies as the number of branches taken, rather than the percentage:

`gcov {{-c|--branch-counts}} {{path/to/file.cpp}}`

- Do not create `gcov` output file:

`gcov {{-n|--no-output}} {{path/to/file.cpp}}`

> Output file level as well as function level summaries:v
`gcov {{-f|--function-summaries}} {{path/to/file.cpp}}`
