# rustfmt

> Rust 소스 코드를 포맷합니다.
> 더 많은 정보: <https://github.com/rust-lang/rustfmt>.

- 파일을 포맷하여 원본 파일을 덮어쓰기:

`rustfmt {{경로/대상/source.rs}}`

- 파일의 포맷을 확인하고 변경 사항을 콘솔에 표시:

`rustfmt --check {{경로/대상/source.rs}}`

- 포맷하기 전에 변경된 파일을 백업 (원본 파일은 `.bk` 확장자로 이름이 변경됩니다):

`rustfmt --backup {{경로/대상/source.rs}}`
