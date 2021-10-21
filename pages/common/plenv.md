# plenv

> Easily switch between multiple versions of Perl.
> More information: <https://github.com/tokuhirom/plenv>.

- Show general usage and briefly describe the available commands:

`plenv`

- Show more detailed help for a specific command:

`plenv help {{command}}`

- Show the currently selected Perl version and how it was selected:

`plenv version`

- List all available installed Perl versions:

`plenv versions`

- Set the global Perl version (used unless a local or shell version takes priority):

`plenv global {{version}}`

- Set the local application-specific Perl version (used in the current directory and all directories below it):

`plenv local {{version}}`

- Set the shell-specific Perl version (used for the current session only):

`plenv shell {{version}}`
