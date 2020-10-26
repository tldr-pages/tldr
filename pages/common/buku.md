# buku

> Command-line browser-independent bookmark manager.
> More information: <https://github.com/jarun/Buku>.

- Display all bookmarks matching "keyword" and with "privacy" tag:

`buku {{keyword}} --stag {{privacy}}`

- Add bookmark with tags "search engine" and "privacy":

`buku --add {{https://example.com}} {{search engine}}, {{privacy}}`

- Delete a bookmark:

`buku --delete {{bookmark_id}}`

- Open editor to edit a bookmark:

`buku --write {{bookmark_id}}`

- Remove "search engine" tag from a bookmark:

`buku --update {{bookmark_id}} --tag {{-}} {{search engine}}`
