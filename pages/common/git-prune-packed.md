# git prune-packed

> Remove loose objects that already exist in a pack file.
> More information: <https://git-scm.com/docs/git-prune-packed>.

- Remove all loose objects that are already packed:

`git prune-packed`

- Show which loose objects would be removed, without actually removing them:

`git prune-packed --dry-run`

- Remove loose objects that are already packed, without showing progress:

`git prune-packed --quiet`
