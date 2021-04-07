# git range-diff

> Compare two commit ranges (e.g. two versions of a branch)
> More information: <https://git-scm.com/docs/git-range-diff>

- Diff the diffs of commit1 and commit2:

`git range-diff {{commit1}}~..{{commit1} {{commit2}}~..{{commit2}}`

- Diff the changes of ours and theirs from their common ancestor:

`git range-diff {{theirs}}...{{ours}}`
