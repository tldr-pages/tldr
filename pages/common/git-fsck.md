# git fsck

> Verify the validity and connectivity of nodes in a Git repository index.
> Does not make any modifications.
> See also: `git gc` for cleaning up dangling blobs.
> More information: <https://git-scm.com/docs/git-fsck>.

- Check the current repository:

`git fsck`

- List all tags found:

`git fsck --tags`

- List all root nodes found:

`git fsck --root`

- Show all unreachable and dangling objects, ignore reflogs, and perform a full integrity check:

`git fsck --dangling --no-reflogs --unreachable --full`

- Check connectivity only (skip object integrity verification):

`git fsck --connectivity-only`
