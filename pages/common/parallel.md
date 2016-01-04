# GNU Parallel

> Run commands on multiple CPU cores

- gzip several files at once, using all cores

`parallel gzip ::: {{file1}} {{file2}} {{file3}}`

- read arguments from stdin, run 4 jobs at once

`ls *.txt | parallel -j4 gzip`

- Convert JPG images to PNG using replacement strings

`parallel convert {} {.}.png ::: *.jpg`

- parallel xargs, cram as many args as possible onto one command

`{{args}} | parallel -X {{command}}`

- break stdin into ~1M blocks, feed each block to stdin of new command

`cat {{bigfile.txt}} | parallel --pipe --block 1M {{command}}`

- run on multiple machines via SSH

`parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`
