# you-get

> Download media contents (videos, audios, images) from the Web.
> See also: `yt-dlp`, `youtube-viewer`, `instaloader`.
> More information: <https://you-get.org/#getting-started>.

- Print media information about a specific media on the web:

`you-get {{[-i|--info]}} {{https://example.com/video?id=value}}`

- Download a media from a specific URL:

`you-get {{https://example.com/video?id=value}}`

- Search on Google Videos and download:

`you-get {{keywords}}`

- Download a media to a specific location:

`you-get {{[-o|--output-dir]}} {{path/to/directory}} {{[-O|--output-filename]}} {{filename}} {{https://example.com/watch?v=value}}`

- Download a media using a proxy:

`you-get {{[-x|--http-proxy]}} {{proxy_server}} {{https://example.com/watch?v=value}}`
