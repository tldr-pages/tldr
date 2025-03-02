# locate

> Find filenames quickly.
> Note: the database is recomputed periodically (usually weekly or daily).
> More information: <https://manned.org/locate>.

- Search for a file matching a pattern in its pathname:

`locate {{pattern}}`

- Perform a case-[i]nsensitive search in file [b]asenames only:

`locate -i -b {{pattern}}`

- [c]ount the number of files that matching a pattern:

`locate -c {{pattern}}`

- Search for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):

`locate '*/{{filename}}'`

- Search using a [r]egular expression and [l]imit the number of output lines:

`locate -r -l {{LIMIT}} '{{regex_pattern}}'`

- Update the database (required to find recently added files):

`sudo updatedb`
