# xml unescape

> A speciális XML-karakterek kikerülése, pl. `&lt;a1&gt;` → `<a1>`. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- Speciális XML karakterek eltávolítása egy karakterláncból:

`xml unescape "{{&lt;a1&gt;}}"`

- Unescape speciális XML-karakterek a `stdin`:

`echo "{{&lt;a1&gt;}}" | xml unescape`

- A `unescape` alparancs súgójának megjelenítése:

`xml escape --help`
