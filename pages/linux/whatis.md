# whatis

> Display one-line descriptions from manual pages.

- Display a description from a man page:

`whatis {{command}}`

- Don't cut the description off at the end of the line:

`whatis --long {{command}}`

- Display descriptions for all commands matching a glob:

`whatis --wildcard {{command_glob}}`

- Search man page descriptions with a regular expression:

`whatis --regex {{regular_expression}}`
