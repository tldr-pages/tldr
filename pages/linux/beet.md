# beet

> Manage the beets media library.
> More information: <https://beets.readthedocs.io/en/stable/reference/cli.html>.

- Add music to your library, attempting to get correct tags for it from MusicBrainz:

`beet import {{path/to/directory}}`

- Add a single song to your library, attempting to get correct tags for it from MusicBrainz:

`beet import {{[-s|--singletons]}} {{path/to/file}}`

- Query library:

`beet list {{query}}`

- Show entire library statistics:

`beet stats`

- Show statistics for a specific query:

` beet stats {{query}}`
