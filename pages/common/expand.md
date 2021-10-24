# expand

> Convert tabs to spaces.
> More information: <https://www.gnu.org/software/coreutils/expand>.

- Convert tabs in each file to spaces, writing to standard output:

`expand {{file}}`

- Convert tabs to spaces, reading from standard input:

`expand`

- Do not convert tabs after non blanks:

`expand -i {{file}}`

- Have tabs a certain number of characters apart, not 8:

`expand -t={{number}} {{file}}`

- Use a comma separated list of explicit tab positions:

`expand -t={{1,4,6}}`
