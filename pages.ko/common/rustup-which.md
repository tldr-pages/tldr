# rustup which

> `rustup`에 의해 관리되는 명령에 대해 실행될 바이너리를 표시.
> `which`와 유사하지만, `$PATH` 대신 Rust 도구 체인을 검색.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 기본 도구 체인에서 바이너리의 경로 표시:

`rustup which {{명령}}`

- 지정된 도구 체인에서 바이너리의 경로 표시 (`rustup help toolchain`에서 더 많은 정보 확인):

`rustup which --toolchain {{도구_체인}} {{명령}}`
