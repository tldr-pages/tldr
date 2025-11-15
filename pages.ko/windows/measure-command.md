# Measure-Command

> 스크립트 블록 및 cmdlet을 실행하는 데 걸리는 시간을 측정합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- 명령어를 실행하는 데 걸리는 시간 측정:

`Measure-Command { {{command}} }`

- `Measure-Command`에 파이프 입력 (파이프된 객체는 `Measure-Command`의 Expression 매개변수에 전달된 스크립트 블록에서 사용 가능):

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
