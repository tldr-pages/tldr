# webtorrent

> Interfața de linie de comandă pentru WebTorrent.
> Suportă magneți, URL-uri, hash-uri de informații și fișiere.torrent.
> Mai multe informaţii: <https://github.com/webtorrent/webtorrent-cli>

- Descarcă un torent:

`webtorrent download "{{torrent_id}}"`

- Transmite un torent la VLC media player:

`webtorrent download "{{torrent_id}}" --vlc`

- Transmite un torent pe un dispozitiv Digital Living Network Alliance (DLNA):

`webtorrent download "{{torrent_id}}" --dlna`

- Afișați o listă de fișiere pentru un anumit torent:

`webtorrent download "{{torrent_id}}" --select`

- Specificați un index de fișiere din torrent pentru a descărca:

`webtorrent download "{{torrent_id}}" --select {{index}}`

- Semănați un anumit fișier sau director:

`webtorrent seed {{path/to/file_or_directory}}`

- Creați un nou fișier torrent pentru calea fișierului specificat:

`webtorrent create {{path/to/file}}`

- Afișarea informațiilor pentru un fișier URI magnet sau `.torrent”:

`webtorrent info {{path/to/file_or_magnet}}`
