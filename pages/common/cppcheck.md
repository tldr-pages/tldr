# cppcheck

> A static analysis tool for C/C++ code.
> Instead of syntax errors, it focuses on the types of bugs that compilers normally do not detect.
> More information: <http://cppcheck.sourceforge.net>.

- Recursively check the current directory, showing progress on the screen and logging error messages to a file:

`cppcheck . 2> cppcheck.log`

- Recursively check a given directory, and don't print progress messages:

`cppcheck --quiet {{path/to/directory}}`

- Check a given file, specifying which tests to perform (by default only errors are shown):

`cppcheck --enable {{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- List available tests:

`cppcheck --errorlist`

- Check a given file, ignoring specific tests:

`cppcheck --suppress {{test_id1}} --suppress {{test_id2}} {{path/to/file.cpp}}`

- Check the current directory, providing paths for include files located outside it (e.g. external libraries):

`cppcheck -I {{include/directory_1}} -I {{include/directory_2}} .`

- Check a Microsoft Visual Studio project (`*.vcxproj`) or solution (`*.sln`):

`cppcheck --project {{path/to/project.sln}}`
