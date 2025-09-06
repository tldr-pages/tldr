# mktorrent

> Create BitTorrent metainfo files.
> More information: <https://github.com/Rudde/mktorrent>.

- Create a torrent with 2^21 KB as the piece size:

`mktorrent {{[-a|--announce]}} {{tracker_announce_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Create a private torrent with a 2^21 KB piece size:

`mktorrent {{[-p|--private]}} {{[-a|--announce]}} {{tracker_announce_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Create a torrent with a comment:

`mktorrent {{[-c|--comment]}} "{{comment}}" {{[-a|--announce]}} {{tracker_announce_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Create a torrent with multiple trackers:

`mktorrent {{[-a|--announce]}} {{tracker_announce_url,tracker_announce_url_2}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Create a torrent with web seed URLs:

`mktorrent {{[-a|--announce]}} {{tracker_announce_url}} -w {{web_seed_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`
