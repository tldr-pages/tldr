# buku

> Manager de marcaje independent de browser de linie de comandă.
> Mai multe informaţii: <https://github.com/jarun/Buku>

- Afișează toate marcajele care se potrivesc cu „cuvânt cheie” și cu eticheta „confidențialitate”:

`buku {{keyword}} --stag {{privacy}}`

- Adăugați marcaj cu etichete „motor de căutare” și „confidențialitate”:

`buku --add {{https://example.com}} {{search engine}}, {{privacy}}`

- Ștergeți un semn de carte:

`buku --delete {{bookmark_id}}`

- Deschideți editorul pentru a edita un marcaj:

`buku --write {{bookmark_id}}`

- Eliminați eticheta „motor de căutare” dintr-un marcaj:

`buku --update {{bookmark_id}} --tag {{-}} {{search engine}}`
