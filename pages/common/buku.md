# buku

> Browser-independent bookmark manager.
> More information: <https://github.com/jarun/Buku#usage>.

- Display all bookmarks matching "keyword" and with "privacy" tag:

`buku {{keyword}} {{[-t|--stag]}} {{privacy}}`

- Add bookmark with tags "search engine" and "privacy":

`buku {{[-a|--add]}} {{https://example.com}} {{search engine}}, {{privacy}}`

- Delete a bookmark:

`buku {{[-d|--delete]}} {{bookmark_id}}`

- Open editor to edit a bookmark:

`buku {{[-w|--write]}} {{bookmark_id}}`

- Remove "search engine" tag from a bookmark:

`buku {{[-u|--update]}} {{bookmark_id}} --tag - {{search engine}}`
