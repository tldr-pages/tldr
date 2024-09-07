# devfsadm

> `/dev`의 관리 명령어입니다. `/dev` 네임스페이스를 유지합니다.
> 더 많은 정보: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- 새 디스크 검색:

`devfsadm -c disk`

- 미해결된 /dev 링크를 정리하고 새 장치를 검색:

`devfsadm -C -v`

- 시뮬레이션 실행 - 변경될 내용을 출력하지만 수정하지 않음:

`devfsadm -C -v -n`
