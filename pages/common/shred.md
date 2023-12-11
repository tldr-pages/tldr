# shred

> Overwrite files to securely delete data.
> More information: <https://www.gnu.org/software/coreutils/shred>.

- Overwrite a file:

`shred {{path/to/file}}`

- Overwrite a file and show progress on the screen:

`shred -v {{path/to/file}}`

- Overwrite a file, leaving zeros instead of random data:

`shred -z {{path/to/file}}`

- Overwrite a file 25 times:

`shred -n25 {{path/to/file}}`

- Overwrite a file and remove it:

`shred -u {{path/to/file}}`

- Overwrite a file 100 times, add a final overwrite with zeros, remove the file after overwriting it and show progress on the screen:

`shred -vzun100 {{path/to/file}}`
