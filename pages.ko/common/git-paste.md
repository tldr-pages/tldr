# git paste

> `pastebinit`을 사용하여 커밋을 pastebin 사이트에 전송.
> `git-extras`의 일부.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>.

- 현재 브랜치와 업스트림 간의 패치를 `pastebinit`을 사용하여 pastebin에 전송:

`git paste`

- `git format-patch`에 옵션을 전달하여 다른 커밋 집합을 선택 ( `@^`는 HEAD의 부모를 선택하여 현재 체크아웃된 커밋을 전송):

`git paste {{@^}}`
