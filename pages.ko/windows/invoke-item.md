# Invoke-Item

> 파일을 기본 프로그램에서 엽니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- 파일을 기본 프로그램에서 열기:

`Invoke-Item -Path {{경로\대상\파일}}`

- 디렉토리 내의 모든 파일 열기:

`Invoke-Item -Path {{경로\대상\디렉토리}}\*`

- 디렉토리 내의 모든 PNG 파일 열기:

`Invoke-Item -Path {{경로\대상\디렉토리}}\*.png`

- 특정 키워드가 포함된 디렉토리 내의 모든 파일 열기:

`Invoke-Item -Path {{경로\대상\디렉토리}}\* -Include {{*키워드*}}`

- 특정 키워드를 포함하는 파일을 제외한 디렉토리 내부의 모든 파일을 열기:

`Invoke-Item -Path {{경로\대상\디렉토리}}\* -Exclude {{*키워드*}}`

- `Invoke-Item`을 통해 디렉토리 내부에서 어떤 파일이 열릴지 확인하기 위한 테스트 실행:

`Invoke-Item -Path {{경로\대상\디렉토리}}\* -WhatIf`
