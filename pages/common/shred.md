# shred

> Overwrite files to securely delete data.
> More information: <https://www.gnu.org/software/coreutils/shred>.

- Overwrite a file:

`shred {{path/to/file}}`

- Overwrite a file and show progress on the screen:

`shred --verbose {{path/to/file}}`

- Overwrite a file, leaving [z]eros instead of random data:

`shred --zero {{path/to/file}}`

- Overwrite a file a specific [n]umber of times:

`shred --iterations {{25}} {{path/to/file}}`

- Overwrite a file and remove it:

`shred -u {{path/to/file}}`

- Overwrite a file 100 times, add a final overwrite with zeros, remove the file after overwriting it and show progress on the screen:

`shred -vzun100 {{path/to/file}}`
