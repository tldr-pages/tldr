# reg flags

> 레지스트리 키에 플래그를 표시하거나 설정.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-flags>.

- 특정 키의 현재 플래그 표시:

`reg flags {{키_이름}} query`

- 특정 키에 하나 이상의 플래그 설정 및 언급되지 않은 플래그 해제:

`reg flags {{키_이름}} set {{플래그_이름1 플래그_이름2 ...}}`

- 특정 키와 그 [하위]키에 하나 이상의 플래그 설정:

`reg flags {{키_이름}} set {{플래그_이름1 플래그_이름2 ...}} /s`
