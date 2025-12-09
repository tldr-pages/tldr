# reg delete

> 레지스트리에서 키 또는 해당 값을 삭제.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- 특정 레지스트리 키 삭제:

`reg delete {{키_이름}}`

- 특정 키 아래의 [v]alue 삭제:

`reg delete {{키_이름}} /v {{값}}`

- 지정된 키 아래의 모든 [v]alue를 재귀적으로 삭제:

`reg delete {{키_이름}} /va`

- 프롬프트 없이 강제로 특정 키 아래의 모든 [v]alue를 재귀적으로 삭제:

`reg delete {{키_이름}} /f /va`
