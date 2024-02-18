# gocr

>  Optical Character Recognition tool
> Recognize characters using its engine, and prompt the user for unknown patterns to store them in a daabase
> More information: <https://manned.org/gocr.1>.

- Recognize characters in the [i]nput image and [o]utput it in the given file. Put the database [p] in {{./existing/db/folder/}} (verify that the folder exists or db usage will silently be skipped). [m]ode 130 means create + use + extend database:

`gocr -m 130 -p {{./exising/db/folder/}} -i {{input/image.png}} -o {{output/file.txt}}`

- Recognize characters, and assume all characters are numbers [C]:
`gocr -m 130 -p {{./existing/db/folder/}} -i {{input/image.png}} -o {{output/file.txt}} -C "0-9"`

- Recognize characters with a cert[a]inty of 100% (characters have a higher chance to be treated as unknown):
`gocr -m 130 -p {{./existing/db/folder/}} -i {{input/image.png}} -o {{output/file.txt}} -a 100`
