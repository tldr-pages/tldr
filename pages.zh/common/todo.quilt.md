# quilt

> Tool to manage a series of patches.
> More information: <https://savannah.nongnu.org/projects/quilt>.

- Import an existing patch from a file:

`quilt import {{path/to/filename.patch}}`

- Create a new patch:

`quilt new {{filename.patch}}`

- Add a file to the current patch:

`quilt add {{path/to/file}}`

- After editing the file, refresh the current patch with the changes:

`quilt refresh`

- Apply all the patches in the series file:

`quilt push -a`

- Remove all applied patches:

`quilt pop -a`
