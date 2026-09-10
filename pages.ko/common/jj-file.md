# jj file

> `jj` 저장소의 파일을 관리하고 확인.
> `annotate`, `list`, `search`, `show` 등 일부 하위 명령은 각각 별도의 사용 문서를 제공.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file>.

- 작업 복사본에서 추적 중인 파일 목록 표시:

`jj file list`

- 작업 복사본에 있는 파일 내용 출력:

`jj file show {{경로/대상/파일}}`

- 추적 중인 파일에서 지정한 패턴을 검색:

`jj file search {{[-p|--pattern]}} "{{패턴}}"`

- 파일 각 줄에 대한 변경 출처 정보 표시:

`jj file annotate {{경로/대상/파일}}`

- 작업 복사본에서 지정한 경로를 추적 대상으로 추가:

`jj file track {{경로/대상/파일_또는_디렉터리}}`

- 작업 복사본에서 지정한 경로의 추적을 주이:

`jj file untrack {{경로/대상/파일_또는_디렉터리}}`

- 파일의 실행 권한 비트 설정 또는 제거:

`jj file chmod {{[-x|--executable]}} {{경로/대상/파일}}`
