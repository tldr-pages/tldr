# locate

> Find filenames quickly.
> More information: <https://keith.github.io/xcode-man-pages/locate.1.html>.

- Look for pattern in the database. Note: the database is recomputed periodically (usually weekly or daily):

`locate "{{pattern}}"`

- Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):

`locate */{{filename}}`

- Recompute the database. You need to do it if you want to find recently added files:

`sudo /usr/libexec/locate.updatedb`
