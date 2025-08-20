# hg pull

> 지정된 저장소에서 로컬 저장소로 변경 사항을 가져옵니다.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/pull>.

- "기본" 소스 경로에서 가져오기:

`hg pull`

- 지정된 소스 저장소에서 가져오기:

`hg pull {{경로/대상/소스_저장소}}`

- 로컬 저장소를 원격의 최신 상태로 업데이트:

`hg pull --update`

- 원격 저장소가 관련이 없는 경우에도 변경 사항 가져오기:

`hg pull --force`

- 특정 리비전 변경 세트를 지정하여 가져오기:

`hg pull --rev {{리비전}}`

- 특정 브랜치를 지정하여 가져오기:

`hg pull --branch {{브랜치}}`

- 특정 북마크를 지정하여 가져오기:

`hg pull --bookmark {{북마크}}`
