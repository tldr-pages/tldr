# fsck

> 파일 시스템의 무결성을 검사하거나 복구합니다. 명령어 실행 시 파일 시스템은 마운트 해제되어 있어야 합니다.
> 더 많은 정보: <https://manned.org/fsck>.

- 파일 시스템 `/dev/sdXN`의 손상된 블록을 보고:

`sudo fsck {{/dev/sdXN}}`

- 파일 시스템 `/dev/sdXN`의 손상된 블록을 보고, 각 블록을 복구할지 사용자에게 상호작용으로 선택하게 함:

`sudo fsck -r {{/dev/sdXN}}`

- 파일 시스템 `/dev/sdXN`의 손상된 블록을 보고, 자동으로 복구:

`sudo fsck -a {{/dev/sdXN}}`
