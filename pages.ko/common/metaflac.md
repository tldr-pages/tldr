# metaflac

> FLAC 오디오 파일의 메타데이터 조회 및 수정.
> 관련 항목: `flac`.
> 더 많은 정보: <https://xiph.org/flac/documentation_tools_metaflac.html>.

- FLAC 파일의 모든 태그 표시:

`metaflac --show-all-tags {{경로/대상/파일.flac}}`

- FLAC 파일로부터 특정 태그만 표시:

`metaflac --show-tag {{태그_이름1}} --show-tag {{태그_이름2}} {{경로/대상/파일.flac}}`

- FLAC 파일 내 태그 설정:

`metaflac --set-tag "{{태그_이름}}={{태그_값}}" {{경로/대상/파일.flac}}`

- FLAC 파일 내 특정 이름의 태그를 제거:

`metaflac --remove-tag {{태그_이름}} {{경로/대상/파일.flac}}`

- FLAC 파일로부터 모든 태그 제거:

`metaflac --remove-all-tags {{경로/대상/파일.flac}}`

- 파일에서 태그 가져오기 (`NAME=VALUE` 형식):

`metaflac --import-tags-from {{경로/대상/태그.txt}} {{경로/대상/파일.flac}}`

- FLAC 파일의 모든 메타데이터 블록 표시:

`metaflac --list {{경로/대상/파일.flac}}`

- FLAC 파일의 샘플 레이트와 채널 수 표시:

`metaflac --show-sample-rate --show-channels {{경로/대상/파일.flac}}`
