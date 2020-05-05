# quilt

> Tool to manage series of patches.
> More information: <https://savannah.nongnu.org/projects/quilt>.

- Import an existing patch from a file:

`quilt import {{path/to/filename.patch}}`

- Create a new patch:

`quilt new {{filename.patch}}`

- Add a file to the current patch:

`quilt add {{path/to/file}}`

- After you have edited the file, refresh the current patch with your changes:

`quilt refresh`

- Apply all patches in the series file:

`quilt push -a`

- Remove all applied patches:

`quilt pop -a`
