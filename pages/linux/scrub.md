# scrub

> Securely overwrite files, block devices, or free disk space.
> More information: <https://manned.org/scrub>.

- Securely overwrite a file using the default overwrite pattern:

`scrub {{path/to/file}}`

- Securely overwrite multiple files:

`scrub {{path/to/file1 path/to/file2 ...}}`

- Securely overwrite a block device or partition:

`sudo scrub {{/dev/sdX}}`

- Securely overwrite a file with a single-pass overwrite pattern:

`scrub {{[-p|--pattern]}} random {{path/to/file}}`

- Securely overwrite a file using the DoD 5220.22-M overwrite pattern:

`scrub {{[-p|--pattern]}} dod {{path/to/file}}`

- Securely overwrite a file using the Gutmann overwrite pattern:

`scrub {{[-p|--pattern]}} gutmann {{path/to/file}}`

- Remove a file after successfully overwriting it:

`scrub {{[-r|--remove]}} {{path/to/file}}`

- Securely overwrite free space in a directory:

`scrub {{[-X|--freespace]}} {{path/to/directory}}`
