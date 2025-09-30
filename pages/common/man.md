# man

> Format and display manual pages.
> More information: <https://manned.org/man>.

- Display the man page for a command:

`man {{command}}`

- Open the man page for a command in a browser (`BROWSER` environment variable can replace `=browser_name`):

`man {{[-H|--html=]}}{{browser_name}} {{command}}`

- Display the man page for a command from section 7:

`man 7 {{command}}`

- List all available sections for a command:

`man {{[-f|--whatis]}} {{command}}`

- Display the path searched for manpages:

`man {{[-w|--path]}}`

- Display the location of a manpage rather than the manpage itself:

`man {{[-w|--where]}} {{command}}`

- Display the man page using a specific locale:

`man {{[-L|--locale]}} {{locale}} {{command}}`

- Search for manpages containing a search string:

`man {{[-k|--apropos]}} "{{search_string}}"`
