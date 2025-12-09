# animdl

> 매우 효율적으로 강력하며, 빠른 애니메이션 스크레이퍼.
> 참고: `ani-cli`.
> 더 많은 정보: <https://github.com/justfoolingaround/animdl>.

- 특정 애니메이션 다운로드:

`animdl download {{애니메이션_제목}}`

- 에피소드 범위를 지정하여 특정 애니메이션을 다운로드:

`animdl download {{애니메이션_제목}} {{[-r|--range]}} {{시작_에피소드}}-{{종료_에피소드}}`

- 다운로드 디렉터리를 지정하여 특정 애니메이션을 다운로드:

`animdl download {{애니메이션_제목}} {{[-d|--download-dir]}} {{경로/대상/다운로드_디렉터리}}`

- 특정 애니메이션의 스트림 URL을 확인:

`animdl grab {{애니메이션_제목}}`

- 다음주에 예정된 애니메이션 일정을 표시:

`animdl schedule`

- 특정 애니메이션 검색:

`animdl search {{애니메이션_제목}}`

- 특정 애니메이션 스트리밍:

`animdl stream {{애니메이션_제목}}`

- 특정 애니메이션의 최신 에피소드를 스트리밍:

`animdl stream {{애니메이션_제목}} {{[-s|--special]}} latest`
