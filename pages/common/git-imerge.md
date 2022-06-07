# git-imerge

> Perform an incremental merge or rebase between two Git branches.
> Conflicts between branches are tracked down to pairs of individual commits, to simplify conflict resolution.
> More information: <https://github.com/mhagger/git-imerge>.

- Start imerge-based rebase (checkout the branch to be rebased, first):

`git-imerge rebase {{branch_to_rebase_onto}}`

- Start imerge-based merge (checkout the branch to merge into, first):

`git-imerge merge {{branch_to_be_merged}}`

- Show ASCII diagram of in-progress merge or rebase:

`git-imerge diagram`

- Continue imerge operation after resolving conflicts (`git add` the conflicted files, first):

`git-imerge continue`

- Finish a merge or a rebase, after all conflicts are resolved:

`git-imerge finish`

- Abort imerge operation and clean up temporary commits:

`git-imerge remove`
