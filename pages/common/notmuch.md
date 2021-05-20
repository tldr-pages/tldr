# notmuch

> Command-line based program for indexing, searching, reading, and tagging large collections of email messages.
> More information: <https://notmuchmail.org/manpages/>.

- Configure for first use:

`notmuch setup`

- Add a tag for all messages matching a search term:

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- Remove a tag for all messages matching a search term:

`notmuch tag -{{custom_tag}} "{{search_term}}"`

- Count messages matching the given search term:

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- Search for messages matching the given search term:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{search_term}}"`

- Limit the number of search results to X:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{search_term}}"`

- Create a reply template for a set of messages:

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{search_term}}"`
