# hg push

> 로컬 저장소의 변경 사항을 지정된 대상으로 푸시.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/push>.

- "기본" 원격 경로로 변경 사항 푸시:

`hg push`

- 지정된 원격 저장소로 변경 사항 푸시:

`hg push {{경로/대상/저장소}}`

- 존재하지 않는 경우 새 브랜치 푸시 (기본적으로 비활성화됨):

`hg push --new-branch`

- 특정 리비전 체인지셋을 지정하여 푸시:

`hg push --rev {{리비전}}`

- 특정 브랜치를 지정하여 푸시:

`hg push --branch {{브랜치}}`

- 특정 북마크를 지정하여 푸시:

`hg push --bookmark {{북마크}}`
