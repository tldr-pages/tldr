# aria2c

> 빠른 다운로드 유틸리티.
> HTTP(S), FTP, SFTP, BitTorrent 및 Metalink를 지원합니다.
> 더 많은 정보: <https://aria2.github.io/manual/en/html/aria2c.html>.

- 특정 URI를 파일로 다운로드:

`aria2c "{{url}}"`

- 특정 출력 이름을 가진 URI에서 파일을 다운로드:

`aria2c --out {{경로/대상/파일}} "{{url}}"`

- 여러 개의 서로 다른 파일을 병렬로 다운로드:

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- 다른 미러 사이트에서 동일한 파일을 다운로드:

`aria2c --checksum {{sha-256}}={{hash}} "{{url1}}" "{{url2}}" "{{urlN}}"`

- 특정 개수의 병렬 다운로드가 되고 있는 파일에 나열된 URI을 다운로드:

`aria2c --input-file {{경로/대상/파일}} --max-concurrent-downloads {{다운로드_횟수}}`

- 다중 연결로 다운로드:

`aria2c --split {{연결_개수}} "{{url}}"`

- 사용자 이름과 비밀번호를 사용하여 FTP 다운로드:

`aria2c --ftp-user {{사용자명}} --ftp-passwd {{패스워드}} "{{url}}"`

- 다운로드 속도를 바이트/초로 제한:

`aria2c --max-download-limit {{속도}} "{{url}}"`
