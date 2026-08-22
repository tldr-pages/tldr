# jj git push

> Git 원격 저장소 푸시.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git-push>.

- 저장한 원격 저장소로 북마크 푸시 (기본값은 `git.push` 설정):

`jj git push {{[-b|--bookmark]}} {{북마크}} --remote {{원격_저장소}}`

- 새로운 북마크 푸시:

`jj git push {{[-b|--bookmark]}} {{북마크}} {{[-N|--allow-new]}}`

- 추적 중인 모든 북마크 푸시:

`jj git push --tracked`

- 모든 북마크 푸시 (새 북마크 포함):

`jj git push --all`

- 지정한 리비전을 가리키는 모든 북마크 푸시:

`jj git push {{[-r|--revisions]}} {{revset}}`

- 새로운 북마크를 생성하여 변경/커밋 푸시 (북마크 이름은 `templates.git_push_bookmark` 설정을 따르며, 기본값은 `"push-" ++ change_id.short()`):

`jj git push {{[-c|--change]}} {{revset}}`

- 지정한 이름으로 리비전 푸시:

`jj git push --named {{이름}}={{리비전}}`
