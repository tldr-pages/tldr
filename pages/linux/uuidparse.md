# uuidparse

> Parse universally unique identifiers.
> See also: `uuidgen`.
> More information: <https://manned.org/uuidparse>.

- Parse the specified UUIDs, use a tabular output format:

`uuidparse {{uuid1 uuid2 ...}}`

- Parse UUIDs from `stdin`:

`{{command}} | uuidparse`

- Use the JSON output format:

`uuidparse {{[-J|--json]}} {{uuid1 uuid2 ...}}`

- Do not print a header line:

`uuidparse {{[-n|--noheadings]}} {{uuid1 uuid2 ...}}`

- Use the raw output format:

`uuidparse {{[-r|--raw]}} {{uuid1 uuid2 ...}}`

- Specify which of the four output columns to print:

`uuidparse {{[-o|--output]}} {{UUID,VARIANT,TYPE,TIME}}`

- Display help:

`uuidparse {{[-h|--help]}}`
