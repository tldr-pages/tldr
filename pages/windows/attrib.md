# attrib

> Displays or changes file and directories attributes.

- Display the attributes of the files in current directory:

`attrib`

- Display the attributes of the files in current directory and sub-directories:

`attrib /S`

- Display the attributes of the files and folders in current directory and sub-directories:

`attrib /S /D`

- Add the read-only attribute to a file:

`attrib +R {{document.txt}}`

- Remove the system and hidden atrtibutes of a file:

`attrib -S -H {{document.txt}}`

- Add the hidden attribute to a folder:

`attrib +H {{path\to\folder}}`
