# hashid

> Python3 program, amely azonosítja az adatok és jelszavak hash-ját. További információ: <https://github.com/psypanda/hashID>.

- Hash-ok azonosítása a standard bemenetről (begépeléssel, másolással és beillesztéssel vagy a hash programba való bepipálásával):

`hashid`

- Az argumentumként átadott hash-ok azonosítása (több hash is átadható):

`hashid {{hash}}`

- Hashek azonosítása fájlban (soronként egy hash):

`hashid {{path/to/hashes.txt}}`

- Az összes lehetséges hash-típus megjelenítése (beleértve a sózott hash-okat is):

`hashid --extended {{hash}}`

- A `hashcat`'s mode number és a `john`'s formátum string a hash típusok:

`hashid --mode --john {{hash}}`

- A kimenet mentése fájlba a standard kimenetre történő nyomtatás helyett:

`hashid --outfile {{path/to/output.txt}} {{hash}}`
