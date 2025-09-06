# deemix

> A barebone deezer downloader library built from the ashes of Deezloader Remix.
> It can be used as a standalone CLI app or implemented in a UI using the API.
> More information: <https://gitlab.com/RemixDev/deemix-py>.

- Download a track or playlist:

`deemix {{https://www.deezer.com/us/track/00000000}}`

- Download track/playlist at a specific bitrate:

`deemix --bitrate {{FLAC|MP3}} {{url}}`

- Download to a specific path:

`deemix --bitrate {{bitrate}} --path {{path}} {{url}}`

- Create a portable deemix configuration file in the current directory:

`deemix --portable --bitrate {{bitrate}} --path {{path}} {{url}}`
