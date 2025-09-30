# Resolve-Path

> 경로에서 와일드카드 문자를 확인하고 경로 내용을 표시합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- 홈 폴더 경로 확인:

`Resolve-Path {{~}}`

- UNC 경로 확인:

`Resolve-Path -Path "\\{{호스트명}}\{{경로\대상\파일}}"`

- 상대 경로 확인:

`Resolve-Path -Path {{경로\대상\파일_또는_디렉토리}} -Relative`
