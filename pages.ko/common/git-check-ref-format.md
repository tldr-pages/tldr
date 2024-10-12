# git check-ref-format

> 참조 이름이 적절한지 확인하고, 그렇지 않으면 0이 아닌 상태로 종료.
> 더 많은 정보: <https://git-scm.com/docs/git-check-ref-format>.

- 지정된 참조 이름의 형식 확인:

`git check-ref-format {{refs/head/refname}}`

- 마지막으로 체크아웃한 브랜치 이름 출력:

`git check-ref-format --branch @{-1}`

- 참조 이름을 정규화:

`git check-ref-format --normalize {{refs/head/refname}}`
