# aria2c

> 빠른 다운로드 유틸리티.
> HTTP(S), FTP, SFTP, BitTorrent, and Metalink를 지원합니다.
> 더 많은 정보: <https://aria2.github.io>.

- URl을 파일에 다운로드:

`aria2c {{url}}`

- 다중 소스를 다운로드:

`aria2c {{url_1}} {{url_2}}`

- 파일에 나열된 URI 다운로드:

`aria2c -i {{filename}}`

- 여러 연결로 다운로드:

`aria2c -s {{connections_num}} {{url}}`

- 사용자 이름과 암호가 있는 FTP 다운로드:

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}`

- 다운로드 속도를 바이트/s로 제한:

`aria2c --max-download-limit={{speed}} {{url}}`
