# diff3

> Utility to compare three files and show differences among them with the ability to three-way merge files.

- Basic comparison of three files:

`diff3 {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Basic comparison of three files, treating all files as text files, even if they are not:

`diff3 -a {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Output changes file1 and file2 do compared to file3 in order:

`diff3 -m {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`
