# git unpack-objects

> Git command for unpacking objects from a packed archive.
> More information: <https://git-scm.com/docs/git-unpack-objects>.

- Simulate the pack file without unpacking objects:

`git unpack-objects -n`

- Suppress percentage progress typically shown by the command:

`git unpack-objects -q`

- Unpack a corrupt packfile beyond the first corruption:

`git unpack-objects -r`

- Don't write objects containing broken content or links:

`git unpack-objects --strict`

- Die, given a pack larger than `size`:

`git unpack objects {{[--max-input-size=<size>]}}`
