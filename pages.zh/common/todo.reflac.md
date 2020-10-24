# reflac

> Recompress FLAC files in-place while preserving metadata.
> More information: <https://github.com/chungy/reflac>.

- Recompress a directory of FLAC files:

`reflac {{path/to/directory}}`

- Enable maximum compression (very slow):

`reflac --best {{path/to/directory}}`

- Display filenames as they are processed:

`reflac --verbose {{path/to/directory}}`

- Recurse into subdirectories:

`reflac --recursive {{path/to/directory}}`

- Perserve file modification times:

`reflac --preserve {{path/to/directory}}`
