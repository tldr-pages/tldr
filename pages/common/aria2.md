# aria2

> A lightweight multi-protocol & multi-source command-line download utility.
> Supports HTTP, HTTPS, FTP, SFTP, BitTorrent and Metalink.
> More information: <https://aria2.github.io/>.

- Download a web resource:

`aria2c {{http://example.org/myLinux.iso}}`

- Download a resource from multiple sources:

`aria2c {{http://mirror1.org/myLinux.iso}} {{http://mirror2.org/myLinux.iso}}`

- Download using 2 connections per host:

`aria2c -x{{2}} {{http://example.org/myLinux.iso}}`

- Download from a Metalink URI:

`aria2c {{http://example.org/myLinux.metalink}}`

- Download from a BitTorrent URI:

`aria2c {{http://example.org/myLinux.torrent}}`

- Download from a BitTorrent Magnet URI:

`aria2c {{'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'}}`

- Download URIs from a file:

`aria2c -i {{uris.txt}}`
