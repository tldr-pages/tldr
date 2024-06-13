# git log

> 커밋 이력을 보여줍니다.
> 더 많은 정보: <https://git-scm.com/docs/git-log>.

- 현재 작업 디렉토리의 Git 리포지토리에서 현재 커밋을 기준으로 역순으로 커밋 시퀀스 보기:

`git log`

- 변경 사항을 포함해, 특정 파일 또는 디렉토리의 이력 보기:

`git log -p {{파일_또는_디렉토리_경로}}`

- 각 커밋에서 어떤 파일이 변경되었는지 개요 보기:

`git log --stat`

- 현재 브랜치의 커밋 그래프를 첫 줄만 사용해 보기:

`git log --oneline --graph`

- 전체 리포지토리의 모든 커밋, 태그 및 브랜치의 그래프 보기:

`git log --oneline --decorate --all --graph`

- 특정 문자열이 포함된 커밋 메시지만 보기 (대소문자 구분 없이):

`git log -i --grep {{검색_문자열}}`

- 특정 작성자의 마지막 N개의 커밋 보기:

`git log -n {{개수}} --author={{작성자}}`

- 두 날짜(yyyy-mm-dd) 사이의 커밋 보기:

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
