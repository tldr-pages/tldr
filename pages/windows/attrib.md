# attrib

> Displays or changes file and directories attributes.

- Display the permission of the files in current directory:

`attrib`

- Display the permission of the files in current directory and sub-directories:

`attrib /S`

- Display the permission of the files and folders in current directory and sub-directories:

`attrib /S /D`

- Add read-only attribute to file:

`attrib +R {{document.txt}}`

- Remove system and hidden atrtibute of a file:

`attrib -S -H {{document.txt}}`

- Add hidden attribute to a folder:

`attrib +H {{path\to\folder}}`
