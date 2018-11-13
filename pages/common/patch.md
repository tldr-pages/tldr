# patch

> Patch a file (or files) with a diff file.
> Note that diff files contain both the target filenames and list of changes.

- Apply a patch:

`patch < {{patch_file}}.diff`

- Apply a patch to current directory:

`patch -p1 < {{patch_file}}.diff`

- Apply the reverse of a patch:

`patch -R < {{patch_file}}.diff`
