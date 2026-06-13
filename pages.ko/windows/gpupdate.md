# gpupdate

> Windows 그룹 정책 설정을 확인하고 적용합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- 업데이트된 그룹 정책 설정 확인 및 적용:

`gpupdate`

- 업데이트할 그룹 정책 설정 지정:

`gpupdate /target:{{computer|user}}`

- 모든 그룹 정책 설정 재적용:

`gpupdate /force`

- 도움말 표시:

`gpupdate /?`
