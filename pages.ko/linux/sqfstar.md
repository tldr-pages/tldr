# sqfstar

> tar 아카이브에서 squashfs 파일 시스템을 생성합니다.
> 더 많은 정보: <https://manned.org/sqfstar>.

- 압축되지 않은 tar 아카이브에서 기본적으로 `gzip`으로 압축된 squashfs 파일 시스템 생성:

`sqfstar {{파일_시스템.squashfs}} < {{아카이브.tar}}`

- `gzip`으로 압축된 tar 아카이브에서 특정 알고리즘으로 파일 시스템을 [comp]압축하여 squashfs 파일 시스템 생성:

`zcat {{아카이브.tar.gz}} | sqfstar -comp {{gzip|lzo|lz4|xz|zstd|lzma}} {{파일_시스템.squashfs}}`

- `xz`로 압축된 tar 아카이브에서 일부 파일을 제외하고 squashfs 파일 시스템 생성:

`xzcat {{아카이브.tar.xz}} | sqfstar {{파일_시스템.squashfs}} {{파일1 파일2 ...}}`

- `zstd`로 압축된 tar 아카이브에서 `.gz`로 끝나는 파일을 제외하고 squashfs 파일 시스템 생성:

`zstdcat {{아카이브.tar.zst}} | sqfstar {{파일_시스템.squashfs}} "{{*.gz}}"`

- `lz4`로 압축된 tar 아카이브에서 정규 표현식에 맞는 파일을 제외하고 squashfs 파일 시스템 생성:

`lz4cat {{아카이브.tar.lz4}} | sqfstar {{파일_시스템.squashfs}} -regex "{{정규_표현식}}"`
