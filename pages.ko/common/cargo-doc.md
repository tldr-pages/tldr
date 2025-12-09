# cargo doc

> Rust 패키지의 문서를 작성.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- 현재 프로젝트와 모든 종속성에 대한 문서를 작성:

`cargo {{[d|doc]}}`

- 종속성에 대한 문서를 작성하지 않음:

`cargo {{[d|doc]}} --no-deps`

- 브라우저에서 문서를 빌드하고 오픈:

`cargo {{[d|doc]}} --open`

- 특정 패키지의 문서를 빌드하고 확인:

`cargo {{[d|doc]}} --open {{[-p|--package]}} {{패키지}}`
