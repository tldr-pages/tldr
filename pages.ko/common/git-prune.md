# git prune

> Git 객체 데이터베이스에서 도달할 수 없는 모든 객체를 제거하는 명령.
> 이 명령은 종종 직접 사용되지 않고, Git gc에서 내부 명령으로 사용됩니다.
> 더 많은 정보: <https://git-scm.com/docs/git-prune>.

- Git prune에 의해 제거될 항목을 보고하지만 실제로 제거하지 않음:

`git prune {{[-n|--dry-run]}}`

- 도달할 수 없는 객체를 제거하고 제거된 항목을 `stdout`에 표시:

`git prune {{[-v|--verbose]}}`

- 진행 상황을 표시하면서 도달할 수 없는 객체를 제거:

`git prune --progress`
