# newsboat

> An RSS/Atom feed reader for text terminals.
> More information: <https://newsboat.org/>.

- First import feed URLs from an OPML file:

`newsboat {{[-i|--import-from-opml]}} {{my-feeds.xml}}`

- Alternatively, add feeds manually:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- Start Newsboat and refresh all feeds on startup:

`newsboat {{[-r|--refresh-on-start]}}`

- Execute one or more commands in non-interactive mode:

`newsboat {{[-x|--execute]}} {{reload print-unread ...}}`

- See keyboard shortcuts (the most relevant are visible in the status line):

`<?>`
