# IFS

> IFS (Internal Field Separator) is a special environment variable that defines the delimiter used for word splitting in Unix shells.
> The default value of IFS is a space, tab, and newline. The three characters serve as delimiters.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html>.

- View the Current IFS Value:

`echo "$IFS"`

- Change the IFS Value:

`IFS=":"`

- Reset IFS to Default:

`IFS=$' \t\n'`

- Temporary IFS Change in a Subshell:

`(IFS=":"; echo "one:two:three")`
