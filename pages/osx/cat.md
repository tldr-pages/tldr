# cat

> Concatenate and display the content of files.
> Built-in command of OS X.
> More information: <https://ss64.com/osx/cat.html>.

- Display a file's contents:

`cat {{path/to/file}}`

- Display all files of extension:

`cat {{*.ext}}`

- Concatenate two files:

`cat {{path/to/file1.ext}} {{path/to/file2.ext}} > union {{filename.ext}}`

- Store contents of a file in a variable:

`my_variable='cat File3.txt'`
