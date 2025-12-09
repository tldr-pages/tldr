# az apim

> Azure API Management 서비스를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/apim>.

- 리소스 그룹 내 API Management 서비스를 나열:

`az apim list {{[-g|--resource-group]}} {{리소스_그룹}}`

- API Management 서비스 인스턴스 생성:

`az apim create {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}} --publisher-email {{이메일}} --publisher-name {{이름}}`

- API Management 서비스 삭제:

`az apim delete {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- API Management 서비스 인스턴스의 세부정보 표시:

`az apim show {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- API Management 서비스 인스턴스 업데이트:

`az apim update {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`
