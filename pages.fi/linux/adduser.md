# adduser

> Käyttäjän lisäysapuohjelma.
> Lisätietoja: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Luo uusi käyttäjä oletuskotihakemistolla ja pyydä käyttäjää asettamaan salasana:

`adduser {{username}}`

- Luo uusi käyttäjä ilman kotihakemistoa:

`adduser --no-create-home {{username}}`

- Luo uusi käyttäjä kotihakemistolla määritetyssä polussa:

`adduser --home {{path/to/home}} {{username}}`

- Luo uusi käyttäjä, jolla on määritetty kuori kirjautumiskuoreksi:

`adduser --shell {{path/to/shell}} {{username}}`

- Luo uusi käyttäjä, joka kuuluu määritettyyn ryhmään:

`adduser --ingroup {{group}} {{username}}`
