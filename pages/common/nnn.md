# nnn

> Interactive terminal file manager and disk usage analyzer.
> More information: <https://github.com/jarun/nnn/wiki/Usage#program-options>.

- Open the current directory (or specify one as the first argument):

`nnn`

- Start in [d]etailed mode:

`nnn -d`

- Show [H]idden files:

`nnn -H`

- Open an existing [b]ookmark (defined in the `$NNN_BMS` environment variable):

`nnn -b {{bookmark_name}}`

- Sort files on [a]pparent disk usage / [d]isk usage / [e]xtension / [r]everse / [s]ize / [t]ime / [v]ersion:

`nnn -T {{a|d|e|r|s|t|v}}`

- Open a file you have selected. Select the file then press `<o>`, and type a program to open the file in:

`nnn -o`
