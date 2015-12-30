# aria2c

> Fast download utility
> Supports HTTP(S), FTP, SFTP, BitTorrent, and Metalink

- Download a URI(include Metalink) to a file

`aria2c {{url}}`

- Download from multiple sources

`aria2c {{url_1}} {{url_2}}`

- Download the URIs listed in a file (one line one URI)

`aria2c -i {{filename}}`

- Download with multiple connections

`aria2c -s {{connections_num}} {{url}}`

- Limit download speed

`aria2c --max-download-limit {{200K}} {{url}}`

- FTP download with username and password

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}`
