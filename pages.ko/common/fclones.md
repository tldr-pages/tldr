# fclones

> 효율적인 중복 파일 찾기 및 제거기.
> 더 많은 정보: <https://github.com/pkolaczk/fclones>.

- 현재 디렉터리에서 중복 파일 검색:

`fclones group .`

- 여러 디렉터리에서 중복 파일을 검색하고 결과를 캐시:

`fclones group --cache {{경로/대상/디렉터리1 경로/대상/디렉터리2}}`

- 하위 디렉터리를 건너 뛰고, 지정된 디렉터리에서만 중복 파일을 검색하고 결과를 파일에 저장:

`fclones group {{경로/대상/디렉터리}} --depth 1 > {{경로/대상/파일.txt}}`

- TXT 파일의 중복 파일을 다른 디렉터리로 이동:

`fclones move {{경로/대상/대상_디렉터리}} < {{경로/대상/파일.txt}}`

- 실제로 연결하지 않고 TXT 파일의 소프트 링크에 대해 연습 실행을 수행:

`fclones link --soft < {{경로/대상/파일.txt}} --dry-run 2 > /dev/null`

- 파일에 저장하지 않고 현재 디렉터리에서 최신 복사본을 삭제:

`fclones group . | fclones remove --priority newest`

- 중복 항목을 찾기 전에 EXIF 데이터를 제거하는 외부 명령을 사용하여 현재 디렉터리의 JPEG 파일을 전처리:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`
