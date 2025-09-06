# cargo clean

> `target` 디렉터리에서 생성된 아티팩트를 제거.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- 전체 `target` 디렉터리를 제거:

`cargo clean`

- 문서 아티팩트 제거 (`target/doc` 디렉터리):

`cargo clean --doc`

- 릴리스 아티팩트 제거 (`target/release` 디렉터리):

`cargo clean --release`

- 지정된 프로필의 디렉터리에서 아티팩트를 제거 (이 경우, `target/debug`):

`cargo clean --profile {{dev}}`
