# fallocate

> Reserve or deallocate disk space to files.
> The utility allocates space without zeroing.
> More information: <https://manned.org/fallocate>.

- Reserve a file taking up 700 MiB of disk space:

`fallocate {{[-l|--length]}} 700M {{path/to/file}}`

- Shrink an already allocated file by 200 MB:

`fallocate {{[-c|--collapse-range]}} {{[-l|--length]}} 200MB {{path/to/file}}`

- Shrink 20 MB of space after 100 MiB in a file:

`fallocate {{[-c|--collapse-range]}} {{[-o|--offset]}} 100M {{[-l|--length]}} 20M {{path/to/file}}`
