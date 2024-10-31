# gunzip

> `gzip` (`.gz`) 아카이브에서 파일을 추출.
> 더 많은 정보: <https://manned.org/gunzip>.

- 아카이브에서 파일을 추출하고, 원본 파일이 있는 경우 교체:

`gunzip {{아카이브.tar.gz}}`

- 대상 목적지로 파일을 추출:

`gunzip --stdout {{아카이브.tar.gz}} > {{아카이브.tar}}`

- 파일을 추출하고 아카이브 파일을 보관:

`gunzip --keep {{아카이브.tar.gz}}`

- 압축 파일의 내용을 나열:

`gunzip --list {{file.txt.gz}}`

- `stdin`에서 아카이브 압축 풀기:

`cat {{경로/대상/아카이브.gz}} | gunzip`
