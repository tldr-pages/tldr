# tspin

> A log file highlighter based on the `less` pager and basically behaves like any pager.
> More information: <https://github.com/bensadeh/tailspin#usage>.

- View a log file using the default pager (`less`):

`tspin {{path/to/file.log}}`

- Read from another command and print to `stdout`:

`{{command}} | tspin`

- Read from a file and print to `stdout` without paging:

`tspin {{path/to/file.log}} {{[-p|--print]}}`

- Follow a file (mimics `tail -f`) and highlight new entries:

`tspin {{[-f|--follow]}} {{path/to/file.log}}`

- Highlight specific groups only (possible values: `numbers`, `urls`, `pointers`, `dates`, `paths`, `quotes`, `key-value-pairs`, `uuids`, `ip-addresses`, `processes`, `json`):

`tspin --enable {{urls,ip-addresses,...}} {{path/to/file.log}}`

- Use a custom pager (the `[FILE]` string is a required literal placeholder):

`tspin --pager "{{bat -p}} [FILE]" {{path/to/file.log}}`

- Highlight custom strings with custom colors:

`tspin --highlight {{red}}:{{ERROR,WARNING,...}} {{path/to/file.log}}`

- Run the provided command and view the output in `less`:

`tspin --exec='{{command}}'`
