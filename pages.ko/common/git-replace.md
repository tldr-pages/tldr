# git replace

> 객체를 대체하기 위한 참조를 생성, 목록화 및 삭제.
> 더 많은 정보: <https://git-scm.com/docs/git-replace>.

- 특정 커밋을 다른 커밋으로 대체하고, 다른 커밋은 변경하지 않음:

`git replace {{객체}} {{대체_객체}}`

- 주어진 객체에 대한 기존 대체 참조 삭제:

`git replace --delete {{객체}}`

- 객체의 내용을 대화형으로 편집:

`git replace --edit {{객체}}`
