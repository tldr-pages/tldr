# git verify-tag

> 태그의 GPG 서명을 검증.
> 태그가 서명되지 않은 경우 오류가 발생합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-verify-tag>.

- 태그의 GPG 서명 검증:

`git verify-tag {{태그1 선택적_태그2 ...}}`

- 태그의 GPG 서명을 검증하고 각 태그에 대한 세부 정보를 표시:

`git verify-tag {{태그1 선택적_태그2 ...}} --verbose`

- 태그의 GPG 서명을 검증하고 원시 세부 정보를 출력:

`git verify-tag {{태그1 선택적_태그2 ...}} --raw`
