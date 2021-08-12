# calibredb

> Instrument pentru a manipula baza de date a cărții electronice.
> O parte a bibliotecii de cărți electronice Calibre.
> Mai multe informaţii: <https://manual.calibre-ebook.com/generated/en/calibredb.html>

- Lista cărților electronice în bibliotecă cu informații suplimentare:

`calibredb list`

- Căutați cărți electronice care afișează informații suplimentare:

`calibredb list --search {{search_term}}`

- Caută doar ID-uri de e-carti:

`calibredb search {{search_term}}`

- Adăugați una sau mai multe cărți electronice în bibliotecă:

`calibredb add {{file1 file2 …}}`

- Adaugă recursiv toate cărțile electronice sub un director la bibliotecă:

`calibredb add -r {{path/to/directory}}`

- Eliminați una sau mai multe cărți electronice din bibliotecă. Aveți nevoie de ID-uri de carte electronică (vezi mai sus):

`calibredb remove {{id1 id2 …}}`
