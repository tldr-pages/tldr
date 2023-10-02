# IFS

> IFS (Internal Field Separator) is a special environment variable that defines the delimiter used for word splitting in Unix shells.
> The default value of IFS is a space, tab, and newline. The three characters serve as delimiters.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html>.

- View the current IFS value:

`echo "$IFS"`

- Change the IFS value:

`IFS="{{:}}"`

- Reset IFS to default:

`IFS=$' \t\n'`

- Temporarily change the IFS value in a subshell:

`(IFS="{{:}}"; echo "{{one:two:three}}")`
