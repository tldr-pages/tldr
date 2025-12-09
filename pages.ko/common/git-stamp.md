# git stamp

> 마지막 커밋 메시지에 버그 추적기의 이슈 번호를 참조하거나 리뷰 페이지 링크를 추가합니다.
> `git-extras`의 일부입니다.
> 더 많은 정보: <https://manned.org/git-stamp>.

- 버그 추적기의 이슈 번호를 참조하여 마지막 커밋 메시지에 스탬프 추가:

`git stamp {{이슈_번호}}`

- 리뷰 페이지 링크를 추가하여 마지막 커밋 메시지에 스탬프 추가:

`git stamp {{리뷰 https://example.org/path/to/review}}`

- 이전 이슈를 새 이슈로 교체하여 마지막 커밋 메시지에 스탬프 추가:

`git stamp {{[-r|--replace]}} {{이슈_번호}}`
