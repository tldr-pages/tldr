# Test-Json

> 문자열이 유효한 JSON 문서인지 여부를 테스트합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- `stdin`에서 문자열이 JSON 형식인지 테스트:

`'{{문자열}}' | Test-Json`

- 문자열이 JSON 형식인지 테스트:

`Test-Json -Json '{{테스트_대상_json}}'`

- `stdin`에서 문자열이 특정 스키마 파일과 일치하는지 테스트:

`'{{문자열}}' | Test-Json -SchemaFile {{경로\대상\스키마_파일.json}}`
