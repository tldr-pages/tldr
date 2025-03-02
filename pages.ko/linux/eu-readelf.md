# eu-readelf

> ELF 파일에 대한 정보를 표시합니다.
> 더 많은 정보: <https://manned.org/eu-readelf>.

- ELF 파일에 포함된 모든 추출 가능한 정보 표시:

`eu-readelf {{[-a|--all]}} {{경로/대상/파일}}`

- 모든 NOTE 세그먼트/섹션 또는 특정 세그먼트/섹션의 내용 표시:

`eu-readelf {{[-n--notes]}} {{.note.ABI-tag}} {{경로/대상/파일}}`
