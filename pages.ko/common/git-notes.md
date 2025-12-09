# git notes

> 객체 노트를 추가하거나 검사.
> 더 많은 정보: <https://git-scm.com/docs/git-notes>.

- 모든 노트와 연결된 객체 나열:

`git notes list`

- 주어진 객체에 연결된 모든 노트 나열 (기본값은 HEAD):

`git notes list [{{객체}}]`

- 주어진 객체에 연결된 노트 표시 (기본값은 HEAD):

`git notes show [{{객체}}]`

- 지정된 객체에 노트 추가 (기본 텍스트 편집기 열림):

`git notes append {{객체}}`

- 지정된 객체에 메시지를 지정하여 노트 추가:

`git notes append --message="{{메시지_텍스트}}"`

- 기존 노트 편집 (기본값은 HEAD):

`git notes edit [{{객체}}]`

- 한 객체에서 다른 객체로 노트 복사:

`git notes copy {{소스_객체}} {{대상_객체}}`

- 지정된 객체에 추가된 모든 노트 제거:

`git notes remove {{객체}}`
