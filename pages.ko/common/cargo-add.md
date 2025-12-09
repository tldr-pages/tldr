# cargo add

> Rust 프로젝트의 `Cargo.toml` 매니페스트에 종속성을 추가.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- 현재 프로젝트에 최신 버전의 종속성을 추가:

`cargo add {{의존성}}`

- 특정 버전의 종속성을 추가:

`cargo add {{의존성}}@{{버전}}`

- 종속성을 추가하고 하나 이상의 특정 기능을 활성화:

`cargo add {{의존성}} --features {{기능_1}},{{기능_2}}`

- 선택적 종속성을 추가하면, 크레이트의 기능으로 노출됨:

`cargo add {{의존성}} --optional`

- 로컬 크레이트를 종속성으로 추가:

`cargo add --path {{경로/대상/크레이트_디렉토리}}`

- 개발 또는 빌드 종속성을 추가:

`cargo add {{의존성}} --{{dev|build}}`

- 모든 기본 기능이 비활성화된 종속성을 추가:

`cargo add {{의존성}} --no-default-features`
