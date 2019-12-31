# deluge-console

> An interactive interface for the Deluge BitTorrent client.
> More information: <https://deluge-torrent.org>.

- Start the interactive console interface:

`deluge-console`

- Connect to a Deluge daemon instance:

`connect {{hostname}}:{{port}}`

- Add a torrent to the daemon:

`add {{url|magnet|path/to/file}}`

- Display information about all torrents:

`info`

- Display information about a specific torrent:

`info {{torrent_id}}`

- Pause a torrent:

`pause {{torrent_id}}`

- Resume a torrent:

`resume {{torrent_id}}`

- Remove a torrent from the daemon:

`rm {{torrent_id}}`
