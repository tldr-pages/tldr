# git fame

> Pretty-print Git repository contributions.
> More information: <https://github.com/casperdcl/git-fame>.

- Calculate contributions for the current Git repository:

`git fame`

- Exclude files/directories that match the specified regular expression:

`git fame --excl "{{regular_expression}}"`

- Calculate contributions made after the specified date:

`git fame --since "{{3 weeks ago|2021-05-13}}"`

- Display contributions in the specified format:

`git fame --format {{pipe|md|markdown|yaml|yml|json|csv|tsv|tabulate}}`

- Display contributions per file extension:

`git fame --bytype`

- Do not display progress bar:

`git fame --silent-progress`
