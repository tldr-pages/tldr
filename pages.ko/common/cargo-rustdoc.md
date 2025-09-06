# cargo rustdoc

> Rust 패키지의 문서를 작성.
> `cargo doc`과 유사하지만, `rustdoc`에 옵션을 전달할 수 있음. 사용 가능한 모든 옵션은 `rustdoc --help`를 참조.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- `rustdoc`에 옵션을 전달:

`cargo rustdoc -- {{rustdoc_옵션}}`

- 문서 린트에 대해 경고:

`cargo rustdoc -- --warn rustdoc::{{린트_이름}}`

- 문서 린트를 무시:

`cargo rustdoc -- --allow rustdoc::{{린트_이름}}`

- 패키지 라이브러리를 문서화:

`cargo rustdoc --lib`

- 지정된 바이너리를 문서화:

`cargo rustdoc --bin {{이름}}`

- 지정된 예시를 문서화:

`cargo rustdoc --example {{이름}}`

- 지정된 통합 테스트를 문서화:

`cargo rustdoc --test {{이름}}`
