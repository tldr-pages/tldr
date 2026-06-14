# peerflix

> Հեռարձակեք վիդեո կամ աուդիո վրա հիմնված հեղեղներ մեդիա նվագարկիչում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mafintosh/peerflix>:.

- Հեռարձակեք ամենամեծ մեդիա ֆայլը հեղեղով.:

`peerflix "{{torrent_url|magnet_link}}"`

- Թվարկեք հեղեղի մեջ պարունակվող բոլոր հոսքային ֆայլերը (տրված որպես մագնիսական հղում).:

`peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" {{[-l|--list]}}`

- Հեռարձակեք ամենամեծ ֆայլը torrent-ում, որը տրված է որպես torrent URL, VLC-ին.:

`peerflix "{{http://example.net/music.torrent}}" {{[-v|--vlc]}}`

- Հեռարձակեք ամենամեծ ֆայլը torrent-ով MPlayer-ին, ենթագրերով.:

`peerflix "{{torrent_url|magnet_link}}" {{[-m|--mplayer]}} {{[-t|--subtitles]}} {{subtitle-file.srt}}`

- Հեռարձակեք բոլոր ֆայլերը հեղեղից դեպի Airplay.:

`peerflix "{{torrent_url|magnet_link}}" {{[-a|--all]}} {{[-s|--airplay]}}`
