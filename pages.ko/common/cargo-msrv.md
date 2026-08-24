# cargo msrv

> 프로젝트의 최소 지원 Rust 버전(Minimum Supported Rust Version-MSRV)을 관리.
> 더 많은 정보: <https://gribnau.dev/cargo-msrv/>.

- 의존성 MSRV 목록 출력 (`Cargo.toml`에 명시된 기준):

`cargo msrv list`

- 다양한 Rust 툴체인으로 컴파일을 시도해 프로젝트의 MSRV 탐색:

`cargo msrv find`

- `Cargo.toml`에 명시된 프로젝트의 MSRV 출력:

`cargo msrv show`

- `Cargo.toml`에 지정한 Rust 버전으로 MSRV 설정:

`cargo msrv set {{버전}}`

- 지정한 Rust 버전으로 컴파일하여 MSRV을 충족하는지 아닌지 검증:

`cargo msrv verify`
