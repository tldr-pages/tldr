# transmission-show

> Get info about a torrent file.
> See also: `transmission`.
> More information: <https://manned.org/transmission-show>.

- Display metadata for a specific a torrent:

`transmission-show {{path/to/file.torrent}}`

- Generate a magnet link for a torrent:

`transmission-show --magnet {{path/to/file.torrent}}`

- Query a torrent's trackers to get the current number of peers:

`transmission-show --scrape {{path/to/file.torrent}}`
