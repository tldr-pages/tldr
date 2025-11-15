# crane index append

> 원격 인덱스에 매니페스트를 추가.
> 하위 명령은 매니페스트가 추가된 (선택사항) 기본 인덱스를 기반으로 인덱스를 푸시.
> 추가된 매니페스트의 플랫폼은 구성 파일에서 유추되거나 실행 불가능한 경우 생략.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

- 원격 인덱스에 매니페스트를 추가:

`crane index append`

- 기본 인덱스에 추가할 매니페스트에 대한 참조:

`crane index append {{[-m|--manifest]}} {{매니페스트_이름1 매니페스트_이름2 ...}}`

- 결과 이미지에 적용할 태그:

`crane index append {{[-t|--tag]}} {{태그_이름}}`

- 비어있는 기본 인덱스에는 OCI 대신 Docker 미디어 유형을 지정:

`crane index append --docker-empty-base`

- 인덱스 자체가 아닌 각 하위의 항목을 추가 (기본값 true):

`crane index append --flatten`

- 도움말 표시:

`crane index append {{[-h|--help]}}`
