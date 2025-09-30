# pbzip2

> `bzip2` 파일 압축기의 병렬 구현.
> 같이 보기: `bzip2`, `tar`.
> 더 많은 정보: <https://manned.org/pbzip2>.

- 파일 압축:

`pbzip2 {{경로/대상/파일}}`

- 지정된 프로세서 수를 사용하여 파일 압축:

`pbzip2 -p{{4}} {{경로/대상/파일}}`

- 파일 [d]압축:

`pbzip2 --decompress {{경로/대상/압축_파일.bz2}}`

- 도움말 표시:

`pbzip2 -h`
