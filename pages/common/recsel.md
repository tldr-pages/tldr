# recsel

> Print records from a human-editable, plain text database called a recfile.
> More information <https://www.gnu.org/software/recutils/manual/recutils.html>.

- Extract name and version field from the output of guix:

`guix package -s malloc | recsel -p name,version`

- Use "~" to match a string with a given regular expression:

`guix package -s python | recsel -e "name  ~ 'numpy$'"`

- Use a predicate to match a name and a version:

`guix search python | recsel -e "name ~ 'numpy$' && version ~ '^1\.1.*'"`
