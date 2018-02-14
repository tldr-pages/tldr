# detox

> Renames files to make them easier to work with. It removes spaces 
> and other such annoyances like duplicate underline characters. 
> It will also translate or cleanup Latin-1 (ISO 8859-1) characters 
> encoded in 8-bit ASCII, Unicode characters encoded in UTF-8, 
> and CGI escaped characters.

- Remove spaces and other undesirable characters from a file's name:

`detox {{file}}`

- Show how detox would rename all of the files in a directory tree:

`detox -n -r {{directory}}`

- Remove spaces and other undesirable characters from all files in a directory tree:

`detox -r {{directory}}`
