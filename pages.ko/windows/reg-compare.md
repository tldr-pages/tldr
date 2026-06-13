# reg compare

> 레지스트리에서 키와 해당 값을 비교.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- 특정 키 아래의 모든 값을 다른 키와 비교:

`reg compare {{키_이름1}} {{키_이름2}}`

- 두 키 아래의 특정 [값]을 비교:

`reg compare {{키_이름1}} {{키_이름2}} /v {{값}}`

- 두 키의 모든 [하위 키]와 값을 비교:

`reg compare {{키_이름1}} {{키_이름2}} /s`

- 지정된 키 간의 일치하는 [동일] 항목만 출력:

`reg compare {{키_이름1}} {{키_이름2}} /os`

- 지정된 키 간의 차이점과 일치하는 항목([모두]) 출력:

`reg compare {{키_이름1}} {{키_이름2}} /oa`

- 두 키를 비교하고, [아무것도] 출력하지 않음:

`reg compare {{키_이름1}} {{키_이름2}} /on`
