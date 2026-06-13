# rcsmerge

> Merge RCS revisions into the working file.
> See also: `ci`, `co`, `rcs`, `rcsdiff`, `rlog`.
> More information: <https://manned.org/rcsmerge>.

- Merge differences between two revisions into the working file:

`rcsmerge -r{{revision1}} -r{{revision2}} {{path/to/file}}`

- Merge changes from a branch revision into the working file:

`rcsmerge -r{{branch_revision}} {{path/to/file}}`

- Perform a quiet merge (suppress diagnostics):

`rcsmerge -q -r{{revision1}} -r{{revision2}} {{path/to/file}}`

- Print the result to `stdout` instead of overwriting the working file:

`rcsmerge -p -r{{revision1}} -r{{revision2}} {{path/to/file}}`
