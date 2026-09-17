# apptainer search

> Container Library에서 컨테이너 이미지를 검색하는 명령어.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_search.html>.

- 쿼리와 일치하는 컨테이너 이미지 검색:

`apptainer search {{쿼리}}`

- 특정 아키텍처의 컨테이너 이미지 검색:

`apptainer search --arch {{amd64|arm64|386|ppc64le|s390x}} {{쿼리}}`

- 서명된 컨테이너 이미지만 검색:

`apptainer search --signed {{쿼리}}`

- 특정 Container Library에서 검색:

`apptainer search --library {{라이브러리_주소}} {{쿼리}}`

- 도움말 표시:

`apptainer search {{[-h|--help]}}`
