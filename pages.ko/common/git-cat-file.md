# git cat-file

> Git 저장소 객체의 콘텐츠 또는 유형 및 크기 정보를 제공합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-cat-file>.

- HEAD 커밋의 크기(바이트 단위) 확인:

`git cat-file -s HEAD`

- 주어진 Git 객체의 유형(blob, tree, commit, tag) 확인:

`git cat-file -t {{8c442dc3}}`

- 주어진 Git 객체의 유형에 따라 콘텐츠를 보기 좋게 출력:

`git cat-file -p {{HEAD~2}}`
