# awk

> Find and Replace text within file(s).
> More information: <https://ss64.com/osx/awk.html>.

- Define an input field separator:

`awk -F '{{regular_expression}}'`

- Assign specific values to variables:

`awk {{-v variable1=value1 -v variable2=value2 ...}}`

- Execute a specific [f]ile:

`awk -f {{path/to/file}}`

- Set the maximum size of the input record:

`awk -mr {{1..infinity}}`

- Set the maximum number of fields:

`awk -mf {{1..infinity}}`
