# mksquashfs

> squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가합니다.
> 더 많은 정보: <https://manned.org/mksquashfs>.

- squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가 (`gzip`으로 기본 압축):

`mksquashfs {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}} {{파일시스템.squashfs}}`

- 특정 [comp]압축 알고리즘을 사용하여 squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가:

`mksquashfs {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}} {{파일시스템.squashfs}} -comp {{gzip|lzo|lz4|xz|zstd|lzma}}`

- squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가하면서 일부 제외:

`mksquashfs {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}} {{파일시스템.squashfs}} -e {{파일_또는_폴더1 파일_또는_폴더2 ...}}`

- gzip으로 끝나는 파일을 제외하고 squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가:

`mksquashfs {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}} {{파일시스템.squashfs}} -wildcards -e "{{*.gz}}"`

- 정규 표현식과 일치하는 파일을 제외하고 squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가:

`mksquashfs {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}} {{파일시스템.squashfs}} -regex -e "{{정규_표현식}}"`
