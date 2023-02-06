# dc

> Tetszőleges pontosságú számológép. Fordított poláris jelölést (RPN) használ. Lásd még: `bc`. További információ: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>.

- Interaktív munkamenet indítása:

`dc`

- Szkript végrehajtása:

`dc {{path/to/script.dc}}`

- Kifejezés kiszámítása a megadott skálával:

`dc --expression='{{10}} k {{5 3 /}} p'`

- Számítson ki 4-szer 5-öt (4 5 \*), vonjon ki 17-et (17 -), és \[p\]rint a kimenet:

`dc --expression='4 5 * 17 - p'`

- Állítsa a tizedesjegyek számát 7-re (7 k), számítsa ki az 5-öt osztva -3-mal (5 \_3 /) és \[p\]rint:

`dc --expression='7 k 5 _3 / p'`

- Az aranymetszés, phi kiszámítása: állítsa a tizedesjegyek számát 100-ra (100 k), az 5 négyzetgyökét (5 v) plusz 1 (1 +), osztva 2-vel (2 /), és \[p\]rint eredmény:

`dc --expression='100 k 5 v 1 + 2 / p'`
