# git name-rev

> Describe a commit using existing ref names.
> More information: <https://git-scm.com/docs/git-name-rev>.

- Show name for HEAD:

`git name-rev HEAD`

- Show only the name:

`git name-rev --name-only HEAD`

- Enumerate all matching ref names:

`git name-rev --all`

- Use only tags to name the commit:

`git name-rev --tags HEAD`

- Prevent ‘undefined’ output for unknown commits:

`git name-rev --no-undefined {{commit-ish}}`

- Show names for multiple commits:

`git name-rev HEAD~1 HEAD~2 main`

- Restrict names to branch refs:

`git name-rev --refs refs/heads/ {{commit-ish}}`

- Read commit IDs from standard input:

`echo "{{commit-ish}}" | git name-rev --annotate-stdin`
