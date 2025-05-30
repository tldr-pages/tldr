# nxc

> 네트워크 서비스 열거 및 익스플로잇 도구.
> `smb`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- 지정된 프로토콜에 대한 사용 가능한 모듈:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-L|--list-modules]}}`

- 지정된 모듈에 대한 사용 가능한 옵션 나열:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{모듈_이름}} --options`

- 모듈에 대한 옵션 지정:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{모듈_이름}} -o {{옵션_이름}}={{옵션_값}}`

- 지정된 프로토콜에 대한 사용 가능한 옵션 보기:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-h|--help]}}`
