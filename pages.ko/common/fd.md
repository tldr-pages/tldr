# fd

> `find`의 대안.
> `find`보다 더 빠르고 쉽게 사용하는 것을 목표.
> 더 많은 정보: <https://github.com/sharkdp/fd#how-to-use>.

- 현재 디렉터리에서 특정 패턴과 일치하는 파일을 반복적으로 찾음:

`fd "{{string|regex}}"`

- `foo`로 시작하는 파일 찾기:

`fd "^foo"`

- 특정 확장자를 가진 파일 찾기:

`fd --extension txt`

- 특정 디렉터리에서 파일 찾기:

`fd "{{string|regex}}" {{경로/대상/디렉터리}}`

- 검색에 무시되거나 숨겨진 파일을 포함:

`fd --hidden --no-ignore "{{string|regex}}"`

- 반환된 각 검색 결과에 대해 명령을 실행:

`fd "{{string|regex}}" --exec {{명령어}}`
