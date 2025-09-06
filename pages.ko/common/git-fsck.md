# git fsck

> Git 저장소 색인의 노드 유효성과 연결성을 확인.
> 수정 작업은 수행하지 않음.
> 같이 보기: `git gc` (dangling blobs 정리).
> 더 많은 정보: <https://git-scm.com/docs/git-fsck>.

- 현재 저장소 확인:

`git fsck`

- 발견된 모든 태그 나열:

`git fsck --tags`

- 발견된 모든 루트 노드 나열:

`git fsck --root`
