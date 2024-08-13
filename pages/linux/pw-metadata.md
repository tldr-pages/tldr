# pw-metadata

> Monitor, set, and delete metadata on PipeWire objects.
> See also: `pipewire`, `pw-mon`, `pw-cli`.
> More information: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- Show metadata in `default` name:

`pw-metadata`

- Show metadata with ID 0 in `settings`:

`pw-metadata {{-n|--name}} {{settings}} {{0}}`

- List all available metadata objects:

`pw-metadata {{-l|--list}}`

- Keep running and log the changes to the metadata:

`pw-metadata {{-m|--monitor}}`

- Delete all metadata:

`pw-metadata {{-d|--delete}}`

- Set `log.level` to 1 in `settings`:

`pw-metadata --name {{settings}} {{0}} {{log.level}} {{1}}`

- Display help:

`pw-metadata --help`
