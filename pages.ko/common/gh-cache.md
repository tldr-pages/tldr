# gh cache

> GitHub Actions 캐시 관리.
> 더 많은 정보: <https://cli.github.com/manual/gh_cache>.

- 현재 저장소의 캐시 목록 표시:

`gh cache {{[ls|list]}}`

- 특정 저장소의 캐시 목록 표시:

`gh cache {{[ls|list]}} {{[-R|--repo]}} {{소유자}}/{{저장소}}`

- 특정 캐시 키 접두사를 가진 캐시 목록 표시:

`gh cache {{[ls|list]}} {{[-k|--key]}} {{키_접두사}}`

- 특정 브랜치의 캐시 목록 표시:

`gh cache {{[ls|list]}} {{[-r|--ref]}} refs/heads/{{브랜치_이름}}`

- 마지막 접근 시간이 가장 오래된 순으로 캐시 목록 정렬:

`gh cache {{[ls|list]}} {{[-S|--sort]}} last_accessed_at {{[-O|--order]}} asc`

- ID로 캐시 삭제:

`gh cache delete {{캐시_아이디}}`

- 키로 캐시 삭제:

`gh cache delete {{캐시_키}}`

- 모든 캐시 삭제:

`gh cache delete {{[-a|--all]}}`
