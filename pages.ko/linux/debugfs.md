# debugfs

> 대화형 ext2/ext3/ext4 파일 시스템 디버거.
> 더 많은 정보: <https://manned.org/debugfs>.

- 파일 시스템을 읽기 전용 모드로 열기:

`debugfs {{/dev/sdXN}}`

- 파일 시스템을 읽기/쓰기 모드로 열기:

`debugfs -w {{/dev/sdXN}}`

- 지정된 파일에서 명령을 읽어 실행하고 종료:

`debugfs -f {{경로/대상/명령_파일}} {{/dev/sdXN}}`

- debugfs 콘솔에서 파일 시스템 통계 보기:

`stats`

- 파일 시스템 닫기:

`close -a`

- 사용 가능한 모든 명령 나열:

`lr`
