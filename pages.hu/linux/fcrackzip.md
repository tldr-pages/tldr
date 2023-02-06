# fcrackzip

> ZIP-archívum jelszó feltörő segédprogram. További információ: <https://manned.org/fcrackzip>.

- Erőszakos jelszófeltörés: a jelszó hossza 4-8 karakter, és csak alfanumerikus karaktereket tartalmaz (a sorrend számít):

`fcrackzip --brute-force --length 4-8 --charset aA1 {{archive}}`

- Brute-force egy 3 karakter hosszúságú, csak kisbetűs karaktereket tartalmazó jelszó szóbeli üzemmódban: `$` és `%`:

`fcrackzip -v --brute-force --length 3 --charset a:$% {{archive}}`

- Brute-force jelszó, amely csak kisbetűket és speciális karaktereket tartalmaz:

`fcrackzip --brute-force --length 4 --charset a! {{archive}}`

- Brute-force egy olyan jelszó, amely csak számjegyeket tartalmaz, kezdve a `12345` jelszóval:

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 {{archive}}`

- Jelszó feltörése szólista segítségével:

`fcrackzip --use-unzip --dictionary --init-password {{wordlist}} {{archive}}`

- A feltörési teljesítmény összehasonlítása:

`fcrackzip --benchmark`
