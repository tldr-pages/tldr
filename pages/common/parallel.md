# parallel

> Run commands on multiple CPU cores.
> More information: <https://www.gnu.org/software/parallel>.

- Gzip several files at once, using all cores:

`parallel gzip ::: {{file1}} {{file2}} {{file3}}`

- Read arguments from `stdin`, run 4 jobs at once:

`ls *.txt | parallel -j4 gzip`

- Convert JPG images to PNG using replacement strings:

`parallel convert {} {.}.png ::: *.jpg`

- Parallel xargs, cram as many args as possible onto one command:

`{{args}} | parallel -X {{command}}`

- Break `stdin` into ~1M blocks, feed each block to `stdin` of new command:

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- Run on multiple machines via SSH:

`parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`
