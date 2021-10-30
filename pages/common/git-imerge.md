# git-imerge

> Perform a merge or rebase between two Git branches incrementally.
> Conflicts between branches are tracked down to pairs of individual commits, to simplify conflict resolution.
> More information: <https://github.com/mhagger/git-imerge>.

- Start imerge-based rebase (checkout the branch to be rebased, first):

`git imerge rebase {{branch_to_rebase_onto}}`

- Start imerge-based merge (checkout the branch to merge into, first):

`git imerge merge {{branch_to_be_merged}}`

- Show ASCII diagram of in-progress merge or rebase:

`git imerge diagram`

- Continue imerge operation after resolving conflicts (`git add` the conflicted files, first):

`git imerge continue --no-edit`

- Wrap up imerge operation, after all conflicts are resolved:

`git imerge finish`

- Abort imerge operation, and return to the previous branch:

`git-imerge remove && git checkout {{previous_branch}}`
