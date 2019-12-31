# git diff

> Show changes to tracked files.
> More information: <https://git-scm.com/docs/git-diff>.

- Show unstaged, uncommitted changes:

`git diff`

- Show all uncommitted changes (including staged ones):

`git diff HEAD`

- Show only staged (added, but not yet committed) changes:

`git diff --staged`

- Show changes from all commits since a given date/time (a date expression, e.g. "1 week 2 days" or an ISO date):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Show only names of changed files since a given commit:

`git diff --name-only {{commit}}`

- Output a summary of file creations, renames and mode changes since a given commit:

`git diff --summary {{commit}}`

- Create a patch file:

`git diff > {{target_file}}.patch`

- Compare a single file between two branches or commits:

`git diff {{branch_1}}..{{branch_2}} [--] {{path/to/file}}`

- Compare different files from the current branch to other branch:

`git diff {{branch}}:{{path/to/file2}} {{path/to/file}}`
