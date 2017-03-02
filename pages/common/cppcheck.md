# cppcheck

> A static analysis tool for C/C++ code.
> Instead of syntax errors, it focuses on the types of bugs that compilers normally do not detect.

- Recursively check the current folder, showing progress on the screen and logging error messages to a file:

`cppcheck . 2> cppcheck.log`

- Recursively check a given folder, and don't print progress messages:

`cppcheck --quiet {{path/to/folder}}`

- Check a given file, specifying which tests to perform (by default only errors are shown):

`cppcheck --enable={{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- List available tests, filtered by a given search pattern:

`cppcheck --errorlist | grep "{{search pattern}}"`

- Check a given file, ignoring specific tests:

`cppcheck --suppress={{test_id1}} --suppress={{test_id2}} {{path/to/file.cpp}}`

- Check the current folder, providing paths for include files located outside it (e.g. external libraries):

`cppcheck -I {{include/folder_1}} -I {{include/folder_2}} .`

- Check a Microsoft Visual Studio project (`*.vcxproj`) or solution (`*.sln`):

`cppcheck --project={{path/to/project.sln}}`
