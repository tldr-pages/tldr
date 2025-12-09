# git diff-tree

> 두 트리 객체를 통해 찾은 블롭의 내용과 모드를 비교.
> 더 많은 정보: <https://git-scm.com/docs/git-diff-tree>.

- 두 트리 객체 비교:

`git diff-tree {{tree-ish1}} {{tree-ish2}}`

- 특정 두 커밋 간의 변경 사항 표시:

`git diff-tree -r {{commit1}} {{commit2}}`

- 패치 형식으로 변경 사항 표시:

`git diff-tree {{[-p|--patch]}} {{tree-ish1}} {{tree-ish2}}`

- 특정 경로로 변경 사항 필터링:

`git diff-tree {{tree-ish1}} {{tree-ish2}} -- {{경로/대상/파일_또는_폴더}}`
