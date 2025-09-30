# expand

> Convert tabs to spaces.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- Convert tabs in each file to spaces, writing to `stdout`:

`expand {{path/to/file}}`

- Convert tabs to spaces, reading from `stdin`:

`expand`

- Do not convert tabs after non blanks:

`expand {{[-i|--initial]}} {{path/to/file}}`

- Have tabs a certain number of characters apart, not 8:

`expand {{[-t|--tabs]}} {{number}} {{path/to/file}}`

- Use a comma separated list of explicit tab positions:

`expand {{[-t|--tabs]}} {{1,4,6}}`
