# az tag

> 리소스에 대한 태그를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/tag>.

- 태그 값 생성:

`az tag add-value {{[-n|--name]}} {{태그_이름}} --value {{태그_값}}`

- 구독에서 태그를 생성:

`az tag create {{[-n|--name]}} {{태그_이름}}`

- 구독에서 태그를 삭제:

`az tag delete {{[-n|--name]}} {{태그_이름}}`

- 구독의 모든 태그 나열:

`az tag list --resource-id /subscriptions/{{구독_아이디}}`

- 특정 태그 이름에 대한 태그 값 삭제:

`az tag remove-value {{[-n|--name]}} {{태그_이름}} --value {{태그_값}}`
