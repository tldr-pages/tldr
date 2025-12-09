# del

> 하나 이상의 파일 삭제.
> PowerShell에서는 이 명령이 `Remove-Item`의 별칭입니다. 이 문서는 명령 프롬프트(`cmd`) 버전의 `del`을 기준으로 합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 동등한 PowerShell 명령의 문서 보기:

`tldr remove-item`

- 하나 이상의 파일 또는 패턴 삭제:

`del {{파일_패턴1 파일_패턴2 ...}}`

- 각 파일을 삭제하기 전에 확인 요청:

`del {{파일_패턴}} /p`

- 읽기 전용 파일 강제 삭제:

`del {{파일_패턴}} /f`

- 모든 하위 디렉토리에서 파일을 재귀적으로 삭제:

`del {{파일_패턴}} /s`

- 글로벌 와일드카드를 기반으로 파일 삭제 시 확인 요청 안 함:

`del {{파일_패턴}} /q`

- 도움말 표시 및 사용 가능한 속성 목록 보기:

`del /?`

- 지정된 속성을 기반으로 파일 삭제:

`del {{파일_패턴}} /a {{속성}}`
