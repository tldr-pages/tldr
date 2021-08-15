# xml-edit

> XMLStarlet toolkit: Un-escape special XML characters.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Unescape special XML characters from a string:

`xml unescape {{"&lt;a1&gt;"}}`

- Unescape special XML characters from standard input:

`echo  {{"&lt;a1&gt;"}} | xml unescape`

- Display help for `unescape` subcommand:

`xml escape --help`
