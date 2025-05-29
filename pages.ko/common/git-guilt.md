# git guilt

> 스테이지되지 않은 변경 사항이 있는 파일에 대한 전체 블레임 수를 표시하거나 두 개의 리비전 간 블레임 변경을 계산.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-guilt>.

- 전체 블레임 수 표시:

`git guilt`

- 두 개의 리비전 간 블레임 변경 계산:

`git guilt {{첫번째_리비전}} {{마지막_리비전}}`

- 작성자 이메일을 이름 대신 표시:

`git guilt {{[-e|--email]}}`

- 블레임을 할당할 때 공백만 변경된 부분 무시:

`git guilt {{[-e|--email]}}`

- 지난 3주 동안의 블레임 델타 찾기:

`git guilt 'git log --until "3 weeks ago" --format "%H" {{[-n|--max-count]}} 1'`

- 지난 3주 동안의 블레임 델타 찾기 (git 1.8.5+):

`git guilt @{3.weeks.ago}`
