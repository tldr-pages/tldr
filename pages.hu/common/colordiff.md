# colordiff

> Egy eszköz a diff kimenet színezésére. A colordiff Perl szkript a `diff` csomagolása, és ugyanazt a kimenetet produkálja, de szép szintaxis kiemeléssel. A színsémák testre szabhatók. További információ: <https://github.com/kimmel/colordiff>.

- Fájlok összehasonlítása:

`colordiff {{file1}} {{file2}}`

- Kimenet két oszlopban:

`colordiff -y {{file1}} {{file2}}`

- A fájlok tartalmának esetenkénti eltéréseinek figyelmen kívül hagyása:

`colordiff -i {{file1}} {{file2}}`

- Jelentést ad, ha két fájl megegyezik:

`colordiff -s {{file1}} {{file2}}`

- Fehér szóközök figyelmen kívül hagyása:

`colordiff -w {{file1}} {{file2}}`
