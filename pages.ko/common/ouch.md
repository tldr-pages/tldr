# ouch

> 파일 및 디렉터리를 압축하고 해제하는 명령줄 유틸리티.
> 더 많은 정보: <https://crates.io/crates/ouch>.

- 특정 파일 압축 해제:

`ouch decompress {{경로/대상/아카이브.tar.xz}}`

- 특정 위치에 파일 압축 해제:

`ouch decompress {{경로/대상/아카이브.tar.xz}} --dir {{경로/대상/폴더}}`

- 여러 파일 압축 해제:

`ouch decompress {{경로/대상/아카이브1.tar 경로/대상/아카이브2.tar.gz ...}}`

- 파일 압축:

`ouch compress {{경로/대상/파일1 경로/대상/파일2 ...}} {{경로/대상/아카이브.zip}}`
