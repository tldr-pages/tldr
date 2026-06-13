# fsck

> 파일 시스템의 무결성을 점검하거나 복구합니다. 명령어를 실행할 때 파일 시스템은 마운트 해제되어 있어야 합니다.
> 필요에 따라 `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, `fsck_udf`를 호출하는 래퍼입니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- 파일 시스템 `/dev/sdX`의 무결성을 점검하고 손상된 블록을 보고:

`fsck {{/dev/sdX}}`

- 파일 시스템 `/dev/sdX`가 깨끗할 경우에만 점검하고, 손상된 블록을 보고하며 사용자가 각 블록을 복구할지 선택하도록 상호작용:

`fsck -f {{/dev/sdX}}`

- 파일 시스템 `/dev/sdX`가 깨끗할 경우에만 점검하고, 손상된 블록을 보고하며 자동으로 복구:

`fsck -fy {{/dev/sdX}}`

- 파일 시스템 `/dev/sdX`의 무결성을 점검하고, 깔끔하게 마운트 해제되었는지 보고:

`fsck -q {{/dev/sdX}}`
