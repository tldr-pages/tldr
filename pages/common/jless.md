# jless

> Command-line JSON viewer for reading, exploring, and searching JSON data.
> See also: `jq`, `fx`, `less`.
> More information: <https://jless.io/user-guide>.

- Open a JSON file:

`jless {{path/to/file.json}}`

- Read JSON from `stdin`:

`cat {{path/to/file.json}} | jless`

- Force YAML parsing regardless of file extension:

`jless --yaml {{path/to/file}}`

- Start in line mode (show braces, commas, and quoted object keys):

`jless {{[-m|--mode]}} line {{path/to/file.json}}`

- Hide line numbers:

`jless {{[-N|--no-line-numbers]}} {{path/to/file.json}}`

- Show relative line numbers:

`jless {{[-r|--relative-line-numbers]}} {{path/to/file.json}}`

- Search forward for a pattern (press `<n>`/`<N>` for next/previous match):

`</>{{pattern}}`

- Exit:

`<q>`
