# git difftool

> 외부 diff 도구를 사용하여 파일 변경 사항을 표시합니다. `git diff`와 동일한 옵션과 인수를 허용합니다.
> 같이 보기: `git diff`.
> 더 많은 정보: <https://git-scm.com/docs/git-difftool>.

- 사용 가능한 diff 도구 나열:

`git difftool --tool-help`

- 기본 diff 도구를 meld로 설정:

`git config --global diff.tool "{{meld}}"`

- 기본 diff 도구를 사용하여 스테이징된 변경 사항 표시:

`git difftool --staged`

- 특정 도구(opendiff)를 사용하여 주어진 커밋 이후의 변경 사항 표시:

`git difftool --tool={{opendiff}} {{커밋}}`
