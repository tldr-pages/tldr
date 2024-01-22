# uuidparse

> Parse universally unique identifiers.
> More information: <https://manned.org/uuidparse.1>.

- Parse the specified UUIDs, use a tabular output format:

`uuidparse {{uuid1 uuid2 ...}}`

- Parse UUIDs from `stdin`:

`{{command}} | uuidparse`

- Use the JSON output format:

`uuidparse --json {{uuid1 uuid2 ...}}`

- Do not print a header line:

`uuidparse --noheadings {{uuid1 uuid2 ...}}`

- Use the raw output format:

`uuidparse --raw {{uuid1 uuid2 ...}}`

- Display help:

`uuidparse -h`
