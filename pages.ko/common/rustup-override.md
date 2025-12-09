# rustup override

> 디렉터리 툴체인 오버라이드를 수정합니다.
> 툴체인에 대한 자세한 내용은 `rustup help toolchain`을 참조하세요.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 디렉터리 툴체인 오버라이드 목록 표시:

`rustup override list`

- 현재 디렉터리에 대한 오버라이드 툴체인 설정 (즉, 해당 디렉터리에서 `cargo`, `rustc` 등을 특정 툴체인으로 실행하도록 `rustup`에 지시):

`rustup override set {{toolchain}}`

- 현재 디렉터리에 대한 툴체인 오버라이드 제거:

`rustup override unset`

- 더 이상 존재하지 않는 디렉터리에 대한 모든 툴체인 오버라이드 제거:

`rustup override unset --nonexistent`
