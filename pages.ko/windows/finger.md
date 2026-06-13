# finger

> 지정된 시스템의 사용자 정보 반환.
> 원격 시스템은 Finger 서비스를 실행 중이어야 합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- 특정 사용자에 대한 정보 표시:

`finger {{사용자}}@{{호스트}}`

- 지정된 호스트의 모든 사용자에 대한 정보 표시:

`finger @{{호스트}}`

- 더 긴 형식으로 정보 표시:

`finger {{사용자}}@{{호스트}} -l`

- 도움말 정보 표시:

`finger /?`
