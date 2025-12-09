# cargo fmt

> Rust 프로젝트의 모든 소스 파일에 대해 `rustfmt`를 실행.
> 더 많은 정보: <https://github.com/rust-lang/rustfmt>.

- 모든 소스 파일 포맷:

`cargo fmt`

- 파일에 쓰지 않고 포맷 오류를 확인:

`cargo fmt --check`

- 각 `rustfmt` 호출에 인수를 전달:

`cargo fmt -- {{rustfmt_인수}}`
