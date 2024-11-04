# zcmp

> 압축된 파일 비교.
> 더 많은 정보: <https://manned.org/zcmp>.

- `gzip`로 압축된 두 파일을 `cmp`로 비교:

`zcmp {{경로/대상/파일1.gz}} {{경로/대상/파일2.gz}}`

- 파일을 해당 gzipped 버전과 비교 (이미 `.gz`가 존재한다고 가정):

`zcmp {{경로/대상/파일}}`
