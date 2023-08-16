# xzdiff

> Invokes `diff` on files compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`.
> All options specified are passed directly to `diff`.
> More information: <https://manned.org/xzdiff>.

- Compare files:

`xzdiff {{path/to/file1}} {{path/to/file2}}`

- Compare files, showing the differences side by side:

`xzdiff --side-by-side {{path/to/file1}} {{path/to/file2}}`

- Compare files and report only that they differ (no details on what is different):

`xzdiff --brief {{path/to/file1}} {{path/to/file2}}`

- Compare files and report when the files are the same:

`xzdiff --report-identical-files {{path/to/file1}} {{path/to/file2}}`

- Compare files using paginated results:

`xzdiff --paginate {{path/to/file1}} {{path/to/file2}}`
