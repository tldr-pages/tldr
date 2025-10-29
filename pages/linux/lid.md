# lid

> Search for patterns in an ID database created by `mkid`.
> Part of GNU IDUtils.
> More information: <https://www.gnu.org/software/idutils/manual/html_node/lid-invocation.html>.

- Search for a token in the ID database:

`lid {{token}}`

- Search for files containing a specific regular expression:

`lid -r '{{regex_pattern}}'`

- Match tokens exactly (case-sensitive):

`lid -e {{token}}`

- Limit the number of results displayed:

`lid -l {{number}} {{token}}`

- Display database information (without searching):

`lid --statistics`

- Show version information:

`lid --version`
