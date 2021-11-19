# ytfzf

> A POSIX script that helps you find and download videos and music.
> More information: <https://github.com/pystardust/ytfzf>.

- Search videos in YouTube and display the thumbnails:

`ytfzf --show-thumbnails {{search_pattern}}`

- Play only audio of first item in loop:

`ytfzf --audio-only --auto-select --loop {{search_pattern}}`

- Download a video from history:

`ytfzf --download --choose-from-history`

- Play all the music found in one search:

`ytfzf --audio-only --select-all {{search_pattern}}`

- See the trending videos in external menu:

`ytfzf --trending --ext-menu {{search_pattern}}`

- Search PeerTube instead of YouTube:

`ytfzf --peertube {{search_pattern}}`
