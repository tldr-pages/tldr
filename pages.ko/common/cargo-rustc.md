# cargo rustc

> Rust 패키지를 컴파일. `cargo build`와 유사하지만, 컴파일러에 추가 옵션을 전달할 수 있음.
> 사용 가능한 모든 옵션은 `rustc --help`를 참조.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- 패키지를 빌드하고 `rustc`에 옵션을 전달:

`cargo rustc -- {{rustc_옵션}}`

- 최적화를 통해 릴리스 모드에서 아티팩트 빌드:

`cargo rustc --release`

- 현재 CPU에 대한 아키텍처별 최적화로 컴파일:

`cargo rustc --release -- -C target-cpu=native`

- 속도 최적화로 컴파일:

`cargo rustc -- -C opt-level {{1|2|3}}`

- 크기([s]ize) 최적화로 컴파일 (`z` 또한 루프 벡터화를 끔):

`cargo rustc -- -C opt-level {{s|z}}`

- 패키지가 안전하지 않은 코드를 사용하는지 확인:

`cargo rustc --lib -- -D unsafe-code`

- 특정 패키지 빌드:

`cargo rustc --package {{패키지}}`

- 지정된 바이너리만 빌드:

`cargo rustc --bin {{이름}}`
