# metaflac

> View and edit metadata in FLAC audio files.
> See also: `flac`.
> More information: <https://xiph.org/flac/documentation_tools_metaflac.html>.

- Show all tags in a FLAC file:

`metaflac --show-all-tags {{path/to/file.flac}}`

- Show one or more specific tags from a FLAC file:

`metaflac --show-tag {{tag_name1}} --show-tag {{tag_name2}} {{path/to/file.flac}}`

- Set a tag in a FLAC file (the argument must be in `NAME=VALUE` format):

`metaflac --set-tag "{{tag_name}}={{tag_value}}" {{path/to/file.flac}}`

- Remove all tags with a specific name from a FLAC file:

`metaflac --remove-tag {{tag_name}} {{path/to/file.flac}}`

- Remove all tags from a FLAC file:

`metaflac --remove-all-tags {{path/to/file.flac}}`

- Import tags from a file (one `NAME=VALUE` pair per line):

`metaflac --import-tags-from {{path/to/tags.txt}} {{path/to/file.flac}}`

- List all metadata blocks in a FLAC file:

`metaflac --list {{path/to/file.flac}}`

- Show the sample rate and number of channels from a FLAC file:

`metaflac --show-sample-rate --show-channels {{path/to/file.flac}}`
