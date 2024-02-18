# gocr

>  Optical Character Recognition tool
> More information: <https://manned.org/gocr.1>.

- Recognize characters in the [i]nput image and [o]utput it in the given file. Put the database [p] in ./db/. [m]ode 130 means create + use + extend database:

`gocr -m 130 -p ./db/ -i {{input/image.png}} -o {{output/file.txt}}`

- Recognize characters, and assume all characters are numbers [C]:
`gocr -m 130 -p ./db/ -i {{input/image.png}} -o {{output/file.txt}} -C "0-9"`

- Recognize characters with a cert[a]inty of 100% (characters have a higher chance to be treated as unknown):
`gocr -m 130 -p ./db/ -i {{input/image.png}} -o {{output/file.txt}} -a 100`
