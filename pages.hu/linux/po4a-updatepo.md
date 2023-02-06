# po4a-updatepo

> Egy dokumentáció fordításának frissítése (PO formátumban). További információ: <https://po4a.org/man/man1/po4a-updatepo.1.php>.

- Egy PO-fájl frissítése a származási fájl módosításának megfelelően:

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- A rendelkezésre álló formátumok listájának lekérdezése:

`po4a-updatepo --help-format`

- Több PO-fájl frissítése a származási fájl módosításának megfelelően:

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/po1.po}} --po {{path/to/po2.po}}`
