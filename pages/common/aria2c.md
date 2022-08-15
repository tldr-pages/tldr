# aria2c

> Fast download utility.
> Supports HTTP(S), FTP, SFTP, BitTorrent, and Metalink.
> More information: <https://aria2.github.io>.

- Download a URI to a file:

`aria2c {{url}}`

- Download the file pointed to by the specified URI with the specified output name:

`aria2c --out={{filename}} {{url}}`

- Download multiple (different) files in parallel:

`aria2c --force-sequential {{false}} {{url_1}} {{url_2}}`

- Download from multiple sources with each URI pointing to the same file:

`aria2c {{url_1}} {{url_2}}`

- Download the URIs listed in a file with limited parallel downloads:

`aria2c --input-file={{filename}} --max-concurrent-downloads={{number_of_downloads}}`

- Download with multiple connections:

`aria2c --split={{number_of_connections}} {{url}}`

- FTP download with username and password:

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}`

- Limit download speed in bytes/s:

`aria2c --max-download-limit={{speed}} {{url}}`
