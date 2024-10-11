# rustup

> Rust 툴체인을 설치, 관리 및 업데이트.
> `toolchain`, `target`, `update` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 시스템에 nightly 툴체인 설치:

`rustup install nightly`

- 기본 툴체인을 nightly로 전환하여 `cargo` 및 `rustc` 명령이 이를 사용하도록 설정:

`rustup default nightly`

- 현재 프로젝트 내에서만 nightly 툴체인을 사용하고 전역 설정은 변경하지 않음:

`rustup override set nightly`

- 모든 툴체인 업데이트:

`rustup update`

- 설치된 툴체인 나열:

`rustup show`

- 특정 툴체인으로 `cargo build` 실행:

`rustup run {{툴체인}} cargo build`

- 기본 웹 브라우저에서 로컬 Rust 문서 열기:

`rustup doc`
