# transmission-cli

> A lightweight, command-line BitTorrent client.
> This tool has been deprecated, please see `transmission-remote`.
> More information: <https://manned.org/transmission-cli>.

- Download a specific torrent:

`transmission-cli {{url|magnet|path/to/file}}`

- Download a torrent to a specific directory:

`transmission-cli {{[-w|--download-dir]}} {{path/to/download_directory}} {{url|magnet|path/to/file}}`

- Create a torrent file from a specific file or directory:

`transmission-cli --new {{path/to/source_file_or_directory}}`

- Specify the download speed limit (in KB/s):

`transmission-cli {{[-d|--downlimit]}} {{50}} {{url|magnet|path/to/file}}`

- Specify the upload speed limit (in KB/s):

`transmission-cli {{[-u|--uplimit]}} {{50}} {{url|magnet|path/to/file}}`

- Use a specific port for connections:

`transmission-cli {{[-p|--port]}} {{port_number}} {{url|magnet|path/to/file}}`

- Force encryption for peer connections:

`transmission-cli {{[-er|--encryption-required]}} {{url|magnet|path/to/file}}`

- Use a Bluetack-formatted peer blocklist:

`transmission-cli {{[-b|--blocklist]}} {{blocklist_url|path/to/blocklist}} {{url|magnet|path/to/file}}`
