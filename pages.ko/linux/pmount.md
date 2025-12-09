# pmount

> 일반 사용자가 임의의 핫플러그 가능 장치를 마운트.
> 더 많은 정보: <https://manned.org/pmount>.

- 장치를 `/media/` 아래에 마운트(장치를 마운트 지점으로 사용):

`pmount {{/dev/to/block/device}}`

- 특정 파일시스템 타입으로 장치를 `/media/label`에 마운트:

`pmount --type {{파일시스템}} {{/dev/to/block/device}} {{라벨}}`

- CD-ROM을 읽기 전용 모드로 마운트(파일시스템 타입 ISO9660):

`pmount --type {{iso9660}} --read-only {{/dev/cdrom}}`

- NTFS로 포맷된 디스크를 읽기-쓰기 모드로 강제 마운트:

`pmount --type {{ntfs}} --read-write {{/dev/sdX}}`

- 마운트된 모든 이동식 장치 표시:

`pmount`
