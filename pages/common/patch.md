#patch

> Patch a file (or files) with a diff file.
> Note that diff files contain both the target filenames and list of changes.

- apply a patch

`patch < {{patchfile}}.diff`

- apply a patch to current directory

`patch -p1 < {{patchfile}}.diff`

- apply the reverse of a patch

`patch -R < {{patchfile}}.diff`
