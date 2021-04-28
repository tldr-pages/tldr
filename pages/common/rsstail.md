# rsstail

> `tail` for RSS feeds.
> More information: <https://github.com/gvalkov/rsstail.py>.

- Show the feed of a given URL and wait for new entries appearing at the bottom:

`rsstail -u {{url}}`

- Show the feed in reverse chronological order (newer at the bottom):

`rsstail -r -u {{url}}`

- Include publication date and link:

`rsstail -pl -u {{url}}`

- Set update interval:

`rsstail -u {{url}} -i {{interval_in_seconds}}`

- Show feed and exit:

`rsstail -1 -u {{url}}`
