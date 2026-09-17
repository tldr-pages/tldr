# az webapp

> Azure Cloud Services에서 호스팅되는 웹 애플리케이션을 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/webapp>.

- 웹 애플리케이션에 사용 가능한 런타임 나열:

`az webapp list-runtimes {{[-os|--os-type]}} {{windows|linux}}`

- 웹 애플리케이션 생성:

`az webapp up {{[-n|--name]}} {{이름}} {{[-l|--location]}} {{위치}} {{[-r|--runtime]}} {{런타임}}`

- 모든 웹 애플리케이션 나열:

`az webapp list`

- 특정 웹 애플리케이션 삭제:

`az webapp delete {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`
