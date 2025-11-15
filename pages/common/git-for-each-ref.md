# git for-each-ref

> List and optionally format references (branches, tags) in a Git repository.
> More information: <https://git-scm.com/docs/git-for-each-ref>.

- List all refs (branches and tags):

`git for-each-ref`

- List only branches:

`git for-each-ref refs/heads/`

- List only tags:

`git for-each-ref refs/tags/`

- Show branches merged into HEAD:

`git for-each-ref --merged HEAD refs/heads/`

- List short names of all refs:

`git for-each-ref --format "%(refname:short)"`

- Sort refs by committer date (most recent first):

`git for-each-ref --sort -committerdate`

- Sort refs by committer date (oldest first):

`git for-each-ref --sort committerdate`

- Limit output to a specified number of refs:

`git for-each-ref --count {{count}}`
