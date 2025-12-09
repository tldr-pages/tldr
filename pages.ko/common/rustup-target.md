# rustup target

> 툴체인의 지원 대상 수정.
> `--toolchain` 옵션이 없으면 `rustup`은 기본 툴체인을 사용합니다. 툴체인에 대한 자세한 정보는 `rustup help toolchain`을 참조하세요.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 툴체인에 대상 추가:

`rustup target add --toolchain {{툴체인}} {{대상}}`

- 툴체인에서 대상 제거:

`rustup target remove --toolchain {{툴체인}} {{대상}}`

- 툴체인의 사용 가능 및 설치된 대상 나열:

`rustup target list --toolchain {{툴체인}}`

- 툴체인에 설치된 대상 나열:

`rustup target list --toolchain {{툴체인}} --installed`
