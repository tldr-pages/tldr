# adduser

> Käyttäjän lisäysapuohjelma.
> Lisätietoja: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Luo uusi käyttäjä oletuskotihakemistolla ja pyydä käyttäjää asettamaan salasana:

`adduser {{tunnus}}`

- Luo uusi käyttäjä ilman kotihakemistoa:

`adduser --no-create-home {{tunnus}}`

- Luo uusi käyttäjä kotihakemistolla määritetyssä polussa:

`adduser --home {{polku/kotiin}} {{tunnus}}`

- Luo uusi käyttäjä, jolla on määritetty kuori kirjautumiskuoreksi:

`adduser --shell {{polku/kuoriin}} {{tunnus}}`

- Luo uusi käyttäjä, joka kuuluu määritettyyn ryhmään:

`adduser --ingroup {{ryhmä}} {{tunnus}}`
