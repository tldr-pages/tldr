# plocate

> Find filenames quickly.
> Make sure to run `sudo updatedb` to include new files.
> More information: <https://plocate.sesse.net>.

- Look for patterns in the database (recomputed periodically):

`plocate {{pattern}}`

- Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):

`plocate */{{filename}}`
