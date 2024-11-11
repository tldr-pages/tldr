# e2fsck

> Linux ext2/ext3/ext4 파일 시스템을 검사합니다. 파티션은 마운트 해제되어 있어야 합니다.
> 더 많은 정보: <https://manned.org/e2fsck>.

- 파일 시스템을 검사하고 손상된 블록을 보고:

`sudo e2fsck {{/dev/sdXN}}`

- 파일 시스템을 검사하고 손상된 블록을 자동으로 복구:

`sudo e2fsck -p {{/dev/sdXN}}`

- 읽기 전용 모드로 파일 시스템 검사:

`sudo e2fsck -c {{/dev/sdXN}}`

- 불량 블록을 위한 철저하고 비파괴적인 읽기-쓰기 테스트를 수행하고 블랙리스트에 추가:

`sudo e2fsck -fccky {{/dev/sdXN}}`
