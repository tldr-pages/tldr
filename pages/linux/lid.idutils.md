# lid

> Query an ID database for tokens matching a pattern.
> Note: An ID database must first be built using `mkid`.
> More information: <https://www.gnu.org/software/idutils/manual/idutils.html#lid-invocation>.

- List all tokens and their file locations in the ID database:

`lid`

- Find files containing a specific token:

`lid {{token}}`

- Find tokens matching a pattern, ignoring case:

`lid {{[-i|--ignore-case]}} {{token}}`

- Find tokens matching an extended regular expression:

`lid {{[-r|--regexp]}} "{{pattern}}"`

- Output matching lines in grep-style format:

`lid {{[-R|--result]}} grep {{token}}`

- Find tokens that appear only once (useful for finding unused definitions):

`lid {{[-F|--frequency]}} 1`
