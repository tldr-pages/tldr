# az acr

> Azure Container Registries를 사용해 프라이빗 레지스트리를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/acr>.

- 관리형 컨테이너 레지스트리를 생성:

`az acr create --name {{레지스트리_이름}} --resource-group {{리소스_그룹}} --sku {{sku}}`

- 레지스트리에 로그인:

`az acr login --name {{레지스트리_이름}}`

- ACR용 로컬 이미지에 태그를 지정:

`docker tag {{이미지_이름}} {{레지스트리_이름}}.azurecr.io/{{이미지_이름}}:{{태그}}`

- 이미지를 레지스트리에 푸시:

`docker push {{레지스트리_이름}}.azurecr.io/{{이미지_이름}}:{{태그}}`

- 레지스트리에서 이미지를 가져옴:

`docker pull {{레지스트리_이름}}.azurecr.io/{{이미지_이름}}:{{태그}}`

- 레지스트리에서 이미지 삭제:

`az acr repository delete --name {{레지스트리_이름}} --repository {{이미지_이름}}:{{태그}}`

- 관리형 컨테이너 레지스트리를 삭제:

`az acr delete --name {{레지스트리_이름}} --resource-group {{리소스_그룹}} --yes`

- 레지스트리 내의 이미지 목록 나열:

`az acr repository list --name {{레지스트리_이름}} --output table`
