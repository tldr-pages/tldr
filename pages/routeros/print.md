# print

> Print the currently-configured entries on a system log or settings directory.
> Equivalent to `ls` and `cat` in common filesystems.
> More information: <https://manual.mikrotik.com/docs/developer-guides/scripting/#print-parameters>.

- List all of the configured settings or log entries in the current settings directory:

`print`

- List all of the configured settings or log entries in a specific settings directory:

`{{/ip/route}} print`

- Sort the output by a specific attribute or parameter (use `-{{parameter}}` for descending order):

`print order-by={{parameter}}`

- Filter the output by a specific attribute or parameter:

`print where {{parameter}}={{value}}`

- Print all entries without interactive paging functionality:

`print without-paging`

- Automatically print new entries, with or without displaying previous entries:

`print {{follow|follow-only}}`

- Print and continuously update all entries for a specific interval:

`print interval={{seconds}}`

- List without comments and save outputs to a file:

`print !comments file={{path/to/file}}`
