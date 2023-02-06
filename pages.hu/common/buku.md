# buku

> Parancssoros, böngészőfüggetlen könyvjelzőkezelő. További információ: <https://github.com/jarun/Buku>.

- Az összes olyan könyvjelző megjelenítése, amely megfelel a "kulcsszónak" és "privacy" címkével rendelkezik:

`buku {{keyword}} --stag {{privacy}}`

- Könyvjelző hozzáadása "keresőmotor" és "adatvédelem" címkékkel:

`buku --add {{https://example.com}} {{search engine}}, {{privacy}}`

- Könyvjelző törlése:

`buku --delete {{bookmark_id}}`

- Szerkesztő megnyitása könyvjelző szerkesztéséhez:

`buku --write {{bookmark_id}}`

- A "keresőmotor" címke eltávolítása a könyvjelzőből:

`buku --update {{bookmark_id}} --tag {{-}} {{search engine}}`
