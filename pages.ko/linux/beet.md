# beet

> beets 미디어 라이브러리 관리.
> 더 많은 정보: <https://beets.readthedocs.io/en/stable/reference/cli.html>.

- 특정 디렉터리의 음악을 라이브러리에 추가하고, MusicBrainz를 사용해 올바른 태그를 자동으로 가져올 수 있게 시도:

`beet import {{경로/대상/디렉터리}}`

- 단일 음악 파일을 라이브러리에 추가하고, MusicBrainz를 사용해 올바른 태그를 자동으로 가져올 수 있게 시도:

`beet import {{[-s|--singletons]}} {{경로/대상/파일}}`

- 라이브러리 검색:

`beet list {{쿼리}}`

- 전체 라이브러리 통계 표시:

`beet stats`

- 특정 검색 조건에 대한 통계 표시:

`beet stats {{쿼리}}`
