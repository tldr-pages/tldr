# deluge-console

> An interactive interface for the Deluge BitTorrent client.
> More information: <https://deluge-torrent.org/userguide/thinclient/>.

- Start the interactive console interface:

`deluge-console`

- [Interactive] Connect to a Deluge daemon instance:

`connect {{hostname}}:{{port}}`

- [Interactive] Add a torrent to the daemon:

`add {{url|magnet|path/to/file}}`

- [Interactive] Display information about all torrents:

`info`

- [Interactive] Display information about a specific torrent:

`info {{torrent_id}}`

- [Interactive] Pause a torrent:

`pause {{torrent_id}}`

- [Interactive] Resume a torrent:

`resume {{torrent_id}}`

- [Interactive] Remove a torrent from the daemon:

`rm {{torrent_id}}`
