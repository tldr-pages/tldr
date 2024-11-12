# rustdoc

> Rust 크레이트에 대한 문서를 생성합니다.
> 더 많은 정보: <https://doc.rust-lang.org/stable/rustdoc>.

- 크레이트의 루트에서 문서 생성:

`rustdoc {{src/lib.rs}}`

- 프로젝트 이름 지정:

`rustdoc {{src/lib.rs}} --crate-name {{이름}}`

- 마크다운 파일에서 문서 생성:

`rustdoc {{경로/대상/파일.md}}`

- 출력 디렉토리 지정:

`rustdoc {{src/lib.rs}} --out-dir {{경로/대상/출력_디렉토리}}`
