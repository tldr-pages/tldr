# secret-tool

> `libsecret` 패키지의 일부로 비밀번호를 저장하고 검색.
> `gnome-keyring`과 같은 Freedesktop 비밀 서비스 구현과 통신.
> 더 많은 정보: <https://gnome.pages.gitlab.gnome.org/libsecret/>.

- 선택적 레이블과 함께 비밀 저장:

`secret-tool store --label={{레이블}} {{키}} {{값}}`

- 비밀 검색:

`secret-tool lookup key {{키}}`

- 비밀에 대한 추가 정보 얻기:

`secret-tool search key {{키}}`

- 저장된 비밀 삭제:

`secret-tool clear key {{키}}`
