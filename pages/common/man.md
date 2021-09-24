# man

> Format and display manual pages.
> More information: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- Display the man page for a command:

`man {{command}}`

- Display the man page for a command from section 7:

`man {{7}} {{command}}`

- Display the path searched for manpages:

`man --path`

- Display the location of a manpage rather than the manpage itself:

`man -w {{command}}`

- Display the man page using a specific locale:

`man {{command}} --locale={{locale}}`

- Search for manpages containing a search string:

`man -k "{{search_string}}"`
