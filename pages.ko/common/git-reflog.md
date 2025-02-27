# git reflog

> 로컬 Git 저장소의 브랜치, 태그, HEAD 등의 변경사항을 로그로 보여줍니다.
> 더 많은 정보: <https://git-scm.com/docs/git-reflog>.

- HEAD의 변경된 기록을 표시:

`git reflog`

- 지정된 브랜치의 변경된 기록을 표시:

`git reflog {{브랜치_이름}}`

- 변경된 기록의 최근 5개 항목만 표시:

`git reflog {{[-n|--max-count]}} 5`
