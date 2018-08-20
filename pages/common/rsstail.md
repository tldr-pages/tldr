# rsstail

> Basically tail for RSS feeds.

- Show feed of given url and wait for new entries:

`rsstail -u {{url}}`

- Show feed with latest item at the bottom:

`rsstail -r -u {{url}}`

- Show feed including publication date and link:

`rsstail -pl -u {{url}}`

- Show feed and set update interval:

`rsstail -u {{url}} -i {{interval_in_seconds}}`

- Show feed and exit:

`rsstail -1 -u {{url}}`
