# xzcat
> A general purpose data compression tool similar to gzip and bzip2 syntaxes.
> Compress or decompress .xz and .lzma files.
> More information: <https://www.unix.com/man-page/linux/1/xzcat/>.
- Force compress:
`xzcat -z {{path/to/file}}`

- Force [d]ecompress:

`xzcat -d {{path/to/file}}`

- [t]est compressed file integrity:

`xzcat -t {{path/to/file}}`

- [l]ist information about the .xz file:

`xzcat -l {{path/to/file}}`

- [k]eep/Avoid deleting input files:

`xzcat -k {{path/to/file}}`

- [f]orce overwrite output files and decompress links:

`xzcat -f {{path/to/file}}`

- [e]xtreme compression using more CPU time:

`xzcat -e {{path/to/file}}`

- Keep warnings [q]uiet. (Specify twice to keep warnings and errors quiet):

`xzcat -q {{path/to/file}}`
