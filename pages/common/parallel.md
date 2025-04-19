# parallel

> Run commands on multiple CPU cores.
> More information: <https://www.gnu.org/software/parallel>.

- Gzip several files at once, using all cores:

`parallel gzip ::: {{path/to/file1 path/to/file2 ...}}`

- Read arguments from `stdin`, run 4 jobs at once:

`ls *.txt | parallel {{[-j|--jobs]}} 4 gzip`

- Convert JPEG images to PNG using replacement strings:

`parallel convert {} {.}.png ::: *.jpg`

- Parallel xargs, cram as many args as possible onto one command:

`{{args}} | parallel -X {{command}}`

- Break `stdin` into ~1M blocks, feed each block to `stdin` of new command:

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- Run on multiple machines via SSH:

`parallel {{[-S|--sshlogin]}} {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`

- Download 4 files simultaneously from a text file containing links showing progress:

`parallel {{[-j|--jobs]}} 4 --bar --eta wget {{[-q|--quote]}} {} :::: {{path/to/links.txt}}`

- Print the jobs which `parallel` is running in `stderr`:

`parallel {{[-t|--verbose]}} {{command}} ::: {{args}}`
