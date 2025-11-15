# git write-tree

> 현재 색인에서 트리 객체를 생성하는 저수준 유틸리티.
> 더 많은 정보: <https://git-scm.com/docs/git-write-tree>.

- 현재 색인에서 트리 객체 생성:

`git write-tree`

- 디렉토리가 참조하는 객체가 객체 데이터베이스에 존재하는지 확인하지 않고 트리 객체 생성:

`git write-tree --missing-ok`

- 하위 디렉토리를 나타내는 트리 객체 생성 (지정된 하위 디렉토리에 대한 하위 프로젝트의 트리 객체를 작성할 때 사용):

`git write-tree --prefix {{하위_디렉토리}}/`
