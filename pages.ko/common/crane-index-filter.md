# crane index filter

> 플랫폼 기반 필터링을 통해 원격 인덱스를 수정.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- 원격 인덱스 수정:

`crane index filter`

- os/arch{{/variant}}{{:osversion}}{{,<platform>}} 형식으로 기본에서 유지할 플랫폼을 지정:

`crane index filter --platform {{플랫폼1 플랫폼2 ...}}`

- 결과 이미지에 적용할 태그 지정:

`crane index filter {{[-t|--tags]}} {{태그_이름}}`

- 도움말 표시:

`crane index filter {{[-h|--help]}}`
