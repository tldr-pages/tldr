# git patch-id

> Compute unique IDs for patches, ignoring line numbers and whitespace.
> Useful for finding commits that introduce the same change, such as cherry-picked commits.
> More information: <https://git-scm.com/docs/git-patch-id>.

- Compute the patch ID of a specific commit:

`git show {{commit}} | git patch-id`

- Compute the patch ID of a patch file:

`git patch-id < {{path/to/file.patch}}`

- Compute the patch IDs of all commits in a range:

`git log --patch {{commit1}}..{{commit2}} | git patch-id`

- Compute a patch ID that does not depend on the order of files in the patch:

`git show {{commit}} | git patch-id --stable`

- Compute a patch ID without ignoring whitespace changes:

`git show {{commit}} | git patch-id --verbatim`
