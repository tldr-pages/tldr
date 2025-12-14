# ident

> Identify RCS keyword strings in files.
> See also: `ci`, `co`, `rcs`, `rcsdiff`, `rlog`.
> More information: <https://manned.org/ident>.

- Display RCS identification strings in a file:

`ident {{path/to/file}}`

- Display RCS identification strings with their filename:

`ident -q {{path/to/file1 path/to/file2 ...}}`

- Display RCS identification strings from `stdin`:

`cat {{path/to/file}} | ident`
