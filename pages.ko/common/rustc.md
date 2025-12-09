# rustc

> Rust 컴파일러.
> Rust 프로젝트는 보통 `rustc`를 직접 호출하는 대신 `cargo`를 사용합니다.
> 더 많은 정보: <https://doc.rust-lang.org/rustc>.

- 바이너리 크레이트 컴파일:

`rustc {{경로/대상/main.rs}}`

- 최적화하여 컴파일 (`s`는 바이너리 크기 최적화를 의미하며, `z`는 더 많은 최적화를 포함):

`rustc -C lto -C opt-level={{0|1|2|3|s|z}} {{경로/대상/main.rs}}`

- 디버깅 정보 포함하여 컴파일:

`rustc -g {{경로/대상/main.rs}}`

- 오류 메시지 설명:

`rustc --explain {{오류_코드}}`

- 현재 CPU에 대한 아키텍처별 최적화로 컴파일:

`rustc -C target-cpu={{native}} {{경로/대상/main.rs}}`

- 대상 목록 표시 (참고: 컴파일하려는 대상은 먼저 `rustup`을 사용하여 추가해야 함):

`rustc --print target-list`

- 특정 대상에 대해 컴파일:

`rustc --target {{타겟_트리플}} {{경로/대상/main.rs}}`
