# Measure-Object

> 객체의 숫자 속성과 문자열 객체(예: 텍스트 파일)의 문자, 단어 및 줄을 계산합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-object>.

- 디렉토리의 파일 및 폴더 수 계산:

`Get-ChildItem | Measure-Object`

- `Measure-Command`에 파이프 입력 (파이프된 객체는 `Measure-Command`의 Expression 매개변수에 전달된 스크립트 블록에서 사용 가능):

`"One", "Two", "Three", "Four" | Set-Content -Path "{{경로\대상\파일}}"; Get-Content "{{경로\대상\파일}}"; | Measure-Object -Character -Line -Word`
