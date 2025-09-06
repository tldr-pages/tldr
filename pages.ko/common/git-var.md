# git var

> Git 논리 변수의 값을 출력.
> `git var`보다 `git config`를 사용하는 것이 좋습니다.
> 더 많은 정보: <https://git-scm.com/docs/git-var>.

- Git 논리 변수의 값을 출력:

`git var {{GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER}}`

- 모든 Git 논리 변수를 [l]리스트:

`git var -l`
