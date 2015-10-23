# touch

> Change a file access and modification times (atime, mtime)

- Create a new empty file(s) or change the times for existing file(s) to current time.`

`touch {{filename}}`

- Set the times on a file to those specified

`touch -t 201412250801.59 {{filename}}
`touch -t {{YYYYMMDDHHMM.SS}} {{filename}}

- Set the times on a file to match those on second file

`touch -r {{filename2}} {{filename}}`
