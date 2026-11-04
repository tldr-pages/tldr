# grafana cli admin

> Grafana 관리자 명령을 관리.
> 더 많은 정보: <https://grafana.com/docs/grafana/latest/administration/cli/#admin-commands>.

- 관리자 비밀번호 재설정:

`grafana cli admin reset-admin-password {{새로운_비밀번호}}`

- 지정한 사용자의 비밀번호 재설정:

`grafana cli admin reset-admin-password --user-id {{사용자_아이디}} {{새로운_비밀번호}}`

- 지정한 Grafana 홈 디렉터리를 사용하여 관리자 비밀번호 재설정:

`grafana cli --homepath {{path/to/grafana}} admin reset-admin-password {{새로운_비밀번호}}`

- 도움말 표시:

`grafana cli admin {{[-h|--help]}}`

- 버전 정보 표시:

`grafana cli admin {{[-v|--version]}}`
