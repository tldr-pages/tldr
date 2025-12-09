# multitail

> Extension of tail.
> More information: <https://manned.org/multitail>.

- Tail all files matching a pattern in a single stream:

`multitail -Q 1 '{{pattern}}'`

- Tail all files in a directory in a single stream:

`multitail -Q 1 '{{path/to/directory}}/*'`

- Automatically add new files to a window:

`multitail -Q {{pattern}}`

- Show 5 logfiles while merging 2 and put them in 2 columns with only one in the left column:

`multitail -s 2 -sn 1,3 {{path/to/mergefile}} -I {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} {{path/to/file4}}`
