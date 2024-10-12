# git range-diff

> 두 커밋 범위(예: 브랜치의 두 버전)를 비교.
> 더 많은 정보: <https://git-scm.com/docs/git-range-diff>.

- 두 개별 커밋의 변경 사항을 비교:

`git range-diff {{커밋_1}}^! {{커밋_2}}^!`

- 공통 조상으로부터 ours와 theirs의 변경 사항을 비교 (예: 인터랙티브 리베이스 후):

`git range-diff {{theirs}}...{{ours}}`

- 두 커밋 범위의 변경 사항을 비교 (예: `base1`에서 `base2`로 리베이스하는 동안 충돌이 적절하게 해결되었는지 확인):

`git range-diff {{base1}}..{{rev1}} {{base2}}..{{rev2}}`
