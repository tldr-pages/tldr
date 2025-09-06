# Test-NetConnection

> 연결에 대한 진단 정보를 표시합니다.
> 참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- 연결을 테스트하고 자세한 결과를 표시:

`Test-NetConnection -InformationLevel Detailed`

- 지정된 포트 번호를 사용하여 원격 호스트에 대한 연결을 테스트:

`Test-NetConnection -ComputerName {{아이피_또는_호스트명}} -Port {{포트_번호}}`
