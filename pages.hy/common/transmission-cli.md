# փոխանցում-cli

> Թեթև, հրամանի տող BitTorrent հաճախորդ:.
> Այս գործիքը հնացել է, տես `transmission-remote`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/transmission-cli>:.

- Ներբեռնեք կոնկրետ հեղեղ.:

`transmission-cli {{url|magnet|path/to/file}}`

- Ներբեռնեք հեղեղ հատուկ գրացուցակում.:

`transmission-cli {{[-w|--download-dir]}} {{path/to/download_directory}} {{url|magnet|path/to/file}}`

- Ստեղծեք torrent ֆայլ որոշակի ֆայլից կամ գրացուցակից.:

`transmission-cli --new {{path/to/source_file_or_directory}}`

- Նշեք ներբեռնման արագության սահմանաչափը (ԿԲ/վ-ով).:

`transmission-cli {{[-d|--downlimit]}} {{50}} {{url|magnet|path/to/file}}`

- Նշեք վերբեռնման արագության սահմանաչափը (ԿԲ/վ-ով).:

`transmission-cli {{[-u|--uplimit]}} {{50}} {{url|magnet|path/to/file}}`

- Միացումների համար օգտագործեք հատուկ նավահանգիստ.:

`transmission-cli {{[-p|--port]}} {{port_number}} {{url|magnet|path/to/file}}`

- Հարկադիր կոդավորումը հասակակից կապերի համար.:

`transmission-cli {{[-er|--encryption-required]}} {{url|magnet|path/to/file}}`

- Օգտագործեք Bluetack-ի ձևաչափով հասակակիցների արգելափակման ցուցակը.:

`transmission-cli {{[-b|--blocklist]}} {{blocklist_url|path/to/blocklist}} {{url|magnet|path/to/file}}`
