# ytfzf

> Zoek en download video's en muziek. Geschreven in POSIX shell.
> Zie ook: `youtube-dl`, `yt-dlp`, `instaloader`.
> Meer informatie: <https://manned.org/ytfzf>.

- Zoek naar video's op YouTube met thumbnailvoorbeelden:

`ytfzf {{[-t|--show-thumbnails]}} {{zoekpatroon}}`

- Speel alleen de audio van het eerste item in een lus af:

`ytfzf {{[-m|--audio-only]}} {{[-a|--auto-select]}} {{[-l|--loop]}} {{zoekpatroon}}`

- Download een video uit de geschiedenis:

`ytfzf {{[-d|--download]}} --choose-from-history`

- Speel alle muziek af die gevonden is in een zoekopdracht:

`ytfzf {{[-m|--audio-only]}} {{[-A|--select-all]}} {{zoekpatroon}}`

- Bekijk de trending video's in een extern menu:

`ytfzf --trending --ext-menu {{zoekpatroon}}`

- Zoek op PeerTube in plaats van YouTube:

`ytfzf --peertube {{zoekpatroon}}`
