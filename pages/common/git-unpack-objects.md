# git unpack-objects

> Git command for unpacking objects from a packed archive.
> More information: <https://git-scm.com/docs/git-unpack-objects>.

- Simulate the pack file without unpacking objects:

`git < {{pack-file.pack}} unpack-objects -n`

- Suppress percentage progress typically shown by the command:

`git < {{pack-file.pack}} unpack-objects -q`

- Unpack a corrupt packfile beyond the first corruption:

`git < {{pack-file.pack}} unpack-objects -r`

- Don't write objects containing broken content or links:

`git < {{pack-file.pack}} unpack-objects --strict`

- Die, given a pack larger than `size`:

`git < {{pack-file.pack}} unpack-objects --max-input-size={{size}}`
