# hlsq

> CLI-Tool zum Einfärben und Filtern von HLS-Manifests.
> Weitere Informationen: <https://github.com/soldiermoth/hlsq/>.

- Zeige ein HLS-Manifest von einer URL an:

`{{curl --silent url}} | hlsq`

- Zeige ein HLS-Manifest aus einer Datei an:

`{{cat path/to/file.m3u8}} | hlsq`

- Lade eine URL kontinuierlich neu und aktualisiere die Ausgabe:

`hlsq -watch -url {{url}}`

- Filtere eine Multivarianten-Playlist nach einem Attribut (Textwert):

`{{cat path/to/file.m3u8}} | hlsq -query '{{type = SUBTITLES}}'`

- Filtere eine Multivarianten-Playlist nach einem Attribut (Zahlenwert):

`{{cat path/to/file.m3u8}} | hlsq -query '{{bandwidth > 1000000}}'`
