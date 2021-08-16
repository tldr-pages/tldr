# xml escape

> Escape special XML characters.
> More information: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Escape special XML characters in a string:

`xml escape "{{<a1>}}"`

- Escape special XML characters from the standard input:

`echo  "{{<a1>}}" | xml escape`

- Display help for the `escape` subcommand:

`xml escape --help`
