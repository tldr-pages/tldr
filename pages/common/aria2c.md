# aria2c

> Fast download utility
> Supports HTTP(S), FTP, SFTP, BitTorrent, and Metalink

- Download a URL to a file

`aria2c {{url}}`

- Download from multiple sources

`aria2c {{url_1}} {{url_2}}`

- Download Metalink

`aria2c {{magnet:?xt=urn:btih:...}}`

- Download with multiple connections

`aria2c -s {{20}} {{url}}`

- Limit download speed

`aria2c --max-download-limit {{200K}} {{url}}`

- FTP download with username and password

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}`
