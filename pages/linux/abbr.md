# abbr

> Manage abbreviations for the fish shell.
> User-defined words are replaced with longer phrases after they are entered.  
> More information: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Add a new abbreviation:

`abbr --add gco git checkout`

- Rename an existing abbreviation:

`abbr --rename gco gch`

- Erase an existing abbreviation:

`abbr --erase gco`

- Import the abbreviations defined on another_host over SSH.:

`ssh another_host abbr -s | source`
