# jj file search

> `jj` 저장소 파일에서 내용을 검색.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-search>.

- 작업 복사본에서 정규 표현식(`regex`)을 포함하는 파일 검색:

`jj file search {{[-p|--pattern]}} "{{regex}}"`

- glob 패턴과 일치하는 내용을 포함하는 파일 검색:

`jj file search {{[-p|--pattern]}} "{{glob:*pattern*}}"`

- 지정한 리비전 파일에서 내용 검색:

`jj file search {{[-r|--revision]}} {{revision}} {{[-p|--pattern]}} "{{패턴}}"`

- 지정한 경로 또는 파일에서만 내용 검색:

`jj file search {{[-p|--pattern]}} "{{패턴}}" {{경로/대상/파일_또는_디렉터리}}`
