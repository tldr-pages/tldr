# git cherry

> 아직 상류에 적용되지 않은 커밋을 찾습니다.
> 더 많은 정보: <https://git-scm.com/docs/git-cherry>.

- 상류에 동등한 커밋이 있는 커밋(및 그 메시지) 표시:

`git cherry {{[-v|--verbose]}}`

- 다른 상류 및 주제 브랜치 지정:

`git cherry {{origin}} {{topic}}`

- 주어진 한계 내의 커밋만 제한:

`git cherry {{origin}} {{topic}} {{base}}`
