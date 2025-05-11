# xml unescape

> Unescape special XML characters, e.g. `&lt;a1&gt;` → `<a1>`.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960>.

- Unescape special XML characters from a string:

`xml {{[unesc|unescape]}} "{{&lt;a1&gt;}}"`

- Unescape special XML characters from `stdin`:

`echo "{{&lt;a1&gt;}}" | xml {{[unesc|unescape]}}`

- Display help:

`xml {{[esc|escape]}} --help`
