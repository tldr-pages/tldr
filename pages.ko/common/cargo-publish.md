# cargo publish

> 패키지를 레지스트리에 업로드.
> 참고: 패키지를 게시하기 전에 `cargo login`을 사용하여 인증 토큰을 추가해야 함.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- 검사를 수행하고, `.crate` 파일을 생성하여 레지스트리에 업로드:

`cargo publish`

- 검사를 수행하고, `.crate` 파일을 생성하여 레지스트리에 업로드하지 않음 (`cargo package`와 동일):

`cargo publish --dry-run`

- 지정된 레지스트리를 사용함 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo publish --registry {{이름}}`
