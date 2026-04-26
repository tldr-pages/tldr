# fd

> `find`의 대안.
> 관련 항목: `find`.
> 더 많은 정보: <https://github.com/sharkdp/fd#how-to-use>.

- 현재 디렉터리에서 특정 패턴과 일치하는 파일을 재귀적으로 찾기:

`fd "{{regex}}"`

- 특정 디렉터리에서 파일 찾기:

`fd "{{regex}}" {{경로/대상/디렉터리}}`

- 특정 확장자를 가진 파일 찾기:

`fd {{[-e|--extension]}} {{txt}}`

- 특정 패턴과 일치하는 디렉터리만 찾기:

`fd {{[-t|--type]}} {{d|directory}} "{{regex}}"`

- 검색에 무시되거나 숨겨진 파일을 포함:

`fd {{[-H|--hidden]}} {{[-I|--no-ignore]}} "{{regex}}"`

- 특정 glob 패턴과 일치하는 파일을 제외:

`fd {{regex}} {{[-E|--exclude]}} {{glob}}`

- 반환된 각 검색 결과에 대해 명령을 실행:

`fd "{{regex}}" {{[-x|--exec]}} {{명령어}}`

- 현재 디렉터리에서만 파일 찾기:

`fd {{[-d|--max-depth]}} 1 "{{regex}}"`
