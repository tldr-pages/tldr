# փոխանցում-ստեղծել

> Ստեղծեք BitTorrent `.torrent` ֆայլեր:.
> Տես նաև՝ `transmission`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/transmission-create>:.

- Ստեղծեք հեղեղ որոշակի կտորի չափով (KB-ով).:

`transmission-create {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_announce_url}} {{[-s|--piecesize]}} {{2048}} {{path/to/file_or_directory}}`

- Ստեղծեք մասնավոր հեղեղ որոշակի կտորի չափով (KB-ով).:

`transmission-create {{[-p|--private]}} {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_announce_url}} {{[-s|--piecesize]}} {{2048}} {{path/to/file_or_directory}}`

- Ստեղծեք հեղեղ մեկնաբանությունով.:

`transmission-create {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_url1}} {{[-c|--comment]}} {{comment}} {{path/to/file_or_directory}}`

- Ստեղծեք հեղեղ մի քանի հետքերով.:

`transmission-create {{[-o|--outfile]}} {{path/to/example.torrent}} {{[-t|--tracker]}} {{tracker_url1}} {{[-t|--tracker]}} {{tracker_url2}} {{path/to/file_or_directory}}`

- Ցուցադրել օգնությունը.:

`transmission-create {{[-h|--help]}}`
