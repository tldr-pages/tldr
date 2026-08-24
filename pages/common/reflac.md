# reflac

> Recompress FLAC files in-place while preserving metadata.
> More information: <https://github.com/chungy/reflac#running>.

- Recompress a directory of FLAC files:

`reflac {{path/to/directory}}`

- Enable maximum compression (very slow):

`reflac {{[-8|--best]}} {{path/to/directory}}`

- Display filenames as they are processed:

`reflac {{[-v|--verbose]}} {{path/to/directory}}`

- Recurse into subdirectories:

`reflac {{[-r|--recursive]}} {{path/to/directory}}`

- Preserve file modification times:

`reflac --preserve {{path/to/directory}}`
