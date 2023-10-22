# expand

> Convert tabs to spaces.
> More information: <https://www.gnu.org/software/coreutils/expand>.

- Convert tabs in each file to spaces, writing to `stdout`:

`expand {{path/to/file}}`

- Convert tabs to spaces, reading from `stdin`:

`expand`

- Do not convert tabs after non blanks:

`expand -i {{path/to/file}}`

- Have tabs a certain number of characters apart, not 8:

`expand -t={{number}} {{path/to/file}}`

- Use a comma separated list of explicit tab positions:

`expand -t={{1,4,6}}`
