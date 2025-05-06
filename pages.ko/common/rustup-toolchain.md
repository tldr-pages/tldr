# rustup toolchain

> Rust 툴체인 관리.
> 툴체인에 대한 자세한 정보는 `rustup help toolchain`을 참조.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 주어진 툴체인 설치 또는 업데이트:

`rustup toolchain install {{툴체인}}`

- 툴체인 제거:

`rustup toolchain uninstall {{툴체인}}`

- 설치된 툴체인 나열:

`rustup toolchain list`

- 디렉토리에 대한 심볼릭 링크를 통해 사용자 지정 툴체인 생성:

`rustup toolchain link {{사용자_지정_툴체인_이름}} {{경로/대상/폴더}}`
