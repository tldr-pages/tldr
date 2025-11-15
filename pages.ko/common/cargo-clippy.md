# cargo clippy

> 일반적인 실수를 포착하고 Rust 코드를 개선하기 위한 린트 모음.
> 더 많은 정보: <https://github.com/rust-lang/rust-clippy>.

- 현재 디렉터리의 코드에 대한 검사를 실행:

`cargo clippy`

- `Cargo.lock`이 최신 버전이어야 함:

`cargo clippy --locked`

- 작업공간의 모든 패키지에 대해 검사 실행:

`cargo clippy --workspace`

- Run checks for a package:

`cargo clippy --package {{패키지}}`

- 린트 그룹에 대한 검사 실행 (<https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious> 참조):

`cargo clippy -- --warn clippy::{{린트_그룹}}`

- 경고를 오류로 처리:

`cargo clippy -- --deny warnings`

- 검사를 실행하고 경고를 무시:

`cargo clippy -- --allow warnings`

- Clippy 제안을 자동으로 적용:

`cargo clippy --fix`
