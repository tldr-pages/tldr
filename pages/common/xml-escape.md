# xml escape

> Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`.
> More information: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Escape special XML characters in a string:

`xml escape "{{<a1>}}"`

- Escape special XML characters from stdin:

`echo  "{{<a1>}}" | xml escape`

- Display help for the `escape` subcommand:

`xml escape --help`
