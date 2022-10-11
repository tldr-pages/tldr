# xzdiff

> Invokes the diff command on files compressed with xz, lzma, gzip, bzip2, lzop, or zstd.
> All options specified are passed directly to diff.
> More information: <https://manned.org/xzdiff.1>.

- Compare files:

`xzdiff {{path/to/file1}} {{path/to/file2}}`

- Compare files, showing the differences side by side:

`xzdiff -y {{path/to/file1}} {{path/to/file2}}`

- Compare files and report only that they differ (no details on what is different):

`xzdiff -q {{path/to/file1}} {{path/to/file2}}`

- Compare files and report when the files are the same:

`xzdiff -s {{path/to/file1}} {{path/to/file2}}`

- Compare files and paginate results:

`xzdiff -l {{path/to/file1}} {{path/to/file2}}`

- Compare directories recursively (shows names for differing files/directories as well as changes made to files):

`diff -r {{path/to/file1}} {{path/to/file2}}`
