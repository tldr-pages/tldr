# tmutil

> Time Machine 백업을 관리하는 도구. 대부분의 동사는 루트 권한이 필요합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/tmutil.8.html>.

- HFS+ 드라이브를 백업 대상으로 설정:

`sudo tmutil setdestination {{경로/대상/디스크_마운트_포인트}}`

- APF 공유 또는 SMB 공유를 백업 대상으로 설정:

`sudo tmutil setdestination "{{프로토콜://사용자[:비밀번호]@호스트/공유}}"`

- 주어진 대상을 목적지 목록에 추가:

`sudo tmutil setdestination -a {{대상}}`

- 자동 백업 활성화:

`sudo tmutil enable`

- 자동 백업 비활성화:

`sudo tmutil disable`

- 백업이 실행 중이 아니라면 시작하고 셸의 제어를 해제:

`sudo tmutil startbackup`

- 백업을 시작하고 완료될 때까지 대기:

`sudo tmutil startbackup -b`

- 백업 중지:

`sudo tmutil stopbackup`
