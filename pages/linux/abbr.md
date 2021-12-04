# abbr

> Manages abbreviations for the fish shell
> User-defined words are replaced with longer phrases after they are entered.
> More information: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Add a new abbreviation:

`abbr -a -g gco git checkout`

- Rename an existing abbreviation:

`abbr -r gco gch`

- Erase an existing abbreviation:

`abbr -e gco`

- Import the abbreviations defined on another_host over SSH.:

`ssh another_host abbr -s | source`
