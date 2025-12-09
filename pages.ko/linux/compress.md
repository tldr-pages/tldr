# compress

> Unix `compress` 명령어를 사용하여 파일 압축.
> 더 많은 정보: <https://manned.org/compress.1>.

- 특정 파일 압축:

`compress {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 파일 압축, 존재하지 않는 파일은 무시:

`compress -f {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 최대 압축 비트 지정 (9-16 비트):

`compress -b {{비트}}`

- `stdout`에 기록 (파일은 변경되지 않음):

`compress -c {{경로/대상/파일}}`

- 파일 압축 해제 (`uncompress`처럼 동작):

`compress -d {{경로/대상/파일}}`

- 압축 비율 표시:

`compress -v {{경로/대상/파일}}`
