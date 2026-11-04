# you-get

> Download media (video's, audio, afbeeldingen) van het web.
> Zie ook: `yt-dlp`, `youtube-viewer`, `instaloader`.
> Meer informatie: <https://you-get.org/#getting-started>.

- Toon informatie over specifieke media op het web:

`you-get {{[-i|--info]}} {{https://example.com/video?id=value}}`

- Download media van een specifieke URL:

`you-get {{https://example.com/video?id=value}}`

- Zoek op Google Video's en download:

`you-get {{trefwoorden}}`

- Download media naar een specifieke locatie:

`you-get {{[-o|--output-dir]}} {{pad/naar/map}} {{[-O|--output-filename]}} {{bestandsnaam}} {{https://example.com/watch?v=value}}`

- Download media via een proxy:

`you-get {{[-x|--http-proxy]}} {{proxy_server}} {{https://example.com/watch?v=value}}`
