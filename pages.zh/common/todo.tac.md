# tac

> Print and concatenate files in reverse (last line first).

- Print the contents of *file1* reversed to the standard output:

`tac {{file1}}`

- Print the contents of the standard input reversed to the standard output:

`{{command}} | tac`

- Concatenate several files reversed into the target file:

`tac {{file1}} {{file2}} > {{target_file}}`
