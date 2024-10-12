# git show-index

> Git 저장소의 패키지된 아카이브 색인 표시.
> 더 많은 정보: <https://git-scm.com/docs/git-show-index>.

- Git 패키지 파일의 IDX 파일을 읽고 내용을 `stdout`에 덤프:

`git show-index {{경로/대상/파일.idx}}`

- 색인 파일의 해시 알고리즘 지정 (실험적):

`git show-index --object-format={{sha1|sha256}} {{경로/대상/파일}}`
