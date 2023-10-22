# shred

> Overwrite files to securely delete data.
> More information: <https://www.gnu.org/software/coreutils/shred>.

- Overwrite a file:

`shred {{path/to/file}}`

- Overwrite a file, leaving zeroes instead of random data:

`shred --zero {{path/to/file}}`

- Overwrite a file 25 times:

`shred -n25 {{path/to/file}}`

- Overwrite a file and remove it:

`shred --remove {{path/to/file}}`
