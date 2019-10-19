# aria2

> 一个轻量级多协议和多源命令行下载工具
> 支持 HTTP, HTTPS, FTP, SFTP, BitTorrent and Metalink.
> 主页：<https://aria2.github.io/>.

- 下载一个网络资源:

`aria2c {{http://example.org/myLinux.iso}}`

- 从多个源处下载一个资源:

`aria2c {{http://mirror1.org/myLinux.iso}} {{http://mirror2.org/myLinux.iso}}`

- 使用两个连接下载资源:

`aria2c -x{{2}} {{http://example.org/myLinux.iso}}`

- 从 Metalink URI 中下载资源:

`aria2c {{http://example.org/myLinux.metalink}}`

- 从 BitTorrent URI 中下载资源:

`aria2c {{http://example.org/myLinux.torrent}}`

- 从 BitTorrent Magnet URI 中下载资源:

`aria2c {{'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'}}`

- 从一个文件中下载资源:

`aria2c -i {{uris.txt}}`
