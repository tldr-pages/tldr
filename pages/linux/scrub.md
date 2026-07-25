# scrub

> Securely overwrite files, block devices, or free disk space.
> More information: <https://manned.org/scrub>.

- Securely overwrite a file using the default overwrite pattern:

`scrub {{path/to/file}}`

- Securely overwrite multiple files:

`scrub {{path/to/file1 path/to/file2 ...}}`

- Securely overwrite a block device or partition:

`sudo scrub {{/dev/sdX}}`

- Securely overwrite a file using a single overwrite pattern:

`scrub {{[-p|--pattern]}} 1 {{path/to/file}}`

- Securely overwrite a file using the DoD 5220.22-M overwrite pattern:

`scrub -p dod {{path/to/file}}`

- Securely overwrite a file using the Gutmann overwrite pattern:

`scrub -p gutmann {{path/to/file}}`

- [R]emove a file after successfully overwriting it:

`scrub -r {{path/to/file}}`

- Display help:

`scrub --help`
