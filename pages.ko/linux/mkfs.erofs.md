# mkfs.erofs

> 이미지 내에 EROFS 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.erofs>.

- 루트 디렉토리를 기반으로 EROFS 파일 시스템 생성:

`mkfs.erofs image.erofs root/`

- 특정 UUID를 가진 EROFS 이미지 생성:

`mkfs.erofs -U {{UUID}} image.erofs root/`

- 압축된 EROFS 이미지 생성:

`mkfs.erofs -zlz4hc image.erofs root/`

- 모든 파일의 소유자가 root인 EROFS 이미지 생성:

`mkfs.erofs --all-root image.erofs root/`
