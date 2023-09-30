# IFS

> In Linux and Unix-like operating systems, the IFS (Internal Field Separator) is a special environment variable that defines the delimiter used for word splitting and parsing strings in the shell.
> The default value of IFS is a space, tab, and newline (space, tab, and newline characters are used as delimiters).
> More information: <https://www.baeldung.com/linux/ifs-shell-variable>.

- View the Current IFS Value:

`echo "$IFS"`

- Change the IFS Value:

`IFS=":"`

- Reset IFS to Default:

`IFS=$' \t\n'`

- Temporary IFS Change in a Subshell:

`(IFS=":"; echo "one:two:three")`
