# addr2line

> Convert addresses of a binary into file names and line numbers.

- Get the file name and line number of an instruction address of an executable in the source code:

`addr2line --exe=<executable> <address>`

- Also show the function name:

`addr2line --exe=<executable> --functions <address>`

- Demangle function name for C++ code:

`addr2line --exe=<executable> --functions --demangle <address>`
