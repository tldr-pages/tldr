# git shortlog

> Summarizes the `git log` output.
> More information: <https://git-scm.com/docs/git-shortlog>.

- View a summary of all the commits made, grouped alphabetically by author name:

`git shortlog`

- View a summary of all the commits made, sorted by the number of commits made:

`git shortlog {{--numbered|-n}}`

- View a summary of all the commits made, grouped by the committer identities (name and email):

`git shortlog {{--committer|-c}}`

- View a summary of the last 5 commits (i.e. specify a revision range):

`git shortlog HEAD~{{5}}..HEAD`

- View all users, emails and the number of commits in the current branch:

`git shortlog {{--summary|-s}} {{--numbered|-n}} {{--email|-e}}`

- View all users, emails and the number of commits in all branches:

`git shortlog {{--summary|-s}} {{--numbered|-n}} {{--email|-e}} --all`
