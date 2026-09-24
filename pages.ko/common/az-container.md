# az container

> Azure Container Instances 관리.
> `azure-cli`의 일부 (`az`).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/container>.

- 컨테이너 그룹에 컨테이너 생성:

`az container create {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{이름}} --image {{이미지_이름}} {{[-os|--os-type]}} {{windows|linux}} --cpu {{cpu_코어_개수}} --memory {{memory_in_GB}}`

- 실행 중인 컨테이너에서 명령어 실행:

`az container exec {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{컨테이너_그룹_이름}} --exec-command "{{명령어}}"`

- 컨테이너 그룹 안 컨테이너 로그 확인:

`az container logs {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- 컨테이너 그룹 상세 정보 조회:

`az container show {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- 컨테이너 그룹 내 모든 컨테이너 시작:

`az container start {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- 컨테이너 그룹 내 모든 컨테이너 중지:

`az container stop {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- 컨테이너 그룹 삭제:

`az container delete {{[-n|--name]}} {{이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`
