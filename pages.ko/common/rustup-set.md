# rustup set

> `rustup` 설정 변경.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 기본 호스트 트리플 설정:

`rustup set default-host {{호스트_트리플}}`

- 기본 프로필 설정 (`minimal`은 `rustc`, `rust-std`, `cargo`만 포함하고, `default`는 `rust-docs`, `rustfmt`, `clippy`를 추가로 포함):

`rustup set profile {{minimal|default}}`

- `rustup update` 실행 시 `rustup` 자체 업데이트 여부 설정:

`rustup set auto-self-update {{enable|disable|check-only}}`
