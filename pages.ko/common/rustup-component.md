# rustup component

> 툴체인에 설치된 구성 요소를 수정.
> `--toolchain` 옵션 없이 사용하면 `rustup`은 기본 툴체인을 사용합니다. 툴체인에 대한 자세한 내용은 `rustup help toolchain`을 참조하세요.
> 더 많은 정보: <https://rust-lang.github.io/rustup>.

- 툴체인에 구성 요소 추가:

`rustup component add --toolchain {{툴체인}} {{구성_요소}}`

- 툴체인에서 구성 요소 제거:

`rustup component remove --toolchain {{툴체인}} {{구성_요소}}`

- 툴체인에 대해 설치된 및 사용 가능한 구성 요소 나열:

`rustup component list --toolchain {{툴체인}}`

- 툴체인에 대해 설치된 구성 요소 나열:

`rustup component list --toolchain {{툴체인}} --installed`
