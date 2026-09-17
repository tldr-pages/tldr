# hlsq

> Display HLS manifests with color and basic filtering.
> More information: <https://github.com/soldiermoth/hlsq/>.

- View an HLS manifest from a URL:

`{{curl --silent url}} | hlsq`

- View an HLS manifest from a file:

`{{cat path/to/file.m3u8}} | hlsq`

- Continuously refetch a URL and update the output:

`hlsq -watch -url {{url}}`

- Filter a multivariant playlist by an attribute's string value:

`{{cat path/to/file.m3u8}} | hlsq -query '{{type = SUBTITLES}}'`

- Filter a multivariant playlist by an attribute's numeric value:

`{{cat path/to/file.m3u8}} | hlsq -query '{{bandwidth > 1000000}}'`
