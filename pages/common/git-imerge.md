# git-imerge

> Perform a merge or rebase between two git branches incrementally.
> Conflicts between branches are tracked down to pairs of individual commits, to simplify conflict resolution.

- Start imerge-based rebase (checkout the branch to rebase first):

`git imerge rebase {{target_root_branch}}`

- Start imerge-based merge (checkout the branch to merge into, first):

`git imerge merge {{branch_to_merge}}`

- Show ASCII diagram of in-progress merge or rebase:

`git imerge diagram`

- Continue imerge operation after resolving conflicts (`git add` the conflicted files first):

`git imerge continue --no-edit`

- Wrap up the imerge operation, after all conflicts are resolved:

`git imerge finish`
