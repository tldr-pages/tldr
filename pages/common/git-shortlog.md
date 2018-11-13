# git shortlog

> Summarizes the `git log` output.

- View a summary of all the commits made, grouped alphabetically by author name:

`git shortlog`

- View a summary of all the commits made, sorted by the number of commits made:

`git shortlog -n`

- View a summary of all the commits made, grouped by the commiter identities (name and email):

`git shortlog -c`

- View a summary of the last 5 commits (i.e. specify a revision range):

`git shortlog HEAD~{{5}}..HEAD`
