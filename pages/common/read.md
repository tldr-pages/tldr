# read

> Shell builtin for retrieving data from `stdin`.
> More information: <https://manned.org/read.1p>.

- Store data that you type from the keyboard:

`read {{variable}}`

- Do not let backslash (\\) act as an escape character:

`read -r {{variable}}`

- Read `stdin` and perform an action on every line:

`while read line; do echo "$line"; done`
