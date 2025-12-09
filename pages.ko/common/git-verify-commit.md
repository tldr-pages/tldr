# git verify-commit

> 커밋의 GPG 검증 확인.
> 커밋이 검증되지 않으면, 지정된 옵션에 상관없이 아무것도 출력되지 않습니다.
> 더 많은 정보: <https://git-scm.com/docs/git-verify-commit>.

- 커밋에 대한 GPG 서명 확인:

`git verify-commit {{커밋_해시1 선택_커밋_해시2 ...}}`

- 커밋에 대한 GPG 서명을 확인하고 각 커밋의 세부 정보를 표시:

`git verify-commit {{커밋_해시1 선택_커밋_해시2 ...}} --verbose`

- 커밋에 대한 GPG 서명을 확인하고 원시 세부 정보를 출력:

`git verify-commit {{커밋_해시1 선택_커밋_해시2 ...}} --raw`
