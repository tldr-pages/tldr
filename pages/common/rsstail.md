# rsstail

> 'tail' for RSS feeds.

- Show feed of given url and wait for new entries:

`rsstail -u {{url}}`

- Reverse feed:

`rsstail -r -u {{url}}`

- Include publication date and link:

`rsstail -pl -u {{url}}`

- Set update interval:

`rsstail -u {{url}} -i {{interval_in_seconds}}`

- Show feed and exit:

`rsstail -1 -u {{url}}`
