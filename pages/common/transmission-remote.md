# transmission-remote

> Remote control utility for `transmission-daemon` and `transmission`.
> More information: <https://manned.org/transmission-remote>.

- Add a torrent file or magnet link to Transmission and download to a specified directory:

`transmission-remote {{hostname}} {{[-a|--all]}} {{torrent|url}} {{[-w|--download-dir]}} /{{path/to/download_directory}}`

- Change the default download directory:

`transmission-remote {{hostname}} {{[-w|--download-dir]}} /{{path/to/download_directory}}`

- List all torrents:

`transmission-remote {{hostname}} {{[-l|--list]}}`

- Start torrent 1 and 2, stop torrent 3:

`transmission-remote {{hostname}} {{[-t|--torrent]}} "1,2" {{[-s|--start]}} {{[-t|--torrent]}} 3 {{[-S|--stop]}}`

- Remove torrent 1 and 2, and also delete local data for torrent 2:

`transmission-remote {{hostname}} {{[-t|--torrent]}} 1 {{[-r|--remove]}} {{[-t|--torrent]}} 2 {{[-rad|--remove-and-delete]}}`

- Stop all torrents:

`transmission-remote {{hostname}} {{[-t|--torrent]}} {{all}} {{[-S|--stop]}}`

- Move torrents 1-10 and 15-20 to a new directory (which will be created if it does not exist):

`transmission-remote {{hostname}} {{[-t|--torrent]}} "1-10,15-20" --move /{{path/to/new_directory}}`
