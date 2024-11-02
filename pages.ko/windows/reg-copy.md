# reg copy

> 레지스트리에서 키와 그 값을 복사.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- 레지스트리 키를 새로운 레지스트리 위치로 복사:

`reg copy {{old_key_name}} {{new_key_name}}`

- 레지스트리 키를 재귀적으로 (모든 [s]ubkeys 포함) 새로운 레지스트리 위치로 복사:

`reg copy {{old_key_name}} {{new_key_name}} /s`

- [f]orcefully (프롬프트 없이) 레지스트리 키 복사:

`reg copy {{old_key_name}} {{new_key_name}} /f`
