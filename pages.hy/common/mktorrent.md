#mktorrent

> Ստեղծեք BitTorrent մետատեղեկատվական ֆայլեր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mktorrent>:.

- Ստեղծեք torrent 2^21 KB-ով որպես կտորի չափ.:

`mktorrent {{[-a|--announce]}} {{tracker_announce_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Ստեղծեք անձնական հեղեղ 2 ^ 21 ԿԲ կտորի չափով.:

`mktorrent {{[-p|--private]}} {{[-a|--announce]}} {{tracker_announce_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Ստեղծեք հեղեղ մեկնաբանությունով.:

`mktorrent {{[-c|--comment]}} "{{comment}}" {{[-a|--announce]}} {{tracker_announce_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Ստեղծեք հեղեղ մի քանի հետքերով.:

`mktorrent {{[-a|--announce]}} {{tracker_announce_url,tracker_announce_url_2}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`

- Ստեղծեք հեղեղ վեբ սերմերի URL-ներով.:

`mktorrent {{[-a|--announce]}} {{tracker_announce_url}} -w {{web_seed_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{path/to/example.torrent}} {{path/to/file_or_directory}}`
