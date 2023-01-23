# xml escape

> Speciális XML karakterek elrejtése, pl. `<a1>` → `&lt;a1&gt;`. További információ: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Speciális XML karakterek kikerülése egy karakterláncban:

`xml escape "{{<a1>}}"`

- Speciális XML-karakterek kikerülése a `stdin`:

`echo "{{<a1>}}" | xml escape`

- A `escape` alparancs súgójának megjelenítése:

`xml escape --help`
