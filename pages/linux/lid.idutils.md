# lid

> Query an `idutils` ID database for identifiers.
> More information: <https://www.gnu.org/software/idutils/manual/html_node/lid-invocation.html>.

- Search for a token using a literal match:

`lid {{token}}`

- Search case-insensitively:

`lid --ignore-case {{token}}`

- Search using an extended regular expression:

`lid --regexp "{{regular_expression}}"`

- Treat the pattern as a literal even if it contains regex metacharacters:

`lid --literal "{{pattern_with_special_characters}}"`

- Show only tokens that appear within a frequency range:

`lid --frequency={{1..}} {{token}}`

- Output matching lines in `grep` style:

`lid --result={{grep}} {{token}}`
