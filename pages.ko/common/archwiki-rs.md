# archwiki-rs

> ArchWiki에서 페이지를 읽고 검색하고 다운로드.
> 더 많은 정보: <https://gitlab.com/lucifayr/archwiki-rs>.

- ArchWiki에서 한 페이지를 읽어보기:

`archwiki-rs read-page {{페이지_제목}}`

- 지정된 형식으로 ArchWiki에서 페이지를 읽음:

`archwiki-rs read-page {{페이지_제목}} --format {{plain-text|markdown|html}}`

- 제공된 텍스트가 포함된 페이지를 ArchWiki에서 검색:

`archwiki-rs search "{{검색_텍스트}}" --text-search`

- 모든 ArchWiki 페이지의 로컬 복사본을 특정 디렉터리로 다운로드:

`archwiki-rs local-wiki {{/경로/대상/로컬_위키}} --format {{plain-text|markdown|html}}`
