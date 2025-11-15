# Select-String

> PowerShell에서 문자열과 파일에서 텍스트를 찾습니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> `Select-String`을 UNIX의 `grep`이나 Windows의 `findstr.exe`와 유사하게 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- 파일 내에서 패턴 검색:

`Select-String -Path "{{경로\대상\파일}}" -Pattern '{{검색_패턴}}'`

- 정확한 문자열 검색 (정규식 비활성화):

`Select-String -SimpleMatch "{{정확한_문자열}}" {{경로\대상\파일}}`

- 현재 디렉토리의 모든 `.ext` 파일에서 패턴 검색:

`Select-String -Path "{{*.ext}}" -Pattern '{{검색_패턴}}'`

- 패턴과 일치하는 줄 앞뒤의 지정된 줄 수 캡처:

`Select-String --Context {{2,3}} "{{검색_패턴}}" {{경로\대상\파일}}`

- `stdin`에서 패턴과 일치하지 않는 줄 검색:

`Get-Content {{경로\대상\파일}} | Select-String --NotMatch "{{검색_패턴}}"`
