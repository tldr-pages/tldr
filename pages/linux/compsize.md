# compsize

> Calculate the compression ratio of a set of files on a btrfs filesystem.
> See also `btrfs filesystem` for recompressing a file by defragmenting it.
> More information: <https://github.com/kilobyte/compsize>.

- Calculate the current compression ratio for a file or directory:

`sudo compsize {{path/to/file_or_directory}}`

- Don't traverse filesystem boundaries:

`sudo compsize --one-file-system {{path/to/file_or_directory}}`

- Show raw byte counts instead of human-readable sizes:

`sudo compsize --bytes {{path/to/file_or_directory}}`
