# cargo test

> Rust 패키지의 단위 및 통합 테스트를 실행.
> 더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- 이름에 특정 문자열이 포함된 테스트만 실행:

`cargo {{[t|test]}} {{테스트명}}`

- 동시 실행 테스트 케이스 수 설정:

`cargo {{[t|test]}} -- --test-threads {{숫자}}`

- 최적화를 통해, 릴리스 모드에서 아티팩트 테스트:

`cargo {{[t|test]}} {{[-r|--release]}}`

- 작업공간의 모든 패키지를 테스트:

`cargo {{[t|test]}} --workspace`

- 특정 패키지에 대한 테스트를 실행:

`cargo {{[t|test]}} {{[-p|--package]}} {{패키지}}`

- 테스트 실행의 출력을 숨기지 않고 테스트를 실행:

`cargo {{[t|test]}} -- --nocapture`
