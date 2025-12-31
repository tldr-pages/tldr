# xml escape

> Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`.
> More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960>.

- Escape special XML characters in a string:

`xml {{[esc|escape]}} "{{<a1>}}"`

- Escape special XML characters from `stdin`:

`echo "{{<a1>}}" | xml {{[esc|escape]}}`

- Display help:

`xml {{[esc|escape]}} --help`
