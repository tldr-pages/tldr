# notmuch

> A command-line based program for indexing, searching, reading, and tagging large collections of email messages.

- Configure for first use:

`notmuch setup`

- Add tags for all messages matching the search term:

`notmuch tag +{{tag}} {{"search-term"}}`

- Remove tags for all messages matching the search term:

`notmuch tag -{{tag}} {{"search-term"}}`

- Count messages matching the given search term:

`notmuch count --output={{messages|threads}} {{"search-term"}}`

- Search for messages matching the given search terms:

`notmuch search --format={{json|text}} --output={summary|threads|messages|files|tags} {{"search-term"}}`
