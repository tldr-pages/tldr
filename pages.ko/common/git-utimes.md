# git utimes

> 파일의 수정 시간을 마지막 커밋 날짜로 변경. 작업 트리 또는 색인에 있는 파일은 건드리지 않습니다.
> `git-extras`의 일부.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-utimes>.

- 모든 파일의 수정 시간을 마지막 커밋 날짜로 변경:

`git utimes`

- 마지막 커밋 날짜보다 최신인 파일의 수정 시간을 변경하고, 로컬 리포지토리에서 커밋된 파일의 원래 수정 시간을 유지:

`git utimes --newer`
