# you-get

> Download media contents (videos, audios, images) from the Web.
> More information: <https://you-get.org>.

- Print media information about a specific media on the web:

`you-get --info {{https://example.com/video?id=value}}`

- Download a media from a specific URL:

`you-get {{https://example.com/video?id=value}}`

- Search on Google Videos and download:

`you-get {{keywords}}`

- Download a media to a specific location:

`you-get --output-dir {{path/to/directory}} --output-filename {{filename}} {{https://example.com/watch?v=value}}`

- Download a media using a proxy:

`you-get --http-proxy {{proxy_server}} {{https://example.com/watch?v=value}}`
