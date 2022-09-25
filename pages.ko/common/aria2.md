# aria2

> 경량 멀티 프로토콜 및 멀티 소스 명령줄 다운로드 유틸리티입니다.
> HTTP, HTTPS, FTP, SFTP, BitTorrent와 Metalink를 지원합니다.
> 더 많은 정보: <https://aria2.github.io/>.

- 웹 리소스 다운로드:

`aria2c {{http://example.org/myLinux.iso}}`

- 멀티 소스 리소스 다운로드:

`aria2c {{http://mirror1.org/myLinux.iso}} {{http://mirror2.org/myLinux.iso}}`

- 호스트당 2개의 연결을 사용하여 다운로드:

`aria2c -x{{2}} {{http://example.org/myLinux.iso}}`

- Metalink URL로 다운로드:

`aria2c {{http://example.org/myLinux.metalink}}`

- BitTorrent URI로 다운로드:

`aria2c {{http://example.org/myLinux.torrent}}`

- BitTorrent Magnet URI로 다운로드:

`aria2c {{'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'}}`

- 파일로 URls 다운로드:

`aria2c -i {{uris.txt}}`
