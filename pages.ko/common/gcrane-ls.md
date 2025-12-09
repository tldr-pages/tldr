# gcrane ls

> 저장소의 태그 나열.
> 태그, 매니페스트 및 하위 저장소를 나열할 수 있는 `crane ls`보다 더 복잡한 형식.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 태그 목록 나열:

`gcrane ls {{레포지토리}}`

- 레지스트리의 응답 형식을 JSON으로 지정:

`gcrane ls {{레포지토리}} --json`

- 레포지토리를 통해 반복할지 여부 결정:

`gcrane ls {{레포지토리}} {{[-r|--recursive]}}`

- 도움말 표시:

`gcrane ls {{[-h|--help]}}`
