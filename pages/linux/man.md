# man

> Format and display manual pages.
> More information: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- Display the man page for a command:

`man {{command}}`

- Display the man page for a command from section 7:

`man {{7}} {{command}}`

- List all available sections for a command:

`man --whatis {{command}}`

- Display the path searched for manpages:

`man --path`

- Display the location of a manpage rather than the manpage itself:

`man --where {{command}}`

- Display the man page using a specific locale:

`man --locale={{locale}} {{command}}`

- Search for manpages containing a search string:

`man --apropos "{{search_string}}"`
