# xml unescape

> Unescape special XML characters.
> More information: <http://xmlstar.sourceforge.net/docs.php>.

- Unescape special XML characters from a string:

`xml unescape "{{&lt;a1&gt;}}"`

- Unescape special XML characters from the standard input:

`echo  "{{&lt;a1&gt;}}" | xml unescape`

- Display help for the `unescape` subcommand:

`xml escape --help`
