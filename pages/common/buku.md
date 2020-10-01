# buku

> Browser-independent bookmark manager for CLI.
> More information: <https://github.com/jarun/Buku>.

- List all bookmarks matching "keyword" and with "privacy" tag:

`buku {{keyword}} -t {{privacy}}`

- Add bookmark with tags "search engine" and "privacy":

`buku -a {{https://ddg.gg}} {{search engine}}, {{privacy}}`

- Delete a bookmark:

`buku -d {{bookmark_id}}`

- Open editor to edit a bookmark:

`buku -w {{bookmark_id}}`

- Remove "search engine" tag from a bookmark:

`buku -u {{bookmark_id}} --tag {{-}} {{search engine}}`
