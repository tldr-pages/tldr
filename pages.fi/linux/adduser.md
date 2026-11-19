# adduser

> Käyttäjän lisäysapuohjelma.
> Lisätietoa: <https://manned.org/adduser>.

- Luo uusi käyttäjä oletuskotihakemistolla ja pyydä käyttäjää asettamaan salasana:

`adduser {{käyttäjätunnus}}`

- Luo uusi käyttäjä ilman kotihakemistoa:

`adduser --no-create-home {{käyttäjätunnus}}`

- Luo uusi käyttäjä kotihakemistolla määritetyssä polussa:

`adduser --home {{polku/kotiin}} {{käyttäjätunnus}}`

- Luo uusi käyttäjä, jolla on määritetty kuori kirjautumiskuoreksi:

`adduser --shell {{polku/kuoriin}} {{käyttäjätunnus}}`

- Luo uusi käyttäjä, joka kuuluu määritettyyn ryhmään:

`adduser --ingroup {{ryhmä}} {{käyttäjätunnus}}`
