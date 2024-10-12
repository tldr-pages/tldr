# rustup-init.sh

> `rustup` 및 Rust 툴체인을 설치하는 스크립트.
> 더 많은 정보: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- `rustup` 및 기본 Rust 툴체인을 설치하기 위해 `rustup-init` 다운로드 및 실행:

`curl https://sh.rustup.rs -sSf | sh -s`

- `rustup-init` 다운로드 및 실행하고 인자를 전달:

`curl https://sh.rustup.rs -sSf | sh -s -- {{인자}}`

- `rustup-init` 실행 및 추가 구성 요소나 타겟 지정하여 설치:

`rustup-init.sh --target {{타겟}} --component {{구성_요소}}`

- `rustup-init` 실행 및 설치할 기본 툴체인 지정:

`rustup-init.sh --default-toolchain {{툴체인}}`

- `rustup-init` 실행하고 툴체인 설치하지 않기:

`rustup-init.sh --default-toolchain {{none}}`

- `rustup-init` 실행 및 설치 프로필 지정:

`rustup-init.sh --profile {{minimal|default|complete}}`

- 확인 요청 없이 `rustup-init` 실행:

`rustup-init.sh -y`
