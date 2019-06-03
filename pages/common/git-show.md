# git show

> Show various types of git objects (commits, tags, etc.).
> More information: <https://git-scm.com/docs/git-show>.

- Show information about the latest commit (message, changes, and other metadata):

`git show`

- Show information about a given commit:

`git show {{commit}}`

- Show information about the commit associated with a given tag:

`git show {{tag}}`

- Show information about the 3rd commit from the tip of a branch:

`git show {{branch}}~{{3}}`

- Show a commit's hash and message in a single line, suppressing the diff output:

`git show --oneline -s {{commit}}`
