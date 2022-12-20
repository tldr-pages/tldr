# awk

> Find and Replace text within file(s).
> More information: <https://ss64.com/osx/awk.html>.

- Define an input field separator:

`awk -F '{{regular_expression}}'`

- Assign values before prog is executed:

`awk [ -v var=value ]`

- Specify a pattern to match within progfile:

`awk [ 'prog' | -f progfile ]`

- Set the maximum size of the input record (MaxRows):

`awk -mr`

- Set the maximum number of fields (MaxFields):

`awk -mf`
