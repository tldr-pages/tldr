# forfiles

> 지정한 명령어를 실행할 파일을 선택.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- 현재 디렉토리에서 파일 검색:

`forfiles`

- 특정 디렉토리에서 파일 검색:

`forfiles /p {{경로\대상\폴더}}`

- 각 파일에 대해 지정된 명령어 실행:

`forfiles /c "{{명령어}}"`

- 특정 글로브 패턴을 사용하여 파일 검색:

`forfiles /m {{글로브_패턴}}`

- 파일을 재귀적으로 검색:

`forfiles /s`

- 5일 이상된 파일 검색:

`forfiles /d +{{5}}`
