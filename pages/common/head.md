# head

> Output the first part of files.
> More information: <https://www.gnu.org/software/coreutils/head>.

- Output the first few lines of a file:

`head -n {{count_of_lines}} {{filename}}`

- Output the first few bytes of a file:

`head -c {{size_in_bytes}} {{filename}}`

- Output everything but the last few lines of a file:

`head -n -{{count_of_lines}} {{filename}}`

- Output everything but the last few bytes of a file:

`head -c -{{size_in_bytes}} {{filename}}`
