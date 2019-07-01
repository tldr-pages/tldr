# attrib

> Displays or changes file and directory attributes.

- Display the attributes of the files in the current directory:

`attrib`

- Display the attributes of the files in the current directory and sub-directories:

`attrib /S`

- Display the attributes of the files and directories in the current directory and sub-directories:

`attrib /S /D`

- Add the read-only attribute to a file:

`attrib +R {{document.txt}}`

- Remove the system and hidden attributes of a file:

`attrib -S -H {{document.txt}}`

- Add the hidden attribute to a directory:

`attrib +H {{path\to\directory}}`
