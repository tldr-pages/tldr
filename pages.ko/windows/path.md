# path

> 실행 파일에 대한 검색 경로를 표시하거나 설정합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- 현재 경로 표시:

`path`

- 세미콜론으로 구분된 하나 이상의 디렉토리로 경로 설정:

`path {{경로\대상\디렉토리1 경로\대상\디렉토리2 ...}}`

- 원래 경로에 새 디렉토리 추가:

`path {{경로\대상\디렉토리}};%path%`

- 실행 파일을 현재 디렉토리에서만 검색하도록 명령 프롬프트를 설정:

`path ;`
