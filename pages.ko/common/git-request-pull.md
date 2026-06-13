# git request-pull

> 업스트림 프로젝트에 변경 사항을 병합해 달라고 요청하는 요청서를 생성.
> 더 많은 정보: <https://git-scm.com/docs/git-request-pull>.

- v1.1 릴리스와 지정된 브랜치 간의 변경 사항을 요약한 요청서 생성:

`git request-pull {{v1.1}} {{https://example.com/project}} {{브랜치_이름}}`

- `foo` 브랜치의 v0.1 릴리스와 로컬 `bar` 브랜치 간의 변경 사항을 요약한 요청서 생성:

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`
