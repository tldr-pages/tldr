# e2undo

> ext2/ext3/ext4 파일 시스템에 대한 undo 로그 재생.
> e2fsprogs 프로그램의 실패한 작업을 취소하는 데 사용할 수 있습니다.
> 더 많은 정보: <https://manned.org/e2undo>.

- 특정 undo 파일에 대한 정보 표시:

`e2undo -h {{경로/대상/undo_파일}} {{/dev/sdXN}}`

- 드라이런을 수행하고 재생할 후보 블록 표시:

`e2undo -nv {{경로/대상/undo_파일}} {{/dev/sdXN}}`

- undo 작업 수행:

`e2undo {{경로/대상/undo_파일}} {{/dev/sdXN}}`

- undo 작업 수행 및 자세한 정보 표시:

`e2undo -v {{경로/대상/undo_파일}} {{/dev/sdXN}}`

- 파일 시스템 블록을 덮어쓰기에 앞서 블록의 이전 내용을 undo 파일에 기록:

`e2undo -z {{경로/대상/file.e2undo}} {{경로/대상/undo_파일}} {{/dev/sdXN}}`
