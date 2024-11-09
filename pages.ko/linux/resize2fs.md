# resize2fs

> ext2, ext3 또는 ext4 파일 시스템 크기 조정.
> 기본 파티션 크기를 조정하지 않습니다. 파일 시스템을 먼저 마운트 해제해야 할 수도 있으며, 자세한 내용은 man 페이지를 참조하세요.
> 더 많은 정보: <https://manned.org/resize2fs>.

- 파일 시스템을 자동으로 크기 조정:

`resize2fs {{/dev/sdXN}}`

- 진행 표시줄을 표시하며 파일 시스템을 40G 크기로 조정:

`resize2fs -p {{/dev/sdXN}} {{40G}}`

- 파일 시스템을 가능한 최소 크기로 축소:

`resize2fs -M {{/dev/sdXN}}`
