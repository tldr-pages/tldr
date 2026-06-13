# cargo build

> 로컬 패키지와 모든 종속성을 컴파일.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- 로컬 경로의 `Cargo.toml` 매니페이스트 파일에 의해 정의된 패키지를 빌드:

`cargo {{[b|build]}}`

- 최적화를 통해 릴리스 모드에서 아티팩트 빌드:

`cargo {{[b|build]}} {{[-r|--release]}}`

- `Cargo.lock`이 최신 버전이어야 함:

`cargo {{[b|build]}} --locked`

- 작업공간에서 모든 패키지를 빌드:

`cargo {{[b|build]}} --workspace`

- 특정 패키지를 빌드:

`cargo {{[b|build]}} {{[-p|--package]}} {{패키지}}`

- 지정된 바이너리만 빌드:

`cargo {{[b|build]}} --bin {{이름}}`

- 지정된 테스트 대상만 빌드:

`cargo {{[b|build]}} --test {{테스트이름}}`
