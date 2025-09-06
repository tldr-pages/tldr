# git obliterate

> Git 저장소에서 파일을 삭제하고 해당 기록을 지웁니다.
> `git-extras`의 일부입니다.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>.

- 특정 파일의 존재를 지우기:

`git obliterate {{파일_이름_1 파일_이름_2 ...}}`

- 두 커밋 사이의 특정 파일 존재를 지우기:

`git obliterate {{파일_이름_1 파일_이름_2 ...}} -- {{커밋_해시_1}}..{{커밋_해시_2}}`
