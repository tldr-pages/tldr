# gpgconf

> .gnupg 홈 디렉터리를 수정.
> 더 많은 정보: <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>.

- 모든 컴포넌트 나열:

`gpgconf --list-components`

- gpgconf가 사용하는 디렉토리를 나열:

`gpgconf --list-dirs`

- 컴포넌트의 모든 옵션을 나열:

`gpgconf --list-options {{컴포넌트}}`

- 프로그램을 나열하고 실행 가능한지 테스트:

`gpgconf --check-programs`

- 컴포넌트 리로드:

`gpgconf --reload {{컴포넌트}}`
