#patch

> Patch a file or files with a diff file.

- apply a patch

`patch < {{patchfile}}.diff`

- apply a patch to current directory

`patch -p1 < {{patchfile}}.diff`

- reverse a patch

`patch -R < {{patchfile}}.diff`
