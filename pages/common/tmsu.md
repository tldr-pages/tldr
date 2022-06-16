# tmsu

> Simple command-line tool for tagging files. 
> More information: https://tmsu.org.

- Apply tags to a single file:

`tmsu tag summer.mp3 music big-jazz mp3`

- Apply tags to multiple files:

`tmsu tag --tags "music mp3" *.mp3`

- List file's or multiple files' tags:

`tmsu tags *.mp3`

- List all files with specified tag(s):

`tmsu files big-jazz music`

- List all files matching boolean expression:

`tmsu files "(year >= 1990 and year <= 2000) and grunge"`

- Mount virtual filesystem at existing location:

`tmsu mount ./tmsu-virtual-fs`
