# winget

> 윈도우 패키지 매니저.
> 더 많은 정보: <https://learn.microsoft.com/windows/package-manager/winget>.

- 패키지 설치:

`winget install {{패키지}}`

- 패키지 제거 (참고: `remove` 대신 `uninstall` 을 사용할 수 있음):

`winget uninstall {{패키지}}`

- 패키지에 대한 정보 표시:

`winget show {{패키지}}`

- 패키지 검색:

`winget search {{패키지}}`

- 모든 패키지를 최신 버전으로 업그레이드:

`winget upgrade --all`

- 관리할 수 있는 모든 패키지 나열:

`winget list --source winget`

- 파일에서 패키지 가져오기 또는 설치된 패키지를 파일로 내보내기:

`winget {{import|export}} {{--import-file|--output}} {{경로/대상/파일}}`

- winget 매니페스트 패키지 저장소에 PR을 제출하기 전에 유효성 검사:

`winget validate {{경로/대상/매니페스트}}`
