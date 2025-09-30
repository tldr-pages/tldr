# calibredb

> 전자책 데이터베이스를 조작하는 도구.
> Calibre 전자책 라이브러리의 일부.
> 더 많은 정보: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- 도서관의 전자책들을 추가 정보와 함께 리스트로 출력:

`calibredb list`

- 추가 정보를 표시하며 전자책 검색:

`calibredb list --search {{검색_용어}}`

- 전자책의 ID만 검색:

`calibredb search {{검색_용어}}`

- 라이브러리에 전자책 하나 이상 추가하기:

`calibredb add {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 디렉토리 내의 모든 전자책을 재귀적으로 라이브러리에 추가:

`calibredb add {{[-r|--recurse]}} {{경로/대상/디렉토리}}`

- 라이브러리에서 전자책을 하나 이상 제거하기. 전자책 ID 필요(위를 참조하시오):

`calibredb remove {{id1 id2 ...}}`
