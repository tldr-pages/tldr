# readelf

> ELF 파일에 대한 정보를 표시합니다.
> 더 많은 정보: <https://manned.org/readelf.1>.

- ELF 파일의 모든 정보 표시:

`readelf -all {{경로/대상/바이너리}}`

- ELF 파일에 포함된 모든 헤더 표시:

`readelf --headers {{경로/대상/바이너리}}`

- ELF 파일의 심볼 테이블 섹션에 있는 항목 표시(존재하는 경우):

`readelf --symbols {{경로/대상/바이너리}}`

- ELF 헤더 정보 표시:

`readelf --file-header {{경로/대상/바이너리}}`

- ELF 섹션 헤더 정보 표시:

`readelf --section-headers {{경로/대상/바이너리}}`
