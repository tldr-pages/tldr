# egrep

> Search files using extended regular expressions.
> This command is an alias of `grep --extended-regexp`.
> More information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Search for a pattern in a file using extended `regex`:

`egrep "{{pattern}}" {{file}}`

- Search recursively in a directory:

`egrep -r "{{pattern}}" {{directory}}`

- Show line numbers of matching lines:

`egrep -n "{{pattern}}" {{file}}`

- Ignore case distinctions:

`egrep -i "{{pattern}}" {{file}}`

- Show only the matched parts of a line:

`egrep -o "{{pattern}}" {{file}}`

- View documentation for the original command:

`tldr grep`
