# git symbolic-ref

> 참조를 저장하는 파일을 읽고, 변경하거나 삭제합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-symbolic-ref>.

- 이름으로 참조 저장:

`git symbolic-ref refs/{{이름}} {{참조}}`

- 업데이트 이유를 포함한 메시지와 함께 이름으로 참조 저장:

`git symbolic-ref -m "{{메시지}}" refs/{{이름}} refs/heads/{{브랜치_이름}}`

- 이름으로 참조 읽기:

`git symbolic-ref refs/{{이름}}`

- 이름으로 참조 삭제:

`git symbolic-ref --delete refs/{{이름}}`

- 스크립팅을 위해 `--quiet`로 오류를 숨기고 `--short`를 사용하여 간소화하기 ("refs/heads/X"가 "X"로 출력됨):

`git symbolic-ref --quiet --short refs/{{이름}}`
