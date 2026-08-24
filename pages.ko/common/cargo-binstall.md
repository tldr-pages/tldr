# cargo binstall

> CI 아티팩트에서 Rust 바이너리를 설치.
> 사용 가능한 바이너리가 없을 경우 `cargo install` (소스 코드 빌드)로 대체됨.
> 더 많은 정보: <https://github.com/cargo-bins/cargo-binstall>.

- <https://crates.io>에서 패키지 설치:

`cargo binstall {{패키지}}`

- 특정 버전의 패키지 설치 (기본값은 최신 버전):

`cargo binstall {{패키지}}@{{버전}}`

- 확인 프롬프트 없이 패키지 설치:

`cargo binstall {{[-y|--no-confirm]}} {{패키지}}`
