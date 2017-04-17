# [shred](http://man7.org/linux/man-pages/man1/shred.1.html)
> Overwrite files to securely delete data.

- Overwrite a file:

`shred {{file}}`

- Overwrite a file, leaving zeroes instead of random data:

`shred --zero {{file}}`

- Overwrite a file 25 times:

`shred -n25 {{file}}`

- Overwrite a file and remove it:

`shred --remove {{file}}`
