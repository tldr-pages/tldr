# ytfzf

> Find and download videos and music. Written in POSIX shell.
> See also: `youtube-dl`, `yt-dlp`, `instaloader`.
> More information: <https://manned.org/ytfzf>.

- Search for videos on YouTube with thumbnail previews:

`ytfzf {{[-t|--show-thumbnails]}} {{search_pattern}}`

- Play only the audio of the first item in a loop:

`ytfzf {{[-m|--audio-only]}} {{[-a|--auto-select]}} {{[-l|--loop]}} {{search_pattern}}`

- Download a video from the history:

`ytfzf {{[-d|--download]}} --choose-from-history`

- Play all the music found in a search:

`ytfzf {{[-m|--audio-only]}} {{[-A|--select-all]}} {{search_pattern}}`

- See the trending videos in an external menu:

`ytfzf --trending --ext-menu {{search_pattern}}`

- Search on PeerTube instead of YouTube:

`ytfzf --peertube {{search_pattern}}`
