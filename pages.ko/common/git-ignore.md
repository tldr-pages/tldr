# git ignore

> `.gitignore` 파일을 표시/업데이트.
> `git-extras`의 일부. 같이 보기: `git ignore-io`.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>.

- 모든 전역 및 로컬 `.gitignore` 파일의 내용을 표시:

`git ignore`

- 파일을 비공개로 무시하고, `.git/info/exclude` 파일을 업데이트:

`git ignore {{파일_패턴}} --private`

- 파일을 로컬에서 무시하고, 로컬 `.gitignore` 파일을 업데이트:

`git ignore {{파일_패턴}}`

- 파일을 전역에서 무시하고, 전역 `.gitignore` 파일을 업데이트:

`git ignore {{파일_패턴}} --global`
