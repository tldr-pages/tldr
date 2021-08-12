# newsboat

> Un cititor de flux RSS/Atom pentru terminale de text.
> Mai multe informaţii: <https://newsboat.org/>

- Primul import URL-uri de flux dintr-un fișier OPML:

`newsboat -i {{my-feeds.xml}}`

- Alternativ, adăugați feed-uri manual:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- Porniți newsboat și reîmprospătați toate fluxurile la pornire:

`newsboat -r`

- Vedeți comenzile rapide de la tastatură (cele mai relevante sunt vizibile în linia de stare):

`?`
