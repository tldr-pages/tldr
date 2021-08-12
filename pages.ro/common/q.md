# q

> Executați interogări ca SQL pe fișierele.csv și .tsv.
> Mai multe informaţii: <https://harelba.github.io/q>

- Interogare fișier `.csv` specificând delimitatorul ca „,”:

`q -d',' "SELECT * from {{path/to/file}}"`

- Fișier de interogare `.tsv`:

`q -t "SELECT * from {{path/to/file}}"`

- Fișier de interogare cu rând antet:

`q -d{{delimiter}} -H "SELECT * from {{path/to/file}}"`

- Citiți datele din stdin; '-' în interogare reprezintă datele din stdin:

`{{output}} | q "select * from -"`

- Alăturați două fișiere (aliate ca `f1` și `f2` în exemplu) în coloana `c1`, o coloană comună:

`q "SELECT * FROM {{path/to/file}} f1 JOIN {{path/to/other_file}} f2 ON (f1.c1 = f2.c1)"`

- Formatarea ieșirii utilizând un delimitator de ieșire cu o linie de antet de ieșire (notă: comanda va afișa numele coloanelor pe baza antetului fișierului de intrare sau a aliasurilor de coloană suprascrise în interogare):

`q -D{{delimiter}} -O "SELECT {{column}} as {{alias}} from {{path/to/file}}"`
