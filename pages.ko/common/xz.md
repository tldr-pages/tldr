# xz

> XZ 및 LZMA 파일을 압축 또는 해제.
> 더 많은 정보: <https://manned.org/xz>.

- 파일을 xz로 압축:

`xz {{경로/대상/파일}}`

- XZ 파일 압축 해제:

`xz {{[-d|--decompress]}} {{경로/대상/파일.xz}}`

- 파일을 lzma로 압축:

`xz {{[-F|--format]}} lzma {{경로/대상/파일}}`

- LZMA 파일 압축 해제:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{경로/대상/파일.lzma}}`

- 파일 압축 해제 후 `stdout`에 쓰기 (`--keep` 포함):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{경로/대상/파일.xz}}`

- 파일을 압축하지만 원본을 삭제하지 않기:

`xz {{[-k|--keep]}} {{경로/대상/파일}}`

- 가장 빠른 압축으로 파일 압축:

`xz -0 {{경로/대상/파일}}`

- 최고의 압축으로 파일 압축:

`xz -9 {{경로/대상/파일}}`
