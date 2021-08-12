# debchange

> Instrument pentru întreținerea fișierului debian/changelog într-un pachet sursă Debian.
> Mai multe informaţii: <https://manpages.debian.org/debchange>

- Adăugați o nouă versiune pentru o încărcare non-mentenant la changelog:

`debchange --nmu`

- Adăugați o intrare changelog la versiunea curentă:

`debchange --append`

- Adăugați o intrare changelog pentru a închide bug-ul cu ID-ul specificat:

`debchange --closes {{bug_id}}`
