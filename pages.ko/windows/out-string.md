# Out-String

> 입력 객체를 문자열로 출력합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- 호스트 정보를 문자열로 출력:

`Get-Alias | Out-String`

- 모든 객체를 단일 문자열로 연결하는 대신 각 객체를 문자열로 변환:

`Get-Alias | Out-String -Stream`

- `Width` 매개변수를 사용하여 잘림을 방지:

`@{TestKey = ('x' * 200)} | Out-String -Width {{250}}`
