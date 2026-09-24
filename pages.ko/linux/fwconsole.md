# fwconsole

> FreePBX 시스템 (PBX 서버)를 관리하고 구성.
> 더 많은 정보: <https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>.

- FreePBX 설정 다시 불러오기:

`fwconsole reload`

- Asterisk와 FreePBX에 필요한 서비스 시작:

`fwconsole start`

- Asterisk와 FreePBX에 필요한 서비스 중지:

`fwconsole stop`

- 설정 조회 및 변경:

`fwconsole setting {{키워드}} {{새로운_값}}`

- 사용 가능한 백업 목록 표시:

`fwconsole backup --list`

- 사용 가능한 FreePBX 명령 목록 표시:

`fwconsole list`

- FreePBX에서 apache 사용자 소유가 필요한 모든 파일과 디렉터리의 소유권 변경:

`fwconsole chown`
