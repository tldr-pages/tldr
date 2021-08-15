# xml-edit

> XMLStarlet toolkit: Un-escape special XML characters.
> More information: <https://http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Unescape special XML characters from a string:

`xml unescape {{"&lt;a1&gt;"}}`

- Unescape special XML characters from standard input:

`echo  {{"&lt;a1&gt;"}} | xml unescape`

- Display help for `unescape` subcommand:

`xml escape --help`
