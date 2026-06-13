# co

> Check out RCS revisions (retrieve working files from the Revision Control System).
> See also: `ci`, `rcs`, `rcsdiff`, `rlog`.
> More information: <https://manned.org/co>.

- Check out the latest revision of a file (retrieves a read-only copy):

`co {{path/to/file}}`

- Check out a file with a lock for editing:

`co -l {{path/to/file}}`

- Check out a specific revision of a file:

`co -r{{revision}} {{path/to/file}}`

- Check out a file and overwrite it if it already exists:

`co -f -l {{path/to/file}}`

- Print a specific revision to `stdout` without creating a file:

`co -p -r{{revision}} {{path/to/file}}`
