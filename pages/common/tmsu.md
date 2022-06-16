# tmsu

> Simple command-line tool for tagging files. 
> More information: https://tmsu.org.

- Tag a file:

`tmsu tag summer.mp3 music big-jazz mp3`

- Tag multiple files:

`tmsu tag --tags "music mp3" *.mp3`

- List tags of specified file(s):

`tmsu tags *.mp3`

- List files with specified tag(s):

`tmsu files big-jazz music`

- List files with tags matching boolean expression:

`tmsu files "(year >= 1990 and year <= 2000) and grunge"`

- Mount virtual filesystem to existing directory:

`tmsu mount ./tmsu-virtual-fs`
