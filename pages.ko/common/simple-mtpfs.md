# simple-mtpfs

> FUSE를 사용하여 MTP 장치 (예: Android 휴대폰)를 파일 시스템으로 마운트.
> 더 많은 정보: <https://manned.org/simple-mtpfs>.

- 사용 가능한 MTP 장치 목록 표시:

`simple-mtpfs {{[-l|--list-devices]}}`

- 장치를 지정한 디렉터리에 마운트:

`simple-mtpfs {{마운트_포인트}}`

- 특정 장치를 지정한 디렉터리에 마운트 (여러 장치가 연결된 경우 유용):

`simple-mtpfs --device {{number}} {{마운트_포인트}}`

- 파일 시스템 마운트 해제:

`umount {{마운트_포인트}}`
