# notmuch

> A command-line based program for indexing, searching, reading, and tagging large collections of email messages.
> More Information: <https://notmuchmail.org/manpages/>.

- Configure for first use:

`notmuch setup`

- Add tags for all messages matching the search term:

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- Remove tags for all messages matching the search term:

`notmuch tag -{{custom-tag}} {{"search-term"}}`

- Count messages matching the given search term:

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- Search for messages matching the given search term:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} {{"search-term"}}`

- Limit the number of saerch results to X:

`notmuch search --format={{json|text}} --output={summary|threads|messages|files|tags} --limit={{X}} {{"search-term"}}`

- Create a reply template for a set of messages:

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} {{"search-term"}}`
