# where

> 검색 패턴과 일치하는 파일의 위치를 표시합니다.
> 기본적으로 현재 작업 디렉토리와 PATH 환경 변수의 경로를 폴더로 설정합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- 파일 패턴의 위치 표시:

`where {{파일_패턴}}`

- 파일 크기와 날짜를 포함하여 파일 패턴의 위치 표시:

`where /T {{파일_패턴}}`

- 지정된 경로에서 파일 패턴을 재귀적으로 검색:

`where /R {{경로\대상\폴더}} {{파일_패턴}}`

- 파일 패턴의 위치에 대한 오류 코드를 자동으로 반환:

`where /Q {{파일_패턴}}`
