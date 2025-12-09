# New-Item

> 새 파일, 디렉토리, 심볼릭 링크 또는 레지스트리 항목을 만듭니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- 새 빈 파일 만들기 ( `touch`와 동일):

`New-Item {{경로\대상\파일}}`

- 새 디렉토리 만들기:

`New-Item -ItemType Directory {{경로\대상\디렉토리}}`

- 지정된 내용으로 새 텍스트 파일 만들기:

`New-Item {{경로\대상\파일}} -Value {{내용}}`

- 동일한 텍스트 파일을 여러 위치에 쓰기:

`New-Item {{경로\대상\파일1 , 경로\대상\파일2 , ...}} -Value {{내용}}`

- 파일 또는 디렉토리에 심볼릭 링크\하드 링크\교차점 만들기:

`New-Item -ItemType {{SymbolicLink|HardLink|Junction}} -Path {{경로\대상\링크_파일}} -Target {{경로\대상\소스_파일_또는_디렉토리}}`

- 새 빈 레지스트리 항목 만들기 (REG_SZ 사용 시 `New-ItemProperty` 또는 `Set-ItemProperty` 사용):

`New-Item {{경로\대상\레지스트리_키}}`

- 지정된 값으로 새 빈 레지스트리 항목 만들기:

`New-Item {{경로\대상\레지스트리_키}} -Value {{값}}`
