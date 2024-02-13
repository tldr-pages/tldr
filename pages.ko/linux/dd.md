# dd

> 파일 변환 및 복사.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/dd>.

- isohybrid 파일(예: `archlinux-xxx.iso`)에서 부팅 가능한 USB 드라이브를 만들고 진행 상황 표시:

`dd if={{경로/대상/파일.iso}} of={{/dev/usb_drive}} status=progress`

- 4 MiB 블록이 있는 다른 드라이브에 드라이브를 복제하고, 오류를 무시하고 진행 상황을 표시:

`dd if={{/dev/소스_드라이브}} of={{/dev/목적지_드라이브}} bs={{4M}} conv={{noerror}} status=progress`

- 커널 랜덤 드라이버를 사용하여 랜덤 100바이트의 파일 생성:

`dd if=/dev/urandom of={{경로/대상/랜덤_파일}} bs={{100}} count={{1}}`

- 디스크의 쓰기 성능 벤치마크:

`dd if=/dev/zero of={{경로/대상/1GB_파일}} bs={{1024}} count={{1000000}}`

- IMG 파일로 시스템 백업을 생성하고 진행 상황 표시:

`dd if={{/dev/드라이브_장치}} of={{경로/대상/파일.img}} status=progress`

- IMG 파일에서 드라이브를 복원하고 진행 상황을 표시:

`dd if={{경로/대상/파일.img}} of={{/dev/드라이브_장치}} status=progress`

- 진행 중인 dd 작업의 진행 상황을 확인 (다른 셸에서 이 명령어 실행):

`kill -USR1 $(pgrep -x dd)`
